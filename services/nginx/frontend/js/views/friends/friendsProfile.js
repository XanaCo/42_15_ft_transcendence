// import "../../components/friends/friendsProfileForm.js";
import { FriendsProfile } from "../../components/friends/friendsProfileForm.js";
import Icookies from "../../components/cookie/cookie.js"


export default async function friendsProfile(username) {
	const logdiv = document.createElement('div');
	if (Icookies.getCookie('token')) {
		logdiv.appendChild(await new FriendsProfile(username).initFriendsInfo());
		document.body.appendChild(logdiv);
	} else {
		alert("You need to be logged in to see your friends");
        window.location.href = '/home';
	}
	return logdiv;
}