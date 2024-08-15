from gpiozero import LED, Buzzer
import time
	
# Asigno pines para cada componente
rojo = LED(19)
verde = LED(13)
azul = LED(26)
buzzer = Buzzer(22)


# empiezo un bucle
while True:
#Pido que se ingrese un comando en la consola enseñando el mensaje como  "prompt"
	comando = input("prompt: ").split()

#Confirmo que haya 2 partes en el comando (acción y componente)
	if len(comando) == 2:
		componente, accion = comando
#Prendo o apago el buzzer segun la opcion que se introduzca
		if componente == "buzzer":
			if accion == "on":
				buzzer.on()
			elif accion == "off":
				buzzer.off()

#Enciendo el rgb con el color indicado en la opción que elegí
		elif componente == "led":
			if accion == "rojo":
				rojo.on()
				azul.off()
				verde.off()
			elif accion == "verde":
				rojo.off()
				verde.on()
				azul.off()
			elif accion == "azul":
				rojo.off()
				verde.off()
				azul.on()
			elif accion == "apagar":
				rojo.off()
				verde.off()
				azul.off()

		else:
			print("Comando incorrecto")
