#def FUN_POLINDROMO(VCH_PALABRA):
#p. ej., anilina; dábale arroz a la zorra el abad
""" Prueba del hello world  RECONOCER   ALA    """
MSG = "Hello World"
print(MSG)

#PALABRA DE LA PALABRA INGRESADA
print("Digite la palabra: ")
VCH_PALABRA = input()
print(VCH_PALABRA)
    #PALABRA = "ALA"
    #PALABRA = "RECONOCER"
    #print(PALABRA)

    #LONGITUD DE LA PALABRA INGRESADA
NMB_LONGITUD = len(VCH_PALABRA) 
print(NMB_LONGITUD)

    #print(b[2:5])
    #x[::-1]
if NMB_LONGITUD == 0:
   print("Si quiere verificar si la palabra es polindroma(que es la misma palabara de izquierda a derecha que de derecha a izquierda)  debe digitar una palabra. "  )
else:
   if VCH_PALABRA == VCH_PALABRA[::-1]: 
      print("La palabra :   " + VCH_PALABRA + "   es un polindromo. "  )
   else:
      print("La palabra :   " + VCH_PALABRA + "   no es un polindromo. "  )
#print(MITAD_POLINDROMO)

#if MITAD_PALABRA == MITAD_POLINDROMO:
#    print("La palabra :  " + PALABRA + "  es un polindromo. "  )
