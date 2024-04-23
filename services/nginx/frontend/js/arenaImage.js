// Envoi de la requête Fetch
fetch('arena/image/')
    .then(response => {
    // Vérifier si la réponse est OK (200)
    if (!response.ok) {
        throw new Error('La requête a échoué avec un code ' + response.status);
    }

    // Renvoyer le corps de la réponse sous forme de texte
    return response.text();
    })
    .then(data => {
    // Afficher le contenu de la réponse dans les logs
    console.log('Réponse de la requête fetch :', data);
    })
    .catch(error => {
    // Attraper les erreurs et les afficher dans les logs
    console.error('Erreur lors de la requête fetch :', error);
    });