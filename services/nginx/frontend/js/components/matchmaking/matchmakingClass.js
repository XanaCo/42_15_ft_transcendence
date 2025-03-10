import Icookies from "../cookie/cookie.js"
import Iuser from "../user/userInfo.js";

class MatchmakingButtons {

	constructor() {
		this.maindiv = document.createElement('div');
		this.maindiv.classList.add('main-matchmaking-div');
		this.matchsocket = null;
		this.status = null;
		this.timer = 0;
	}

	matchmakingsocketaction() {
		this.matchsocket.onmessage = async (event) => {
			const data = JSON.parse(event.data);
			this.status = data.status;
			this.timer = data.waitingTime;
			this.game = data.game;
			if (this.status === 'game') {
				this.removeWaitingPage();
				if (this.game === 'pong_multiplayer'){
					window.location.href = "/gameService"
				} else if (this.game === 'pkm_multiplayer'){
					window.location.href = "/home"
				}
				return;
			}
				
			this.updateData();
			await this.checkstatus(data);
			const msg = {
				"action": "queue_status",
				"game": this.game,
				"id": await Iuser.getID(),
			}
			this.matchsocket.send(JSON.stringify(msg));
		}
	}

	timerCalculation() {
		try {
			let time = new Date(this.timer);
			if (isNaN(time.getTime()))
				return 0;
			let now = new Date();
			let elapsedTimeMillis = now - time;
			return (Math.floor(elapsedTimeMillis / 1000));
		}
		catch (error) {
			return 0;
		}
	}

	async removeUser() {
		const id = await Iuser.getID();
		const body = {
			"userID": id
		}
		const response = await fetch('https://localhost:4430/api/matchmaking/', {
			method: 'DELETE',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': Icookies.getCookie('token'),
				'X-CSRFToken': Icookies.getCookie('csrftoken')
			},
			credentials: 'include',
			body: JSON.stringify(body)
		});
	}

	waitingPage() {
		const waitingpage = document.createElement('div');
		waitingpage.id = 'waiting-page';
		waitingpage.classList.add('waiting-page', 'center', 'p-3', 'position-absolute', 'top-50', 'start-50', 'translate-middle', 'z-index-1');

		const waitinggif = document.createElement('div');

		if (this.game === 'pong_multiplayer'){
			waitinggif.classList.add('embed-responsive', 'embed-responsive-16by9');
			const img = new Image();
			img.src = "../../../images/Site/AloneAgain.gif";
			img.classList.add('embed-responsive-item');
			waitinggif.appendChild(img);
		} else if (this.game === 'pkm_multiplayer'){
			waitinggif.style.width = "100%";
			waitinggif.style.height = "0";
			waitinggif.style.paddingBottom = "71%";
			waitinggif.style.position = "relative";
			
			const img = new Image();
			img.src = "../../../images/Site/AloneAgain.gif";
			img.style.width = "100%";
			img.style.height = "100%";
			img.style.position = "absolute";
			img.frameBorder = "0";
			img.classList.add('giphy-embed');
			img.allowFullscreen = true;
			
			waitinggif.appendChild(img);
		}

		waitingpage.appendChild(waitinggif);

		const timer = document.createElement('p');
		timer.id = 'timer';
		timer.innerText = this.timerCalculation();
		timer.classList.add('timer', 'text-center', 'text-black', 'fs-3');

		const cancelbutton = document.createElement('button');
		cancelbutton.classList.add('cancel-button', 'btn', 'btn-danger', 'text-white', 'fs-3');
		cancelbutton.innerText = 'Cancel';
		cancelbutton.onclick = async () => {
		await this.removeUser();
		this.removeWaitingPage();
		window.location.href = '/home';
	}
		waitingpage.appendChild(timer);
		waitingpage.appendChild(cancelbutton);

		return waitingpage;
	}

	removeWaitingPage() {
		const waitingpage = document.querySelector('#waiting-page');
		waitingpage.remove();
	}

	updateData() {
		const timer = document.querySelector('#timer');

		if (timer) {
			const time = this.timerCalculation();
			if (time > 60) {
				timer.innerText = Math.floor(time / 60) + "m " + time % 60 + "s";
			}
			else {
				timer.innerText = time;
			}
		}
	}

	async createParty_pong(data) {
		const users = await Iuser.getAllUsers();
		let username1 = users.users.find(user => user.user_id === parseInt(data.player1)).username;
		let username2 = users.users.find(user => user.user_id === parseInt(data.player2)).username;
		const party = {
			"player1": {
				id : data.player1,
				username : username1
			},
			"player2": {
				id : data.player2,
				username : username2
			},
		}
		const response = await fetch('https://localhost:4430/api/pong/match/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': Icookies.getCookie('token'),
				'X-CSRFToken': Icookies.getCookie('csrftoken')
			},
			credentials: 'include',
			body: JSON.stringify(party)
		});
	}

	async changeStatus() {
		const id = await Iuser.getID();
		const body = {
			"userID": id,
			"status": "game"
		}
		const response = await fetch('https://localhost:4430/api/matchmaking/', {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': Icookies.getCookie('token'),
				'X-CSRFToken': Icookies.getCookie('csrftoken')
			},
			credentials: 'include',
			body: JSON.stringify(body)
		});
	}

	async checkstatus(data) {
		if (this.status === 'found') {
			this.removeWaitingPage();
			await this.changeStatus();
			if (this.game === 'pong_multiplayer')
				await this.createParty_pong(data);
				window.location.href = "/gameService"
			if (this.game === 'pong_multiplayer')
				await this.createParty_pong(data);
				window.location.href = "/pokecombat"
		}
	}

	async mainMatchmakingDiv() {
		this.matchsocket = new WebSocket("wss://localhost:4430/api/wsqueue/")
		this.matchmakingsocketaction();

		const msg = {
			"action": "queue_add",
			"game": this.game,
			"id": await Iuser.getID(),
		}

		const waitForOpenConnection = new Promise(resolve => {
			this.matchsocket.addEventListener('open', resolve);
		});
		await waitForOpenConnection;

		const waitingPage = this.waitingPage();
		if (waitingPage instanceof HTMLElement) {
			this.maindiv.appendChild(waitingPage);
		} else {
			console.error("waitingPage did not return a valid DOM node.");
		}
		this.matchsocket.send(JSON.stringify(msg));

		document.body.appendChild(this.maindiv);
		return this.maindiv;
	}
}

class Matchmaking extends MatchmakingButtons {
	constructor(game) {
		super();
		this.game = game;
	}
}

const pongRemoteMatchmaking = new Matchmaking('pong_multiplayer');
const pongTournamentMatchmaking = new Matchmaking('pong_tournament');
const pkmRemoteMatchmaking = new Matchmaking('pkm_multiplayer');
const pkmTournamentMatchmaking = new Matchmaking('pkm_tournament');

export { pongRemoteMatchmaking, pongTournamentMatchmaking, pkmRemoteMatchmaking, pkmTournamentMatchmaking };
