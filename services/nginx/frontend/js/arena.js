
//////////////////////////////////////////////////////////////////////
////    SOCKETS
//////////////////////////////////////////////////////////////////////

let gameState = "Dialogs"

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

function gestionToucheEnfoncee(event) {
    // Vérifier si la touche enfoncée est une flèche du clavier
    // if (event.keyCode >= 37 && event.keyCode <= 40) {
    //     // Afficher un message dans la console avec le code de la touche
    //     console.log("Flèche du clavier enfoncée : " + event.keyCode);
    // }
    // if (event.keyCode == 13)
    //     console.log("Touche enter enfoncée");
    if (gameState == "Dialogs")
        gameState = "Menu";
    else
        gameState = "Dialogs";

    
}

// Ajouter un écouteur d'événements pour détecter quand une touche du clavier est enfoncée
document.addEventListener("keydown", gestionToucheEnfoncee);


document.addEventListener("DOMContentLoaded", function() {

    function drawLifeBar(length, x, y) {
        context.fillStyle = "#506860";
        context.fillRect(x, y, 97.5, 6);
        let color1;
        if (length < 45)
            color1 = "#b9992d";
        else
            color1 = "#58d080";
        context.fillStyle = color1
        context.fillRect(x, y, length, 2);
        let color2;
        if (length < 45)
            color2 = "#f9df4f";
        else
            color2 = "#70f8a8";
        context.fillStyle = color2;
        context.fillRect(x, y+2, length, 4);
    }

    function drawExpBar(length, x, y) {
        context.fillStyle = "#5ad7f8"
        context.fillRect(x, y, length, 5);
    }

    // Création d'un élément canvas
    const canvas = document.createElement("canvas");
    canvas.id = "arena";
    canvas.width = 500;
    canvas.height = 500;
    
    // Dessin sur le canvas (par exemple, un rectangle rouge)
    const context = canvas.getContext("2d");
    context.fillStyle = "red";
    context.fillRect(0, 0, canvas.width, canvas.height);

    // recuperer le background
    const imgBackground = new Image();
    imgBackground.src="./images/Battle/GBFormat-BASE.png";
    imgBackground.onload = function() {
        // Dessin de l'image sur le canvas
        context.drawImage(imgBackground, 0, 0, canvas.width, canvas.height);
    }

    // recuperer 2 pokemon
    let opponentPokemon = "Bulbizarre"
    const imgOpponentPokemon = new Image();
    imgOpponentPokemon.src="./images/Persos/Pokemon-Tileset/" + opponentPokemon + "Front.png";
    imgOpponentPokemon.onload = function() {
        context.drawImage(imgOpponentPokemon, canvas.width * 3.1 / 5, canvas.height / 2.8, imgOpponentPokemon.width * 2, imgOpponentPokemon.height * 2);
    }
    let allyPokemon = "Bulbizarre"
    const imgAllyPokemon = new Image();
    imgAllyPokemon.src="./images/Persos/Pokemon-Tileset/" + allyPokemon + "Back.png";
    imgAllyPokemon.onload = function() {
        context.drawImage(imgAllyPokemon, canvas.width / 6.3, canvas.height / 1.765, imgAllyPokemon.width * 2, imgAllyPokemon.height * 2);
    }

    // recuperer les barres de vie
    const imgLifeBar = new Image();
    imgLifeBar.src="./images/Battle/GBFormat-LifeLevels.png";
    imgLifeBar.onload = function() {
        context.drawImage(imgLifeBar, 0, 0, canvas.width, canvas.height);
        context.font = "bold 14px Arial";
        context.fillStyle = "black";
        context.fillText(allyPokemon, canvas.width / 1.4, canvas.height * 0.635);
        context.fillText(opponentPokemon, canvas.width * 0.2, canvas.height * 0.315);



        // remplir barre d'exp
        let expBar = 64;
        drawExpBar(expBar * 130 / 100, canvas.width * 0.67, canvas.height * 0.73);

        // remplir les barres de pv
        let pvOpponent = 40;
        let pvAlly = 80;
        drawLifeBar(pvOpponent * 97.5 / 100, canvas.width * 0.217, canvas.height * 0.341);
        drawLifeBar(pvAlly * 97.5 / 100, canvas.width * 0.736, canvas.height * 0.66);

        // ajouter les lvl
        let lvlOpponent = 5;
        let lvlAlly = 5;
        context.font = "bold 14px Arial";
        context.fillStyle = "black";
        context.fillText(lvlAlly, canvas.width * 0.91, canvas.height * 0.635);
        context.fillText(lvlOpponent, canvas.width * 0.39, canvas.height * 0.315);

        // remplir les menus de selection

    }


    switch (gameState)
    {
        case "Dialogs":
            const imgMenu = new Image();
            imgMenu.src="./images/Battle/GBFormat-BlocActions.png";
            imgMenu.onload = function() {
                context.drawImage(imgMenu, 0, 0, canvas.width, canvas.height);
            }
            break;
        case "Menu":
            const imgDialogs = new Image();
            imgDialogs.src="./images/Battle/GBFormat-BlocBleu.png";
            imgDialogs.onload = function() {
                context.drawImage(imgDialogs, 0, 0, canvas.width, canvas.height);
            }
            break;
    }

    document.body.appendChild(canvas);
});
