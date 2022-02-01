class Billete{
    constructor(v ,c){
        this.valor = v;
        this.cantidad = c;
    }
}


function entregarDinero(){


    var t = document.getElementById('dinero');
    dinero = parseInt(t.value);
    for(var bi of caja){
       if(dinero > 0){
           div = Math.floor(dinero/bi.valor);
           if(div > bi.cantidad ){
               papeles = bi.cantidad
           }
           else{
               papeles = div;
           }    
           entregado.push(new Billete(bi.valor,papeles));
           dinero = dinero - bi.valor*papeles;


       }
    }

    if(dinero > 0){
        document.getElementById('resultado').innerHTML = '';
        resultado.innerHTML = 'Soy un cajero pobre no tengo dinero .(';
    }
    else{
        resultado.innerHTML = '<hr />';
        for( var e of entregado){
            if(e.cantidad > 0 ){
                if(resetScreen == 0){
                    
                    resetScreen = 1
                }
                resultado.innerHTML += e.cantidad + ' billetes de $' + e.valor + '<br />';
            }
            

        }
        
    }
    resetScreen = 0;

    console.log(entregado);
}

var caja = [];
var entregado = [];

caja.push(new Billete(100,5));
caja.push(new Billete(50,5));
caja.push(new Billete(20,10));
caja.push(new Billete(10,10));
caja.push(new Billete(5,10));

var dinero;
var div = 0;
var papeles = 0;
var resetScreen = 0;

var resultado = document.getElementById('resultado');
var b = document.getElementById('extraer');
b.addEventListener('click', entregarDinero);