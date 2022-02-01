var jf = require('johnny-five')
var circuito = new jf.Board()
var led, motor, celda;
var turno = 0

circuito.on('ready', prender)

function prender(){
    var config = {pin:'A0', freq: 50}
    celda = new jf.Sensor(config)

    led = new jf.Led(13)
    led.on()

    motor = new jf.Servo(9)
    motor.to(0)


    Ondear()
}

function Ondear(){
    console.log('luz: ' + celda.value)

    luz = celda.value
    if(luz > 800){
        if( turno){
            turno = 0
            mortor.to(70)
        }
        else{
            turno = 1
            motor.to(110)
        }
    }
    else{
        motor.to(150)
    }
    setTimeout(Ondear,1000)


}