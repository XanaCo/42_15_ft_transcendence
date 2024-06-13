import json
import logging
import asyncio
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404
from urllib.parse import parse_qs

from .models import player, default_mapa, litte_house1, litte_house2, big_house1, big_house2
from .serializers import PlayerModelSerializer, editplayerModelSerializer
import random

logger = logging.getLogger(__name__)

class PlayerConsumer(AsyncWebsocketConsumer):
    gID = 0

    async def connect(self):
        await self.accept()
        logger.info("connected")
        self.map_changed = False
        self.send_message_task = asyncio.create_task(self.send_message())


        

    async def disconnect(self, close_code):
        self.send_message_task.cancel()
        user = await sync_to_async(get_object_or_404)(player, userID=self.gID)
        basejson = {
            "userID": user.userID,
            "posX": user.posX,
            "posY": user.posY,
            "lastPosX": user.lastPosX,
            "lastPosY": user.lastPosY,
            "orientation": user.orientation,
            "player_skin": user.player_skin,
            "player_map": user.player_map,
            "player_status": user.player_status,
            "active": False,
        }
        instance = editplayerModelSerializer(user, data=basejson)
        if instance.is_valid():
            await sync_to_async(instance.save,)()


    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            json_data = {}
            id = text_data_json.get("userID")
            if (id and text_data_json.get("action") == "connect"):
                gID = id
                playerobj = await sync_to_async(get_object_or_404)(player, userID=id)
                basejson = {
                    "userID": playerobj.userID,
                    "posX": playerobj.posX,
                    "posY": playerobj.posY,
                    "lastPosX": playerobj.lastPosX,
                    "lastPosY": playerobj.lastPosY,
                    "orientation": playerobj.orientation,
                    "player_skin": playerobj.player_skin,
                    "player_map": playerobj.player_map,
                    "player_status": playerobj.player_status,
                    "active": True,

                }
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
            elif (id and text_data_json.get("action") == "move"):
                playerobj = await sync_to_async(get_object_or_404)(player, userID=id)
                data = text_data_json.get("new")
                basejson = {
                    "userID": playerobj.userID,
                    "posX": playerobj.posX,
                    "posY": playerobj.posY,
                    "lastPosX": playerobj.lastPosX,
                    "lastPosY": playerobj.lastPosY,
                    "orientation": playerobj.orientation,
                    "active": playerobj.active,
                    "player_skin": playerobj.player_skin,
                    "player_map": playerobj.player_map,
                    "player_status": playerobj.player_status,
                }
                match data:
                    case "y+":
                        json_data = await modify_json_ymore(basejson, playerobj)
                    case "y-":
                        json_data = await modify_json_yless(basejson, playerobj)
                    case "x+":
                        json_data = await modify_json_xmore(basejson, playerobj)
                    case "x-":
                        json_data = await modify_json_xless(basejson, playerobj)
                    case _:
                        logger.info("data not found")
                data_json_load = json.loads(json_data)
                if data_json_load.get("event") is not None:
                    await change_status(playerobj, data_json_load)

                else:
                    await reset_status(playerobj)
                
            all_players = await sync_to_async(player.objects.all, thread_sensitive=True)()
            all_players_json = await sync_to_async(PlayerModelSerializer, thread_sensitive=True)(all_players, many=True)
            all_players_data = await sync_to_async(lambda: all_players_json.data, thread_sensitive=True)()
            self.all_players_data = await sync_to_async(json.dumps, thread_sensitive=True)(all_players_data)

        except Exception as e:
            logger.error(f"error: {e}")
        
    async def send_message(self):
        fps = 30
        frame_duration = 1.0 / fps

        while True:
            start_time = asyncio.get_running_loop().time()

            # Envoyer les données stockées
            if hasattr(self, 'all_players_data'):
                await self.send(text_data=self.all_players_data)

            elapsed_time = asyncio.get_running_loop().time() - start_time
            if elapsed_time < frame_duration:
                await asyncio.sleep(frame_duration - elapsed_time)


