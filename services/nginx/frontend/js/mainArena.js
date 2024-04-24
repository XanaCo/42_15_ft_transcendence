
function getCanvas() {
	var canvas = document.createElement('canvas');

	canvas.width = 700;
	canvas.height = 500;

	var ctx = canvas.getContext('2d');

	ctx.fillStyle = 'rgb(39, 89, 80)';
	ctx.fillRect(0, 0, canvas.width, canvas.height);

	var allyLifeX = 400;
	var allyLifeY = 280;
	var opponentLifeX = 70;
	var opponentLifeY = 100;

	
	var imageOpponent = new Image();
	imageOpponent.src = './images/jess.png';
	// imageOpponent.onload = function() {
	// }
	var imageAlly = new Image();
	imageAlly.src = './images/dauphinroi.png';
	// imageAlly.onload = function() {
	// }
	
	var ground = new Image();
	ground.src = './images/ground.png';
	ground.onload = function() {
		ctx.drawImage(ground, 400, 160)
		ctx.drawImage(ground, 20, 370)
		ctx.drawImage(imageAlly, 50, 208)
		ctx.drawImage(imageOpponent, 420, 50)
		ctx.fillStyle = 'black';
		ctx.fillRect(opponentLifeX - 10 - 1, opponentLifeY - 30 - 1, 250 + 2, 70 + 2);
		ctx.fillRect(allyLifeX - 10 - 1, allyLifeY - 30 - 1, 250 + 2, 70 + 2);
	
		ctx.fillStyle = 'grey';
		ctx.fillRect(opponentLifeX - 10, opponentLifeY - 30, 250, 70);
		ctx.fillRect(allyLifeX - 10, allyLifeY - 30, 250, 70);
	
		ctx.fillStyle = 'black';
		ctx.fillRect(opponentLifeX - 1, opponentLifeY - 1, 200 + 2, 15 + 2);
		ctx.fillRect(allyLifeX - 1, allyLifeY - 1, 200 + 2, 15 + 2);
	
		ctx.fillStyle = 'green';
		ctx.fillRect(opponentLifeX, opponentLifeY, 120, 15);
		ctx.fillRect(allyLifeX, allyLifeY, 200, 15);
	
		ctx.font = "20px Arial";
		ctx.fillStyle = "black";
		ctx.fillText("Dauphinroi", allyLifeX , allyLifeY - 10);
		ctx.fillText("La justice", opponentLifeX , opponentLifeY - 10);
		
		ctx.fillStyle = 'black';
		ctx.fillRect(0, 400, canvas.width, 100);
		ctx.fillStyle = 'white';
		ctx.fillRect(1, 401, canvas.width - 2, 100 - 2);

		// ctx.font = "20px Arial";
		ctx.fillStyle = 'black';
		ctx.fillText("Dauphinroi tabasse La justice !", opponentLifeX , 450);
	}

	return canvas;
}

document.body.appendChild(getCanvas());