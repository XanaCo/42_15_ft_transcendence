// Initiate the router
// Import the views

import home from "./views/home.js";
import about from "./views/about.js";
import contact from "./views/contact.js";
import gameService from "./views/gameService.js";
import userService from "./views/user/userService.js";
import register from "./views/user/register.js";
import login from "./views/user/login.js";
import play from "./views/play.js";

// Define the routes
const routes = {
    '/': {
        title: "Home",
        render: home
    },
    '/about': {
        title: "About",
        render: about
    },
    '/contact': {
        title: "Contact",
        render: contact
    },
    '/userService': {
        title: "User Service",
        render: userService
    },
    '/gameService': {
        title: "Game Service",
        render: gameService
    },
    '/register': {
        title: "Register",
        render: register
    },
    '/login': {
        title: "Log In",
        render: login
    },
    '/play' : {
        title: "Play",
        render: play
    }
};

// Define the router function that will render the view based on the route path name and update the browser history state
function router() {
    let view = routes[location.pathname];
    // define the header title
    const pageTitle = "Transcendence";
    if (view) {
        document.title = pageTitle + " | " + view.title;
        app.innerHTML = view.render();
    } else {
        history.replaceState("", "", "/");
        router()
    }
};

// Handle navigation
window.addEventListener("click", (e) => {
    if (e.target.matches("[data-link]")) {
        e.preventDefault();
        history.pushState("", "", e.target.href);
        router();
    }
});

// Update router
window.addEventListener("popstate", router);
window.addEventListener("DOMContentLoaded", router);