async def modify_json_xless(basejson, playerobj):
    match basejson["player_map"]:
        case player.MapChoices.DEFAULT:
            choosen_map = default_mapa
        case player.MapChoices.BATIMENT_1:
            choosen_map = litte_house1
        case player.MapChoices.BATIMENT_2:
            choosen_map = litte_house2
        case player.MapChoices.BATIMENT_3:
            choosen_map = big_house1
        case player.MapChoices.BATIMENT_4:
            choosen_map = big_house2
        
    if (basejson["orientation"] == "W"):

        if (choosen_map[playerobj.posY][playerobj.posX - 1] == 0):
            basejson["lastPosX"] = basejson["posX"]
            basejson["posX"] -= 1
            basejson["orientation"] = "W"
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(instance_data)
                return json_data

        elif (choosen_map[playerobj.posY][playerobj.posX - 1] == 2):
            if is_entering_combat():
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, "combat")
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data
            else:
                basejson["lastPosX"] = basejson["posX"]
                basejson["posX"] -= 1
                basejson["orientation"] = "W"
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, None)
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data

        elif (choosen_map[playerobj.posY][playerobj.posX - 1] == 3):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "people")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data

        elif (choosen_map[playerobj.posY][playerobj.posX - 1] in [4, 5, 6, 7]):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "door")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data

        else:
            logger.info("match x- failed")
    else:
        basejson["orientation"] = "W"
        instance = editplayerModelSerializer(playerobj, data=basejson)
        if instance.is_valid():
            await sync_to_async(instance.save,)()
            instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
            data_with_event = await add_event(instance_data, None)
            json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
            return json_data

async def modify_json_xmore(basejson, playerobj):
    
    match basejson["player_map"]:
        case player.MapChoices.DEFAULT:
            choosen_map = default_mapa
        case player.MapChoices.BATIMENT_1:
            choosen_map = litte_house1
        case player.MapChoices.BATIMENT_2:
            choosen_map = litte_house2
        case player.MapChoices.BATIMENT_3:
            choosen_map = big_house1
        case player.MapChoices.BATIMENT_4:
            choosen_map = big_house2
    if (basejson["orientation"] == "E"):
        if (choosen_map[playerobj.posY][playerobj.posX + 1] == 0):
            basejson["lastPosX"] = basejson["posX"]
            basejson["posX"] += 1
            basejson["orientation"] = "E"
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, None)
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data

        elif (choosen_map[playerobj.posY][playerobj.posX + 1] == 2):
            if is_entering_combat():
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, "combat")
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data
            else:
                basejson["lastPosX"] = basejson["posX"]
                basejson["posX"] += 1
                basejson["orientation"] = "E"
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, None)
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data

        elif (choosen_map[playerobj.posY][playerobj.posX + 1] == 3):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "people")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data

        elif (choosen_map[playerobj.posY][playerobj.posX + 1] in [4, 5, 6, 7]):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "door")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data

        else:
            logger.info("match x+ failed")
    else:
        basejson["orientation"] = "E"
        instance = editplayerModelSerializer(playerobj, data=basejson)
        if instance.is_valid():
            await sync_to_async(instance.save,)()
            instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
            data_with_event = await add_event(instance_data, None)
            json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
            return json_data

async def modify_json_yless(basejson, playerobj):
    
    match basejson["player_map"]:
        case player.MapChoices.DEFAULT:
            choosen_map = default_mapa
        case player.MapChoices.BATIMENT_1:
            choosen_map = litte_house1
        case player.MapChoices.BATIMENT_2:
            choosen_map = litte_house2
        case player.MapChoices.BATIMENT_3:
            choosen_map = big_house1
        case player.MapChoices.BATIMENT_4:
            choosen_map = big_house2
            
    if (basejson["orientation"] == "N"):
        if (choosen_map[playerobj.posY - 1 ][playerobj.posX] == 0):
            basejson["lastPosY"] = basejson["posY"]
            basejson["posY"] -= 1
            basejson["orientation"] = "N"
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, None)
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data
            
        elif (choosen_map[playerobj.posY - 1 ][playerobj.posX] == 2):
            if is_entering_combat():
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, "combat")
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data
            else:
                basejson["lastPosY"] = basejson["posY"]
                basejson["posY"] -= 1
                basejson["orientation"] = "N"
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, None)
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data
        elif (choosen_map[playerobj.posY - 1 ][playerobj.posX] == 3):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "people")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data
        elif (choosen_map[playerobj.posY - 1 ][playerobj.posX] in [4, 5, 6, 7]):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "door")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data
        else:
            logger.info("match y- failed")
    else:
        basejson["orientation"] = "N"
        instance = editplayerModelSerializer(playerobj, data=basejson)
        if instance.is_valid():
            await sync_to_async(instance.save,)()
            instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
            data_with_event = await add_event(instance_data, None)
            json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
            return json_data

