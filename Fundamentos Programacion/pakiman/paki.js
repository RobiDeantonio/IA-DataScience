var img = [];
img['cauchin'] = 'vaca.webp';
img['pokacho'] = 'pollo.webp';
img['tocinauro'] = 'cerdo.webp';


var cauchin = new Pakiman('cauchin',100,30);
var pocacho = new Pakiman('pokacho',80,50);
var tocinauro = new Pakiman('tocinauro',120,40);

var coleccion = [];

coleccion.push(pocacho);
coleccion.push(cauchin);
coleccion.push(tocinauro);

for(var p of coleccion){
    p.mostrar();
}