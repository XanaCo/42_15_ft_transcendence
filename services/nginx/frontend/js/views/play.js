import { pongRemoteMatchmaking, pongTournamentMatchmaking, pkmRemoteMatchmaking, pkmTournamentMatchmaking } from "../components/matchmaking/matchmakingClass.js";
import { pokeMap } from "../components/pokemon/pokemap.js";
import { pokechat, pokebag } from "../components/pokemon/poketools.js";
import Icookies from "../components/cookie/cookie.js"
import { setup } from "../components/pong3d/pongServLogic.js";
import { tournamentInput } from "../components/pong3d/tournamentInput.js";


export function pong_localplay() {
  const generaldiv = document.createElement('div');
  const screens = document.createElement('div');
  screens.id = "pong-screens";
  screens.classList.add('hidden');
  const gamediv = document.createElement('div');
  gamediv.id = "pong-renderer"
  const scorediv = document.createElement('div');
  scorediv.id = "pong-score"
  if (Icookies.getCookie('token') != null) {
    setup("local", null);
  } else {
    generaldiv.classList.add('not-logged');
    alert("You need to be logged in to play in local");
    window.location.href = '/pongService';
  }
  generaldiv.appendChild(screens);
  generaldiv.appendChild(gamediv);
  generaldiv.appendChild(scorediv);
  document.body.appendChild(generaldiv);
  return generaldiv;
}

export async function pong_remoteplay() {
  const generaldiv = document.createElement('div');
  const screens = document.createElement('div');
  screens.id = "pong-screens";
  screens.classList.add('hidden');
  const gamediv = document.createElement('div');
  gamediv.id = "pong-renderer"
  const scorediv = document.createElement('div');
  scorediv.id = "pong-score"
  if (Icookies.getCookie('token') != null) {
    setup("remote", null);
  } else {
    gamediv.classList.add('not-logged');
    alert("You need to be logged in to play in remote");
    window.location.href = '/pongService';
  }
  generaldiv.appendChild(screens);
  generaldiv.appendChild(gamediv);
  generaldiv.appendChild(scorediv);
  document.body.appendChild(generaldiv);
  return generaldiv;
}

export async function pong_tournamentplay() {
  const generaldiv = document.createElement('div');
  let gamediv = document.createElement('div');
  let scorediv = document.createElement('div');
  if (Icookies.getCookie('token') != null) {
    let turgecence = new tournamentInput();
    generaldiv.appendChild(await turgecence.initTournamentInfo());
    //generaldiv.removeChild(generaldiv.lastChild);
    gamediv.id = "pong-renderer"
    scorediv.id = "pong-score"
    // gamediv.appendChild(await pongTournamentMatchmaking.mainMatchmakingDiv());
  } else {
    gamediv.classList.add('not-logged');
    alert("You need to be logged in to play in tournament");
    window.location.href = '/pongService';
  }
  generaldiv.appendChild(gamediv);
  generaldiv.appendChild(scorediv);
  document.body.appendChild(generaldiv);
  return generaldiv;
}

// export async function pong_tournamentplay() {
//   const gamediv = document.createElement('div');
//   if (Icookies.getCookie('token') != null) {
//     gamediv.appendChild(await new tournamentInput.initTournamentInfo());
//     // gamediv.appendChild(await pongTournamentMatchmaking.mainMatchmakingDiv());
//   } else {
//     gamediv.classList.add('not-logged');
//     alert("You need to be logged in to play in tournament");
//     window.location.href = '/pongService';
//   }
//   document.body.appendChild(gamediv);
//   return gamediv;
// }

export async function pkm_remoteplay() {
  const gamediv = document.createElement('div');
  if (Icookies.getCookie('token') != null) {
    gamediv.appendChild(await pkmRemoteMatchmaking.mainMatchmakingDiv());
  } else {
    gamediv.classList.add('not-logged');
    alert("You need to be logged in to play in remote");
    window.location.href = '/metaService';
  }
  document.body.appendChild(gamediv);
  return gamediv;
}

export async function pokemap_interactive() {
  const maindiv = document.createElement('div');
  maindiv.classList.add('row', 'p-4');

  if (Icookies.getCookie('token') != null) {
    const gamediv = document.createElement('div');
    gamediv.classList.add('col-8');
    gamediv.appendChild(new pokeMap().startingPokeverse());

    const toolsdiv = document.createElement('div');
    toolsdiv.classList.add('col-4');
    toolsdiv.style.display = 'flex';
    toolsdiv.style.flexDirection = 'column';
    const chatdiv = new pokechat().pokechatinit();
    chatdiv.style.display = 'flex';
    chatdiv.style.flexDirection = 'column';
    toolsdiv.appendChild(chatdiv);

    const bagdiv = new pokebag().createAllCards();
    bagdiv.style.marginTop = '15px';
    toolsdiv.appendChild(bagdiv);

    maindiv.appendChild(gamediv);
    maindiv.appendChild(toolsdiv);

  } else {
    maindiv.classList.add('not-logged');
    alert("You need to be logged in to play in the pokeverse");
    window.location.href = '/metaService';
  }
  document.body.appendChild(maindiv);
  return maindiv;
}