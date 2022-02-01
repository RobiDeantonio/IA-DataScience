class Pakiman{
    constructor(nombre, vida, ataque){
        this.imagen = new Image();
        this.nombre = nombre;
        this.vida = vida;
        this.ataque = ataque; 

        this.imagen.src = img[this.nombre];
    }
    hablar(){
        alert(this.nombre);
    }
    mostrar(){
        document.body.appendChild(this.imagen);
        document.write('<p>');
        document.write('<strong>' + this.nombre + '</strong> <br />');
        document.write('Vida: ' + this.vida + '<br />');
        document.write('Ataque: ' + this.ataque + '<hr />');

        document.write('</p>');
    }
} 