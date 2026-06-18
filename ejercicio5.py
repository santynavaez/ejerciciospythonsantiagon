#teniendo dos numeros realice las operaciones suma resta multiplicacion o divicion segun elija el usuario
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
operacion=input("ingrese la operacion que desea realizar: ")
if operacion=="+":
    suma= numero1+numero2
    print("la suma de los dos numeros es: ",suma)
if(operacion=="-"):
    resta= numero1-numero2
    print("la resta de los dos numeros es: ",resta)
if(operacion=="*"):
    multiplicacion= numero1*numero2
    print("la multiplicacion de los dos numeros es: ",multiplicacion)
if(operacion=="/"):
    divicion= numero1/numero2
    print("la divicion de los dos numeros es: ",divicion)

 
    