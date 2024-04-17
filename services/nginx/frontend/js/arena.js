
//////////////////////////////////////////////////////////////////////
////    SOCKETS
//////////////////////////////////////////////////////////////////////

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
    if (event.keyCode >= 37 && event.keyCode <= 40) {
        // Afficher un message dans la console avec le code de la touche
        console.log("Flèche du clavier enfoncée : " + event.keyCode);
    }
    if (event.keyCode == 13)
        console.log("Touche enter enfoncée");
}

// Ajouter un écouteur d'événements pour détecter quand une touche du clavier est enfoncée
document.addEventListener("keydown", gestionToucheEnfoncee);


//////////////////////////////////////////////////////////////////////
////    FETCH
//////////////////////////////////////////////////////////////////////

// Envoi de la requête Fetch
// fetch('https://localhost:8080/arena/testView')
//   .then(response => {
//     // Vérifier si la réponse est OK (200)
//     if (!response.ok) {
//       throw new Error('La requête a échoué avec un code ' + response.status);
//     }
//     // Renvoyer le corps de la réponse sous forme de texte
//     return response.text();
//   })
//   .then(data => {
//     // Afficher le contenu de la réponse dans les logs
//     console.log('Réponse de la requête fetch :', data);
//   })
//   .catch(error => {
//     // Attraper les erreurs et les afficher dans les logs
//     console.error('Erreur lors de la requête fetch :', error);
//   });
