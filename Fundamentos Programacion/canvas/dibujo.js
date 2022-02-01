var d = document.getElementById('dibujito');
var texto = document.getElementById('texto_lineas');
var button = document.getElementById('button');
button.addEventListener('click', dibujoXClick);

var lienzo = d.getContext('2d');
var width = d.width;    

function dibLinea(color, xinicial, yinicial, xfinal, yfinal){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(xinicial,yinicial);
    lienzo.lineTo(xfinal,yfinal)
    lienzo.stroke();
    lienzo.closePath();
}



function dibujoXClick(){
    var xxx = parseInt(texto.value);
    var espacio = width/xxx;
    var l = 0;
    var yi, xf;

    while(l<xxx){
        yi = l*espacio;
        xf = l*espacio;
        dibLinea('pink',0,yi,xf,300);
        l = l+1;
    }
    for(l = 0; l<xxx; l++){   
        yi = l*espacio;
        xf = l*espacio;
        dibLinea('pink',yi,0,300,xf);
    }
}