async def modify_json_ymore(basejson, playerobj):
    
    match basejson["player_map"]:
        case player.MapChoices.DEFAULT:
            choosen_map = default_mapa
        case player.MapChoices.BATIMENT_1:
            choosen_map = litte_house1
        case player.MapChoices.BATIMENT_2:
            choosen_map = litte_house2
        case player.MapChoices.BATIMENT_3:
            choosen_map = big_house1
        case player.MapChoices.BATIMENT_4:
            choosen_map = big_house2
            
    if (basejson["orientation"] == "S"):
        if (choosen_map[playerobj.posY + 1][playerobj.posX] == 0):
            basejson["lastPosY"] = basejson["posY"]
            basejson["posY"] += 1
            basejson["orientation"] = "S"
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, None)
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data
        elif (choosen_map[playerobj.posY + 1][playerobj.posX] == 2):
            if is_entering_combat():
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, "combat")
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data
            else:
                basejson["lastPosY"] = basejson["posY"]
                basejson["posY"] += 1
                basejson["orientation"] = "S"
                instance = editplayerModelSerializer(playerobj, data=basejson)
                if instance.is_valid():
                    await sync_to_async(instance.save,)()
                    instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                    data_with_event = await add_event(instance_data, None)
                    json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                    return json_data
        elif (choosen_map[playerobj.posY + 1][playerobj.posX] == 3):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "people")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data
        elif (choosen_map[playerobj.posY + 1][playerobj.posX] in [4, 5, 6, 7]):
            instance = editplayerModelSerializer(playerobj, data=basejson)
            if instance.is_valid():
                await sync_to_async(instance.save,)()
                instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
                data_with_event = await add_event(instance_data, "door")
                json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
                return json_data
        else:
            logger.info("match y+ failed")
    else:
        basejson["orientation"] = "S"
        instance = editplayerModelSerializer(playerobj, data=basejson)
        if instance.is_valid():
            await sync_to_async(instance.save,)()
            instance_data = await sync_to_async(lambda: instance.data, thread_sensitive=True)()
            data_with_event = await add_event(instance_data, None)
            json_data = await sync_to_async(json.dumps, thread_sensitive=True)(data_with_event)
            return json_data

def is_entering_combat():
    return random.randint(1, 5) == 1

async def add_event(json_data, event):
    json_data["event"] = event
    return json_data


async def change_status(playerobj, json_data):

    basejson = {
        "userID": playerobj.userID,
        "posX": playerobj.posX,
        "posY": playerobj.posY,
        "lastPosX": playerobj.lastPosX,
        "lastPosY": playerobj.lastPosY,
        "orientation": playerobj.orientation,
        "player_skin": playerobj.player_skin,
        "player_map": playerobj.player_map,
        "player_status": playerobj.player_status,
        "active": playerobj.active,
    }
    logger.info(json_data)
    if json_data.get("event") == "combat":
        basejson["player_status"] = player.StatusChoices.FIGHT
    elif json_data.get("event") == "people":
        basejson["player_status"] = player.StatusChoices.TALK
    elif json_data.get("event") == "door":

        if basejson["player_map"] == player.MapChoices.DEFAULT:
            basejson = await change_default_map(basejson)
        else:
            basejson = await change_house(basejson)
    instance = editplayerModelSerializer(playerobj, data=basejson)
    if instance.is_valid():
        await sync_to_async(instance.save,)()

