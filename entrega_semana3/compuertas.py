""" Prueba del hello world  """
MSG = "Hello World"
print(MSG)
# Parent class
class Compuerta():

   # Initializer / Instance attributes
    def __init__(self, valor_A, valor_B):
        self.valor_A = valor_A
        self.valor_B = valor_B

# Child class (inherits from Compuerta class)
class CompuertaAND(Compuerta):
     def resultado(self, valor_A,valor_B):
        #LONGITUD DE LOS VALAORES INGRESADOS
        nmb_longitud_A= len(str(valor_A)) 
        #print(nmb_longitud_A)

        nmb_longitud_B= len(str(valor_B) )
        #print(nmb_longitud_B)

        if nmb_longitud_A == 1 and nmb_longitud_B == 1:

            if (valor_A == 1 or valor_A == 0) and (valor_B == 1 or valor_B == 0) : 

                if valor_A == 1 and valor_B == 1: 
                    return "{} y {}  VERDADEDO ".format(self.valor_A, self.valor_B)
                else:
                    return "{} y {}   FALSO ".format(self.valor_A, self.valor_B)
            else:
                return "Los valores de A y B, {} o {} respectivamente, deben ser numeros binarios, esto es: 0 o 1 ".format(self.valor_A, self.valor_B)

        else:
            return "Los valores de A y B, {} o {} respectivamente, deben ser numeros binarios, esto es: 0 o 1 ".format(self.valor_A, self.valor_B)


# Child class (inherits from Compuerta class)
class CompuertaOR(Compuerta):
    def resultado(self, valor_A,valor_B):
        #LONGITUD DE LOS VALAORES INGRESADOS
        nmb_longitud_A= len(str(valor_A)) 
        #print(nmb_longitud_A)

        nmb_longitud_B= len(str(valor_B) )
        #print(nmb_longitud_B)

        # if(valor_A == "undefined" and valor_B == "undefined"):
        if nmb_longitud_A == 1:

            if nmb_longitud_A == 1 and nmb_longitud_B == 1:

                if (valor_A == 1 or valor_A == 0) and (valor_B == 1 or valor_B == 0) : 

                    if valor_A == 0 and valor_B == 0: 
                        return "{} o {}   FALSO".format(self.valor_A, self.valor_B)
                    else:
                        return "{} o {}   VERDADEDO".format(self.valor_A, self.valor_B)
                else:
                    return "Los valores de A y B, {} o {} respectivamente, deben ser numeros binarios, esto es: 0 o 1 ".format(self.valor_A, self.valor_B)

            else:
                return "Los valores de A y B, {} o {} respectivamente, deben ser numeros binarios, esto es: 0 o 1 ".format(self.valor_A, self.valor_B)

        else:
            return "Los valores de A y B, {} o {} respectivamente, deben ser numeros binarios, esto es: 0 o 1 ".format(self.valor_A, self.valor_B)

# Child classes inherit attributes and
# behaviors from the parent class
# compuerta_AND = CompuertaAND(0, 0)
# compuerta_AND = CompuertaAND(1, 1)
# compuerta_AND = CompuertaAND(0, 1)
# compuerta_AND = CompuertaAND(1, 0)
# Child classes have specific attributes
# and behaviors as well
# print(compuerta_AND.resultado(0, 0))
# print(compuerta_AND.resultado(1, 1))
# print(compuerta_AND.resultado(0, 1))
#print(compuerta_AND.resultado(1, 0))

compuerta_OR = CompuertaOR(0, 0)
# compuerta_OR = CompuertaOR(1, 1)
# compuerta_OR = CompuertaOR(0, 1)
# compuerta_OR = CompuertaOR(1, 0)

print(compuerta_OR.resultado(0, 0))
# print(compuerta_OR.resultado(1, 1))
# print(compuerta_OR.resultado(0, 1))
# print(compuerta_OR.resultado(1, 0))

