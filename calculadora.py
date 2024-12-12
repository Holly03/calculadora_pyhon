#--- Librerías ---
from tkinter import *


#--- Ventana ---

root=Tk()
root.title("Calculadora")
root.geometry("400x300")
root.configure(background="black")


#--- Frame ---

marco=Frame(root)
marco.pack()
marco.configure(background="black")


#--- Variables ---

operacion=""

clear=False

resultado=0


#--- Pantalla ---

digitos=StringVar()

pantalla=Entry(marco, font=('arial',20,'bold'), width=22, textvariable=digitos)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="lightgrey", fg="black", justify="right", bd=5)


#--- Acciones botonera ---

def boton(num):

	global operacion

	global clear

	if clear!=False:

		digitos.set(num)

		clear=False

	else:

		digitos.set(digitos.get() + num)


#--- Operaciones ---
	
	# SUMA

def suma(num):

	global operacion

	global resultado

	global clear

	resultado+=int(num)

	operacion="suma"

	clear=True

	digitos.set(resultado)



	# RESTA

num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global clear

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)

		digitos.set(resultado)

		resultado=digitos.get()


	contador_resta=contador_resta+1

	operacion="resta"

	clear=True



	# MULTIPLICAR

contador_multi=0

def multiplicar(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global clear

	if contador_multi==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)

		digitos.set(resultado)

		resultado=digitos.get()
		

	contador_multi=contador_multi+1

	operacion="multiplicar"

	clear=True



	# DIVIDIR 

contador_dividir=0

def dividir(num):

	global operacion

	global resultado

	global num1

	global contador_dividir

	global clear

	if contador_dividir==0:

		num1=float(num)

		resultado=num1

	else:

		if contador_dividir==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)

		digitos.set(resultado)

		resultado=digitos.get()
		

	contador_dividir=contador_dividir+1

	operacion="dividir"

	clear=True



	# RESULTADO

def igual():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_dividir

	if operacion=="suma":

		digitos.set(resultado+int(digitos.get()))

		resultado=0

	elif operacion=="resta":

		digitos.set(int(resultado)-int(digitos.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicar":

		digitos.set(int(resultado)*int(digitos.get()))

		resultado=0
		
		contador_multi=0

	elif operacion=="dividir":

		digitos.set(int(resultado)/int(digitos.get()))

		resultado=0
		
		contador_dividir=0




#--- Botonera superior ---

boton7=Button(marco, text="7", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("7"))
boton7.grid(row=2, column=1)
boton8=Button(marco, text="8", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("8"))
boton8.grid(row=2, column=2)
boton9=Button(marco, text="9", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(marco, text="/", width=11, height=3, bg="orange", font=('arial',9,'bold'), command=lambda:dividir(digitos.get()))
botonDiv.grid(row=2, column=4)


#--- Botonera media superior ---

boton4=Button(marco, text="4", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("4"))
boton4.grid(row=3, column=1)
boton5=Button(marco, text="5", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("5"))
boton5.grid(row=3, column=2)
boton6=Button(marco, text="6", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("6"))
boton6.grid(row=3, column=3)
botonMult=Button(marco, text="X", width=11, height=3, bg="orange", font=('arial',9,'bold'), command=lambda:multiplicar(digitos.get()))
botonMult.grid(row=3, column=4)


#--- Botonera media inferior ---

boton1=Button(marco, text="1", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("1"))
boton1.grid(row=4, column=1)
boton2=Button(marco, text="2", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("2"))
boton2.grid(row=4, column=2)
boton3=Button(marco, text="3", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("3"))
boton3.grid(row=4, column=3)
botonRest=Button(marco, text="-", width=11, height=3, bg="orange", font=('arial',9,'bold'), command=lambda:resta(digitos.get()))
botonRest.grid(row=4, column=4)


#--- Botonera inferior ---

boton0=Button(marco, text="0", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("0"))
boton0.grid(row=5, column=1)
botonComa=Button(marco, text=",", width=11, height=3, bg="skyblue", font=('arial',9,'bold'), command=lambda:boton("."))
botonComa.grid(row=5, column=2)
botonIgual=Button(marco, text="=", width=11, height=3, bg="yellowgreen", font=('arial',9,'bold'), command=lambda:igual())
botonIgual.grid(row=5, column=3)
botonSum=Button(marco, text="+", width=11, height=3, bg="orange", font=('arial',9,'bold'), command=lambda:suma(digitos.get())) #asigna la función al botón
botonSum.grid(row=5, column=4)





root.mainloop()