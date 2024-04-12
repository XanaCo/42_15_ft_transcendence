
const io = require("socket.io")(3000, {
    cors: {
        origin: ["http://localhost:8080"],
    },
})

io.on("connection", socket => {
    console.log(socket.id)
})

// Handle arrows
document.addEventListener('keydown', function(event) {
    // Vous pouvez accéder au code de la touche via event.keyCode ou event.key
    var keyCode = event.keyCode;
    var key = event.key;

    console.log('Touche enfoncée - Code : ' + keyCode + ', Touche : ' + key);
    
    // Exemple : si la touche 'ArrowUp' est enfoncée
    if (key === 'ArrowUp') {
        console.log('La touche ArrowUp a été pressée.');
    } else if (key === 'ArrowDown') {
        // Faire quelque chose en cas d'appui sur la touche 'ArrowDown'
        console.log('La touche ArrowDown a été pressée.');
    }
});
