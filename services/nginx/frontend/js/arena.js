// Création d'une nouvelle instance de WebSocket en spécifiant l'URL de votre serveur Django
const socket = new WebSocket('ws://localhost:8000/challenger/');

// Événement déclenché lorsqu'une connexion WebSocket est établie
socket.onopen = function(event) {
    console.log('WebSocket Connected');
};

// Événement déclenché lorsqu'un message est reçu du serveur
socket.onmessage = function(event) {
    console.log('Message from server:', event.data);
    // Traitez le message reçu du serveur selon vos besoins
};

// Fonction pour envoyer un message au serveur
function sendMessage(message) {
    socket.send(JSON.stringify({"message": message}));
}

function displayArena() {
	
}
