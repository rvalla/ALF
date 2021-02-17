//La clase psyball hereda la clase ball (tiene casi todas las funciones de ball)
class psyball extends ball {

  constructor(x, y) {
		super(x,y); //Así se llama al constructor de ball
  }

  display() { //El única función distinta entre ball y psyball
		fill(this.getColor()) //Elegimos el color en cada cuadro
    ellipse(this.x, this.y, this.d, this.d)
  }

}
