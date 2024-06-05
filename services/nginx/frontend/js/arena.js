
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



class Arena {
    constructor()
    {
        this.canvas = document.createElement("canvas");
        this.canvas.width = 500;
        this.canvas.height = 500;
        this.context = this.canvas.getContext("2d");
        this.gameState = "Menu";
        this.position = 0;
        this.handleKeyDown = this.handleKeyDown.bind(this); // Bind the method to the instance
        this.att1 = "Charge";
        this.att2 = "Reflet";
        this.att3 = "Morsure";
        this.att4 = "Fouet Lianes";
        
        this.lastAttackAlly = "Charge";
        this.lastEfficiencyAlly = 1; // 0 = not very effective, 1 = normal, 2 = super effective
        this.lastAttackOpponent = "Morsure";
        this.lastEfficiencyOpponent = 1; // 0 = not very effective, 1 = normal, 2 = super effective
        this.fastestPokemon = 0; // 0 = ally, 1 = opponent
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
            case "Menu":
                const imgMenu = new Image();
                imgMenu.src="./images/Battle/GBFormat-BlocActions.png";
                imgMenu.onload = () =>
                {
                    this.context.drawImage(imgMenu, 0, 0, this.canvas.width, this.canvas.height);
                }
                
                const imgCursor = new Image();
                imgCursor.src="./images/Battle/Items/RedArrow.png";
                imgCursor.onload = () =>
                {
                    this.context.drawImage(imgCursor, this.canvas.width - 238 + (this.position & 1) * 115, this.canvas.height - 50 - (this.position < 2) * 40, 20, 20);
                }
                
                break;
            case "Dialogs":
                const imgDialogs = new Image();
                imgDialogs.src="./images/Battle/GBFormat-BlocBleu.png";
                imgDialogs.onload = () =>
                {
                    this.context.drawImage(imgDialogs, 0, 0, this.canvas.width, this.canvas.height);
                }
                const imgCursor3 = new Image();
                imgCursor3.src="./images/Battle/Items/RedArrow.png";
                imgCursor3.onload = () =>
                {
                    this.context.drawImage(imgCursor3, this.canvas.width * 0.9, this.canvas.height * 0.85, 20, 20);
                }
                break;
                
            case "Fight":
                const imgFight = new Image();
                imgFight.src="./images/Battle/GBFormat-BlocBlanc.png";
                imgFight.onload = () =>
                {
                    this.context.drawImage(imgFight, 0, 0, this.canvas.width, this.canvas.height);
                }
                const imgCursor2 = new Image();
                imgCursor2.src="./images/Battle/Items/RedArrow.png";
                imgCursor2.onload = () =>
                {
                    this.context.drawImage(imgCursor2, this.canvas.width * 0.05 + (this.position & 1) * 125, this.canvas.height - 50 - (this.position < 2) * 40, 20, 20);
                    this.context.font = "bold 18px Arial";
                    this.context.fillStyle = "black";
                    this.context.fillText(this.att1, this.canvas.width * 0.1, this.canvas.height * 0.85);
                    this.context.fillText(this.att2, this.canvas.width * 0.35, this.canvas.height * 0.85);
                    this.context.fillText(this.att3, this.canvas.width * 0.1, this.canvas.height * 0.93);
                    this.context.fillText(this.att4, this.canvas.width * 0.35, this.canvas.height * 0.93);
                }
        }
    }
        
//////////////////////////////////////////////////////////////////////
////    HANDLE KEYBOARD
//////////////////////////////////////////////////////////////////////

        handleKeyDown(event)
        {
            document.onkeydown = (event) => {
            if (37 <= event.keyCode && event.keyCode <= 40)
                event.preventDefault();
        }
        
        switch(event.keyCode)
        {
            case 37: // Left arrow
                if (this.position == 1 || this.position == 3)
                    this.position--;
                // console.log(this.position);
                break;
            case 38: // Up arrow
                if (this.position == 2 || this.position == 3)
                    this.position -= 2;
                // console.log(this.position);
                break;
            case 39: // Right arrow
                if (this.position == 0 || this.position == 2)
                    this.position++;
                // console.log(this.position);
                break;
            case 40: // Down arrow
                if (this.position == 0 || this.position == 1)
                    this.position += 2;
                // console.log(this.position);
                break;
            case 32: // Space
                if (this.gameState == "Menu")
                    this.gameState = "Dialogs";
                else
                    this.gameState = "Menu";
                break;
            case 13: // Enter
                if (this.gameState == "Menu" && this.position == 0)
                    this.gameState = "Fight";
                else if (this.gameState == "Fight")
                    socket.send(JSON.stringify({
                        type: "message",
                        content: "1"
                    }));
                break;
            
        }
    }
}

const arena = new Arena();

arena.getDivArena();
setInterval(() => {
    arena.drawArena();
}, 100);

