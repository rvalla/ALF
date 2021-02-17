//Así se declara una clase en javascript
class ball {

  constructor(x, y) { //El constructor corre cuando creás una instancia del objeto
    this.x = x; //La posición en x de esta pelota
		this.y = y; //La posición en y de esta pelota
		this.c = this.getColor(); //Creamos el color de esta pelota
		this.s = this.getSpeed(); //Decidimos el vector velocidad de esta pelota
    this.d = this.getDiameter(); //Decidimos el diámetro de esta pelota
  }

  display() { //La función que dibuja la pelota
		fill(this.c); //Carga su color
    ellipse(this.x, this.y, this.d, this.d); //Y dibuja un círculo con posición (x,y) de diámetro d
  }

  update() { //La función que mueve la pelota
		this.x += this.s.x; //En cada cuadro sumamos el vector velocidad a la posición
		this.y += this.s.y;
  }

  getDiameter() { //La función que decide el diámetro
		return random(25) + 25;
  }

  getColor() { //La función que decide el color
		let c = [];
		c[0] = random(255); //Creamos 3 valores con algo de trampa para que no sea aburrido el color
		c[1] = 120 + random(120);
		c[2] = random(25);
		return color(this.chooseFromArray(c), this.chooseFromArray(c), this.chooseFromArray(c));
  }

  getSpeed() { //La función que decide la velocidad
    return createVector(random(4) - 2, random(4) - 2);
  }

	chooseFromArray(array) { //Una función para elegir al azar una posición de un arreglo
		return random(array);
	}

}
