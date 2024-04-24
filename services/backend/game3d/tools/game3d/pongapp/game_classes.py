import time 
import threading
import asyncio
import logging
from channels.layers import get_channel_layer
from . import initvalues

logger = logging.getLogger(__name__)

class   paddleC:

    def __init__(self, player, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if (player == 1):
            self.positionX = initvalues.PADDLE1_POSITION_X
            self.positionY = 0
            self.scaleY = 0
            self.scaleZ = 0
            self.width = initvalues.PADDLE1_WIDTH
            self.height = initvalues.PADDLE1_HEIGHT
            self.dirY = initvalues.PADDLE1_DIR_Y
            self.speed = initvalues.PADDLE1_SPEED
            self.move = "false";
        else :
            self.positionX = initvalues.PADDLE2_POSITION_X
            self.positionY = 0
            self.scaleY = 0
            self.scaleZ = 0
            self.width = initvalues.PADDLE2_WIDTH
            self.height = initvalues.PADDLE2_HEIGHT
            self.dirY = initvalues.PADDLE2_DIR_Y
            self.speed = initvalues.PADDLE2_SPEED
            self.move = "false";

class   ballC:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positionX = initvalues.BALL_POSITION_X
        self.positionY = initvalues.BALL_POSITION_Y
        self.dirX = initvalues.BALL_DIR_X
        self.dirY = initvalues.BALL_DIR_Y
        self.speed = initvalues.BALL_SPEED


class   gameStateC:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = 0
        self.players_nb = 0
        self.player1Score = initvalues.PADDLE1_SCORE
        self.player2Score = initvalues.PADDLE2_SCORE
        self.limitScore = initvalues.SMALL_LIMIT_SCORE
        self.paddle1 = 0
        self.paddle2 = 0
        self.ball = ballC()
        self.active = 0
        self._lock = threading.Lock()

    async def run_game_loop(self):
        self.active = 1 
        while self.active:
            with self._lock:
                self.ballPhysics(self.ball)
                self.paddlePhysics(self.ball, self.paddle1, self.paddle2)
                #self.paddle1Movement(self.paddle1)
                #self.paddle2Movement(self.paddle2)

            await asyncio.sleep(0.016)
            #self.logObject()
            await self.broadcastGameState()

    def ballPhysics(self, ball):
        if (ball.positionX <= -initvalues.FIELD_WIDTH / 2):
            self.resetBall(self.ball, 2)
        if (ball.positionX >= initvalues.FIELD_WIDTH / 2):
            self.resetBall(self.ball, 1)
        if (ball.positionY <= -initvalues.FIELD_HEIGHT / 2):
            ball.dirY = -ball.dirY
        if (ball.positionY >= initvalues.FIELD_HEIGHT / 2):
            ball.dirY = -ball.dirY
        ball.positionX += ball.dirX * ball.speed
        ball.positionY += ball.dirY * ball.speed
        if (ball.dirY > ball.speed * 2):
            ball.dirY = ball.speed * 2
        if (ball.dirY < -ball.speed * 2):
            ball.dirY = -ball.speed * 2

    def resetBall(self, ball, index):
        ball.positionX = 0
        ball.positionY = 0

        if (index == 1):
            self.player1Score += 1
            ball.dirX = -1
        else:
            self.player2Score += 1
            ball.dirX = 1
        ball.dirY = 1
        self.checkForScore()

    def checkForScore(self):
        if (self.player1Score == self.limitScore or self.player2Score == self.limitScore):
            self.active = 0

    def paddlePhysics(self, ball, paddle1, paddle2):
        if (ball.positionX <= paddle1.positionX + paddle1.width and ball.positionX >= paddle1.positionX):
            if (ball.positionY <= paddle1.positionY + paddle1.height / 2 and ball.positionY >= paddle1.positionY - paddle1.height / 2):
                if (ball.dirX < 0):
                    ball.dirX = -ball.dirX
                    ball.dirY -= paddle1.dirY * 0.7
        if (ball.positionX <= paddle2.positionX + paddle2.width and ball.positionX >= paddle2.positionX):
            if (ball.positionY <= paddle2.positionY + paddle2.height / 2 and ball.positionY >= paddle2.positionY - paddle2.height / 2):
                if (ball.dirX > 0):
                    ball.dirX = -ball.dirX
                    ball.dirY -= paddle2.dirY * 0.7

    def paddle1Movement(self, paddle1):
        if (paddle1.move == "left"):
            if (paddle1.positionY < initvalues.FIELD_HEIGHT * 0.45):
                paddle1.dirY = paddle1.speed * 0.5
            else:
                paddle1.dirY = 0
        elif (paddle1.move == "right"):
            if (paddle1.positionY > -initvalues.FIELD_HEIGHT * 0.45):
                paddle1.dirY = -paddle1.speed * 0.5
            else:
                paddle1.dirY = 0
        else:
            paddle1.dirY = 0
        paddle1.scaleY += (1 - paddle1.scaleY) * 0.2
        paddle1.scaleZ += (1 - paddle1.scaleZ) * 0.2
        paddle1.positionY += paddle1.dirY

    def paddle2Movement(self, paddle2):
        if (paddle2.move == "right"):
            if (paddle2.positionY < initvalues.FIELD_HEIGHT * 0.45):
                paddle2.dirY = paddle2.speed * 0.5
            else:
                paddle2.dirY = 0
        elif (paddle2.move == "left"):
            if (paddle2.positionY > -initvalues.FIELD_HEIGHT * 0.45):
                paddle2.dirY = -paddle2.speed * 0.5
            else:
                paddle2.dirY = 0
        else:
            paddle2.dirY = 0
        paddle2.scaleY += (1 - paddle2.scaleY) * 0.2
        paddle2.scaleZ += (1 - paddle2.scaleZ) * 0.2
        paddle2.positionY += paddle2.dirY

    async def broadcastGameState(self):
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            self.group_name,
            {
                "type": "game.state",
                "game_state": {
                    "player1Score": self.player1Score,
                    "player2Score": self.player2Score,
                    "limitScore": self.limitScore,
                    "paddle1.positionX": self.paddle1.positionX,
                    "paddle1.positionY": self.paddle1.positionY,
                    "paddle1.width": self.paddle1.width,
                    "paddle2.positionX": self.paddle2.positionX,
                    "paddle2.positionY": self.paddle2.positionY,
                    "paddle2.width": self.paddle2.width,
                    "ball.positionX": self.ball.positionX,
                    "ball.positionY": self.ball.positionY,
                    "active": self.active
                }
            }
        )
        
    def logObject(self):

        logbuff = self
        logger.info("group_name : %s" % (logbuff.group_name))
        logger.info("players_nb : %d" % (logbuff.players_nb))
        logger.info("player1Score : %d" % (logbuff.player1Score))
        logger.info("player2Score : %d" % (logbuff.player2Score))
        logger.info("paddle1.positionX : %d" % (logbuff.paddle1.positionX))
        logger.info("paddle1.positionY : %d" % (logbuff.paddle1.positionY))
        logger.info("paddle1.scaleY : %d" % (logbuff.paddle1.scaleY))
        logger.info("paddle1.scaleZ : %d" % (logbuff.paddle1.scaleZ))
        logger.info("paddle1.width : %d" % (logbuff.paddle1.width))
        logger.info("paddle1.height : %d" % (logbuff.paddle1.height))
        logger.info("paddle1.dirY : %d" % (logbuff.paddle1.dirY))
        logger.info("paddle1.speed : %d" % (logbuff.paddle1.speed))
        logger.info("paddle1.move : %s" % (logbuff.paddle1.move))
        logger.info("paddle2.positionX : %d" % (logbuff.paddle2.positionX))
        logger.info("paddle2.positionY : %d" % (logbuff.paddle2.positionY))
        logger.info("paddle2.scaleY : %d" % (logbuff.paddle2.scaleY))
        logger.info("paddle2.scaleZ : %d" % (logbuff.paddle2.scaleZ))
        logger.info("paddle2.width : %d" % (logbuff.paddle2.width))
        logger.info("paddle2.height : %d" % (logbuff.paddle2.height))
        logger.info("paddle2.dirY : %d" % (logbuff.paddle2.dirY))
        logger.info("paddle2.speed : %d" % (logbuff.paddle2.speed))
        logger.info("paddle2.move : %s" % (logbuff.paddle2.move))
        logger.info("ball.positionY : %d" % (logbuff.ball.positionY))
        logger.info("ball.positionX : %d" % (logbuff.ball.positionX))
        logger.info("ball.dirX : %d" % (logbuff.ball.dirX))
        logger.info("ball.dirY : %d" % (logbuff.ball.dirY))
        logger.info("ball.speed : %d" % (logbuff.ball.speed))
        logger.info("active : %d" % (logbuff.active))

