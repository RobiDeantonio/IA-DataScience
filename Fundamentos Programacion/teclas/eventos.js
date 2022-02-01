var teclas = {
    UP: 38,
    DOWN: 40,
    LEFT: 37,
    RIGHT:39
 };
var x = 150, y = 150;

document.addEventListener('keyup', dibujarTeclado);
document.addEventListener('mousedown', dibujarMouse);

var c = document.getElementById('area_dibujo')
var papel = c.getContext('2d');

dibLinea('red',149,149,151,151,papel);

function dibLinea(color, xinicial, yinicial, xfinal, yfinal, lienzo){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 3;
    lienzo.moveTo(xinicial,yinicial);
    lienzo.lineTo(xfinal,yfinal)
    lienzo.stroke();
    lienzo.closePath();
}

function dibujarTeclado(evento){
    var colorcito = 'blue'
    var mov = 10;
    if(evento.keyCode == teclas.UP){
        dibLinea(colorcito,x,y,x,y-mov,papel);
        y= y-mov;
    }
    else if(evento.keyCode == teclas.DOWN){
        dibLinea(colorcito,x,y,x,y+mov,papel);
        y= y+mov;
    }
    else if(evento.keyCode == teclas.LEFT){
        dibLinea(colorcito,x,y,x-mov,y,papel);
        x= x-mov;
    }
    else if(evento.keyCode == teclas.RIGHT){
        dibLinea(colorcito,x,y,x+mov,y,papel);
        x= x+mov;
    }
}
    


function dibujarMouse(evento){

    var colorcito = 'blue'
    var xReal = evento.layerX;
    var yReal = evento.layerY;
    console.log(evento)

    dibLinea(colorcito,x,y,xReal,yReal,papel);
    x = xReal;
    y = yReal;
}




