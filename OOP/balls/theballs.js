let balls; //En javascript así se declaran las variables globales
let limit, count;
let cx, cy;
let alphastep;

function setup() { //setup() es una función de la librería p5.js para configurar la animación
  createCanvas(windowWidth, windowHeight); //Acá creamos las ventana donde todo pasa
	thecanvas = document.getElementsByTagName("canvas")[0]; //Tenemos que gestionar el click (llama processEV())
	thecanvas.addEventListener("mousedown", processEv, false);
	thecanvas.addEventListener("touchend", processEv, false);
	noStroke(); //Para dibujar sin bordes
  frameRate(50); //La velocidad de la animación
	background(0); //El color de fondo
	balls = []; //Vamos a guardar un arreglo objetos de nuestra clase "ball"
	limit = 20; //Limitamos la cantidad de pelotas posibles
	count = 0; //Contamos cuántos click dio el usuario
	alphastep = 50; //Decidimos cuánto tapa un cuadro el cuadro anterior (0-255)
	cx = width / 5  * 2 + random(width / 5); //Elegimos un punto de origen en x
	cy = height / 5 * 2 + random(height / 5); //Elegimos un punto de origen en x
}

function draw() { //draw() es una función de p5.js que corre una vez para cada cuadro de la animación
	background(0, alphastep); //Tapamos lo anterior
	for (let i = 0; i < balls.length; i++) { //Recorremos el arreglo de balls
		balls[i].update(); //Antes de dibujar ball la actualizamos
		balls[i].display(); //Ahora sí se dibuja
	}
}

function processEv() { //Gestionamos los clicks
	type = random([0, 1]) //Tiramos una moneda
	if (type === 0) { //Si sale 0 creamos una ball
		if (count < limit) { //Limitamos la cantidad de objetos
			balls.push(new ball(cx, cy)) //Acá creamos un nuevo objeto ball en la memoria (igual línea 37)
			count += 1;
		} else { //Si superamos el límite creamos la nueva ball borrando una de las viejas
			balls[count%limit] = new ball(cx, cy);
			count += 1;
		}
	} else { //Si sale 1 creamos una psyball
		if (count < limit) {
			balls.push(new psyball(cx, cy)) //Acá creamos un nuevo objeto psyball en la memoria (igual línea 45)
			count += 1;
		} else {
			balls[count%limit] = new psyball(cx, cy);
			count += 1;
		}
	}
	event.preventDefault(); //Estas líneas resuelven problemas de compatibilidad entre navegadores
  return false;
}
