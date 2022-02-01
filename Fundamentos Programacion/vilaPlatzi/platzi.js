var vp = document.getElementById('villaPlatzi');
var papel = vp.getContext('2d');

var fondo = {
    url: 'tile.webp',
    cargaOk: false
};
var vaca = {
    url: 'vaca.webp',
    cargaOk: false
};
var cerdo = {
    url: 'cerdo.webp',
    cargaOk: false
};

var teclas = {
    UP: 38,
    DOWN: 40,
    LEFT: 37,
    RIGHT:39
 };
var xCerdo = 210, yCerdo = 210;

fondo.imagen = new Image();
fondo.imagen.src = fondo.url;
fondo.imagen.addEventListener('load', cargarFondo);

vaca.objeto = new Image();
vaca.objeto.src = vaca.url;
vaca.objeto.addEventListener('load', cargarVaca);

cerdo.objeto = new Image();
cerdo.objeto.src = cerdo.url;
cerdo.objeto.addEventListener('load', cargarCerdo);

document.addEventListener('keyup', moverCerdo);

function cargarFondo(){
    fondo.cargaOk = true;
    dibujar();
}
function cargarVaca(){
    vaca.cargaOk = true;
    dibujar();
}
function cargarCerdo(){
    cerdo.cargaOk = true;
    dibujar();
}

function moverCerdo(evento){
    var mov = 10;
    console.log(evento) 

    if(evento.keyCode == teclas.UP){
        yCerdo = yCerdo-mov;
    }
    else if(evento.keyCode == teclas.DOWN){
        yCerdo = yCerdo+mov;
    }
    else if(evento.keyCode == teclas.LEFT){
        xCerdo = xCerdo-mov;
    }
    else if(evento.keyCode == teclas.RIGHT){
        xCerdo = xCerdo+mov;
    }
    dibujar();


}

function dibujar(){
    if(fondo.cargaOk){
        papel.drawImage(fondo.imagen, 0,0);
    } 

    if(vaca.cargaOk){
        var cant = aleatorio(5,15);
        for(var v=0; v<cant; v++){
            var x = aleatorio(0,420);
            var y = aleatorio(0,420);
            papel.drawImage(vaca.objeto, x,y);
        }
    }

    if(cerdo.cargaOk){
        papel.drawImage(cerdo.objeto, xCerdo,yCerdo);
     
    }
        
}


document.write('<br> <br>')
var z;
for(var i=0; i<10; i++){
    z = aleatorio(10,20);
    document.write(z + ', ');
}

function aleatorio(min,max){
    var resultado;
    resultado = Math.floor(Math.random()*(max-min+1))+ min;
    return resultado;

}
