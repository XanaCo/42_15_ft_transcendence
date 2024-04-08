const canvas = document.querySelector("canvas");
const context = canvas.getContext('2d');

let box = 16;

let red = { x: 10 * box, y: 10 * box };

let score;

const url = 'http://localhost:8080/metaverse/';
// 'http://token:8080/api/token_generate/'
// Options de la requête (dans ce cas, une requête GET)
const options = {
	method: 'GET',
	headers: {
		'Content-Type': 'application/json' // En-tête facultatif
	}
};

fetch(url, options)
    .then(response => {
        // Vérification du statut de la réponse
        if (!response.ok)
            throw new Error('Erreur de réponse du serveur');
        // Analyse de la réponse JSON
        return response.json();
    })
    .then(data => {
        // Manipulation des données reçues
        score = 1;
    })
    .catch(error => {
        console.error('Erreur lors de la requête:', error);
        // Gérer l'erreur ici
        score = 0; // Ou toute autre action appropriée
    });

let d = "DOWN";

let playerDown = new Image();
playerDown.src = 'Red_1.png';

let playerUp = new Image();
playerUp.src = 'Red_2.png';

let playerLeft = new Image();
playerLeft.src = 'Red_3.png';

let playerRight = new Image();
playerRight.src = 'Red_4.png';

document.addEventListener("keydown", direction);

function direction(event) {
    let key = event.keyCode;
    if (key == 37)
	{
		red.x -= box;
        d = "LEFT";
	}
	else if (key == 38)
	{
		red.y -= box;
        d = "UP";
	}
    else if (key == 39)
	{
		red.x += box;
        d = "RIGHT";
	}
    else if (key == 40)
	{
		red.y += box;
        d = "DOWN";
	}
}

function draw() {
    context.clearRect(0, 0, 360, 360);

	if (d == "LEFT")
    	context.drawImage(playerLeft, red.x, red.y - 4, box, box + 4);
	if (d == "UP")
    	context.drawImage(playerUp, red.x, red.y - 4, box, box + 4);
	if (d == "RIGHT")
    	context.drawImage(playerRight, red.x, red.y - 4, box, box + 4);
	if (d == "DOWN")
    	context.drawImage(playerDown, red.x, red.y - 4, box, box + 4);

    if (red.x < 0 || red.y < 0 || red.x > 24 * box || red.y > 24 * box)
	{
        clearInterval(game);
    }


    context.fillStyle = "red";
    context.font = "30px Arial";
    context.fillText(score, 2 * box, 1.6 * box);
}

let game = setInterval(draw, 100);
