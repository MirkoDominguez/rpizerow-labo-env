
from gpiozero import LED, Button
from signal import pause

#importo el led,boton y la señal de pausa

led = LED(19)
button = Button(3)
 
#indico el pin del led y del boton

button.when_pressed = led.on
button.when_released = led.off

#defini que cuando el boton se pulse el led se enciende y cuando el led se suelte el led se apague

pause()
