import { constants } from "./config.js"

export function populatePaddle(color, posX, posY) {

  var paddleMaterial = new THREE.MeshLambertMaterial({ color: color });

  var paddle = new THREE.Mesh(new THREE.BoxGeometry(constants.paddleWidth, constants.paddleHeight, constants.paddleDepth, constants.paddleQuality, constants.paddleQuality, constants.paddleQuality), paddleMaterial);

  paddle.position.x = posX;
  paddle.position.y = posY;
  paddle.position.z = constants.paddleDepth;
  paddle.receiveShadow = true;
  paddle.castShadow = true;

  return paddle;
}

export function populateBall(color, posX, posY) {

  var radius = 5, segments = 6, rings = 6;

  var ballMaterial = new THREE.MeshLambertMaterial({ color: color });

  var ball = new THREE.Mesh(new THREE.SphereGeometry(radius, segments, rings), ballMaterial);

  ball.position.x = posX;
  ball.position.y = posY;
  ball.position.z = radius;
  ball.receiveShadow = true;
  ball.castShadow = true;

  return ball;
}

export function populatePlane(color, posX, posY) {

  var planeMaterial = new THREE.MeshLambertMaterial({ color: color });

  var plane = new THREE.Mesh(new THREE.PlaneGeometry(constants.planeWidth * 0.95, constants.planeHeight, constants.planeQuality, constants.planeQuality), planeMaterial);
  plane.position.x = posX;
  plane.position.y = posY;
  plane.receiveShadow = true;

  return plane;
}

export function populateTable(color, posX, posY, posZ) {

  var tableMaterial = new THREE.MeshLambertMaterial({ color: color });

  var table = new THREE.Mesh(new THREE.BoxGeometry(constants.tableWidth, constants.tableHeight, constants.tableQuality, constants.tableQuality, 1), tableMaterial);
  table.position.x = posX;
  table.position.y = posY;
  table.position.z = posZ;
  table.receiveShadow = true;

  return table;
}

export function populateFloor() {

  const groundTexLoader = new THREE.TextureLoader();

  var path = '../../../images/Floor/FL_RedCarpet.png';

  //Rajouter le switch ici quant a la map

  var groundMaterial = new THREE.MeshLambertMaterial({
    map: groundTexLoader.load(path,
      function(texture) {
        //texture.wrapS = THREE.ClampToEdgeWrapping;
        //texture.wrapT = THREE.ClampToEdgeWrapping;
        //texture.minFilter = THREE.LinearFilter;
        //texture.magFilter = THREE.LinearFilter;
        const repeatX = 2200 / 512;
        const repeatY = 2200 / 512;
        texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
        texture.repeat.set(repeatX, repeatY);
        texture.minFilter = THREE.LinearFilter;
        texture.magFilter = THREE.LinearFilter;
      })
  });

  var ground = new THREE.Mesh(new THREE.BoxGeometry(constants.groundWidth, constants.groundHeight, constants.groundQuality, 1, 1, 1), groundMaterial);
  ground.position.z = -132;
  ground.receiveShadow = true;

  return ground;
}

export function populateWall(player_id) {

  const wallTexLoader = new THREE.TextureLoader();

  var path = '../../../images/Walls/Wall-Back-Figures.png'

  //Rajouter le switch ici quant a la map

  var wallMaterial = new THREE.MeshLambertMaterial({
    map: wallTexLoader.load(path,
      function(texture) {
        texture.wrapS = THREE.ClampToEdgeWrapping;
        texture.wrapT = THREE.ClampToEdgeWrapping;
        texture.minFilter = THREE.LinearFilter;
        texture.magFilter = THREE.LinearFilter;
      })
  });

  var wall = new THREE.Mesh(new THREE.BoxGeometry(constants.wallWidth, constants.wallHeight, constants.wallQuality, 1, 1, 1), wallMaterial);

  if (player_id == 1) {
    wall.position.x = 500;
  }
  else {
    wall.position.x = -500;
  }
  wall.position.z = 25;
  wall.rotateY(Math.PI / 2);
  wall.rotateZ(Math.PI / 2);
  wall.receiveShadow = true;

  return wall;
}