async def reset_status(playerobj):
    basejson = {
        "userID": playerobj.userID,
        "posX": playerobj.posX,
        "posY": playerobj.posY,
        "lastPosX": playerobj.lastPosX,
        "lastPosY": playerobj.lastPosY,
        "orientation": playerobj.orientation,
        "player_skin": playerobj.player_skin,
        "player_map": playerobj.player_map,
        "player_status": playerobj.player_status,
        "active": playerobj.active,
    }
    basejson["player_status"] = player.StatusChoices.DEFAULT
    instance = editplayerModelSerializer(playerobj, data=basejson)
    if instance.is_valid():
        await sync_to_async(instance.save,)()

async def change_default_map(basejson):
    match basejson["orientation"]:
        case "N":
                x = basejson["posX"]
                y = basejson["posY"] - 1
                match default_mapa[y][x]:
                    case 4:
                        basejson["player_map"] = player.MapChoices.BATIMENT_1
                        basejson['posX'] = 5
                        basejson['posY'] = 8
                    case 5:
                        basejson["player_map"] = player.MapChoices.BATIMENT_2
                        basejson['posX'] = 5
                        basejson['posY'] = 8
                    case 6:
                        basejson["player_map"] = player.MapChoices.BATIMENT_3
                        basejson['posX'] = 10
                        basejson['posY'] = 13
                    case 7:
                        basejson["player_map"] = player.MapChoices.BATIMENT_4
                        basejson['posX'] = 10
                        basejson['posY'] = 13
        case "S":
                x = basejson["posX"]
                y = basejson["posY"] + 1
                match default_mapa[y][x]:
                    case 4:
                        basejson["player_map"] = player.MapChoices.BATIMENT_1
                        basejson['posX'] = 5
                        basejson['posY'] = 8                       
                    case 5:
                        basejson["player_map"] = player.MapChoices.BATIMENT_2
                        basejson['posX'] = 5
                        basejson['posY'] = 8
                    case 6:
                        basejson["player_map"] = player.MapChoices.BATIMENT_3
                        basejson['posX'] = 10
                        basejson['posY'] = 13
                    case 7:
                        basejson["player_map"] = player.MapChoices.BATIMENT_4
                        basejson['posX'] = 10
                        basejson['posY'] = 13
            
        case "E":
                x = basejson["posX"] + 1
                y = basejson["posY"]
                match default_mapa[y][x]:
                    case 4:
                        basejson["player_map"] = player.MapChoices.BATIMENT_1
                        basejson['posX'] = 5
                        basejson['posY'] = 8
                    case 5:
                        basejson["player_map"] = player.MapChoices.BATIMENT_2
                        basejson['posX'] = 5
                        basejson['posY'] = 8
                    case 6:
                        basejson["player_map"] = player.MapChoices.BATIMENT_3
                        basejson['posX'] = 10
                        basejson['posY'] = 13
                    case 7:
                        basejson["player_map"] = player.MapChoices.BATIMENT_4
                        basejson['posX'] = 10
                        basejson['posY'] = 13
            
        case "W":
                x = basejson["posX"] - 1
                y = basejson["posY"]
                match default_mapa[y][x]:
                    case 4:
                        basejson["player_map"] = player.MapChoices.BATIMENT_1
                        basejson['posX'] = 5
                        basejson['posY'] = 8
                    case 5:
                        basejson["player_map"] = player.MapChoices.BATIMENT_2
                        basejson['posX'] = 5
                        basejson['posY'] = 8
                    case 6:
                        basejson["player_map"] = player.MapChoices.BATIMENT_3
                    case 7:
                        basejson["player_map"] = player.MapChoices.BATIMENT_4
    
    return basejson

async def change_house(basejson):
    basejson["player_map"] = player.MapChoices.DEFAULT
    basejson['posX'] = 50
    basejson['posY'] = 50
    return basejson