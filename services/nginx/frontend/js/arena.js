
//////////////////////////////////////////////////////////////////////
////    SOCKETS
//////////////////////////////////////////////////////////////////////

// let gameState = "Dialogs"

const socket = new WebSocket("ws://localhost:8080/ws/challenger/");

socket.onopen = function(event) {
    console.log("WebSocket connection opened.");

    // Envoi d'un message au serveur
    socket.send(JSON.stringify({
        type: "message",
        content: "Hello, server!"
    }));
};

// Fonction exécutée lorsqu'un message est reçu du serveur
socket.onmessage = function(event) {
    const message = JSON.parse(event.data);
    console.log("Message received from server:", message);
};

// Fonction exécutée lorsque la connexion WebSocket est fermée
socket.onclose = function(event) {
    console.log("WebSocket connection closed.");
};

// Fonction exécutée en cas d'erreur de connexion WebSocket
socket.onerror = function(error) {
    console.error("WebSocket error:", error);
};


//////////////////////////////////////////////////////////////////////
////    HANDLE KEYBOARD
//////////////////////////////////////////////////////////////////////

// function gestionToucheEnfoncee(event) {
//     // Vérifier si la touche enfoncée est une flèche du clavier
//     // if (event.keyCode >= 37 && event.keyCode <= 40) {
//     //     // Afficher un message dans la console avec le code de la touche
//     //     console.log("Flèche du clavier enfoncée : " + event.keyCode);
//     // }
//     // if (event.keyCode == 13)
//     //     console.log("Touche enter enfoncée");
//     if (gameState == "Dialogs")
//         gameState = "Menu";
//     else
//         gameState = "Dialogs";
    
//     // updateCanvas();
// }

// Ajouter un écouteur d'événements pour détecter quand une touche du clavier est enfoncée
// document.addEventListener("keydown", gestionToucheEnfoncee);

// const context = canvas.getContext("2d");

// document.addEventListener("DOMContentLoaded", function() {

class Arena {
    constructor() {
        this.canvas = document.createElement("canvas");
        this.canvas.width = 500;
        this.canvas.height = 500;
        this.context = this.canvas.getContext("2d");
        this.gameState = "Dialogs";
        this.handleKeyDown = this.handleKeyDown.bind(this); // Bind the method to the instance
        document.addEventListener("keydown", this.handleKeyDown);
    }

    getDivArena()
    {
        const divArena = document.createElement("div");

        // const canvas = document.createElement("canvas");
        this.canvas.width = 500;
        this.canvas.height = 500;
        this.context = this.canvas.getContext("2d");
        // this.drawArena();
        divArena.appendChild(this.canvas);
        document.body.appendChild(divArena);
        return divArena;
    }

    drawLifeBar(length, x, y)
    {
        this.context.fillStyle = "#506860";
        this.context.fillRect(x, y, 97.5, 6);
        let color1;
        if (length < 45)
            color1 = "#b9992d";
        else
            color1 = "#58d080";
        this.context.fillStyle = color1
        this.context.fillRect(x, y, length, 2);
        let color2;
        if (length < 45)
            color2 = "#f9df4f";
        else
            color2 = "#70f8a8";
        this.context.fillStyle = color2;
        this.context.fillRect(x, y+2, length, 4);
    }

    drawExpBar(length, x, y) {
        this.context.fillStyle = "#5ad7f8"
        this.context.fillRect(x, y, length, 5);
    }
    

    // 
    drawArena()
    {
        // recuperer le background
        const imgBackground = new Image();
        imgBackground.src="./images/Battle/GBFormat-BASE.png";
        imgBackground.onload = () => {
            // Dessin de l'image sur le canvas
            this.context.drawImage(imgBackground, 0, 0, this.canvas.width, this.canvas.height);
        }

        // recuperer 2 pokemon
        let opponentPokemon = "Bulbizarre"
        const imgOpponentPokemon = new Image();
        imgOpponentPokemon.src="./images/Persos/Pokemon-Tileset/" + opponentPokemon + "Front.png";
        imgOpponentPokemon.onload = () => {
            this.context.drawImage(imgOpponentPokemon, this.canvas.width * 3.1 / 5, this.canvas.height / 2.8, imgOpponentPokemon.width * 2, imgOpponentPokemon.height * 2);
        }
        let allyPokemon = "Bulbizarre"
        const imgAllyPokemon = new Image();
        imgAllyPokemon.src="./images/Persos/Pokemon-Tileset/" + allyPokemon + "Back.png";
        imgAllyPokemon.onload = () => {
            this.context.drawImage(imgAllyPokemon, this.canvas.width / 6.3, this.canvas.height / 1.765, imgAllyPokemon.width * 2, imgAllyPokemon.height * 2);
        }
    
        // recuperer les barres de vie
        const imgLifeBar = new Image();
        imgLifeBar.src="./images/Battle/GBFormat-LifeLevels.png";
        imgLifeBar.onload = () =>
        {
            this.context.drawImage(imgLifeBar, 0, 0, this.canvas.width, this.canvas.height);
            this.context.font = "bold 14px Arial";
            this.context.fillStyle = "black";
            this.context.fillText(allyPokemon, this.canvas.width / 1.4, this.canvas.height * 0.635);
            this.context.fillText(opponentPokemon, this.canvas.width * 0.2, this.canvas.height * 0.315);
    
            // remplir barre d'exp
            let expBar = 64;
            this.drawExpBar(expBar * 130 / 100, this.canvas.width * 0.67, this.canvas.height * 0.73);
    
            // remplir les barres de pv
            let pvOpponent = 60;
            let pvAlly = 80;
            this.drawLifeBar(pvOpponent * 97.5 / 100, this.canvas.width * 0.217, this.canvas.height * 0.341);
            this.drawLifeBar(pvAlly * 97.5 / 100, this.canvas.width * 0.736, this.canvas.height * 0.66);
    
            // ajouter les lvl
            let lvlOpponent = 5;
            let lvlAlly = 5;
            this.context.font = "bold 14px Arial";
            this.context.fillStyle = "black";
            this.context.fillText(lvlAlly, this.canvas.width * 0.91, this.canvas.height * 0.635);
            this.context.fillText(lvlOpponent, this.canvas.width * 0.39, this.canvas.height * 0.315);
    
            // remplir les menus de selection
    
        }
    
        switch (this.gameState)
        {
            case "Dialogs":
                const imgMenu = new Image();
                imgMenu.src="./images/Battle/GBFormat-BlocActions.png";
                imgMenu.onload = () => {
                    this.context.drawImage(imgMenu, 0, 0, this.canvas.width, this.canvas.height);
                }
                break;
            case "Menu":
                const imgDialogs = new Image();
                imgDialogs.src="./images/Battle/GBFormat-BlocBleu.png";
                imgDialogs.onload = () => {
                    this.context.drawImage(imgDialogs, 0, 0, this.canvas.width, this.canvas.height);
                }
                break;
        }
    }

    handleKeyDown(event)
    {
        if (this.gameState == "Dialogs")
            this.gameState = "Menu";
        else
            this.gameState = "Dialogs";
    }
}

const arena = new Arena();

arena.getDivArena();
setInterval(() => {
    arena.drawArena();
}, 1000);
