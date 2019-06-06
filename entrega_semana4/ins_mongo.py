import mimodulo
import pymongo

#mymodules.greeting("Jonathan") 
mimodulo.conexion_pymongo()

cliente = pymongo.MongoClient("mongodb://52.90.145.195:27017/")
base_datos = cliente ["guillermoprieto"]
coleccion = base_datos ["empleados"]

#datos = {"Cedula": "8400500","Name": "Jaime Prieto","Correo": "jaime@hotmail.com","Cargo": "Contador","ValorHora": 36000,"HorasTrabajadas": 8,"SalarioaPagar": 0}
#x = coleccion.insert_one(datos)

#if x:
 #    print("Cliente guardado correctamente con id", x.inserted_id)
#else:
 #    print("Error al guardar")

# Parent class
class Empleado():

   # Initializer / Instance attributes
    def __init__(self, valor_Cedula, valor_Nombre, valor_Correo, valor_Cargo, valor_ValorHora, valor_HorasTrabajadas):
          self.valor_Cedula = valor_Cedula
          self.valor_Nombre = valor_Nombre
          self.valor_Correo = valor_Correo
          self.valor_Cargo = valor_Cargo
          self.valor_ValorHora = valor_ValorHora
          self.valor_HorasTrabajadas = valor_HorasTrabajadas

# Child class (inherits from Compuerta class)
class Insertar(Empleado):
     def insertado(self, valor_Cedula, valor_Nombre, valor_Correo, valor_Cargo, valor_ValorHora, valor_HorasTrabajadas):
          #LONGITUD DE LOS VALAORES INGRESADOS
          nmb_longitud_valor_Cedula = len(str(valor_Cedula)) 
          #print(nmb_longitud_A)
          nmb_longitud_valor_Nombre = len(str(valor_Nombre)) 

          nmb_longitud_valor_Correo = len(str(valor_Correo)) 

          nmb_longitud_valor_Cargo= len(str(valor_Cargo)) 

          nmb_longitud_valor_ValorHora= len(str(valor_ValorHora)) 

          nmb_longitud_HorasTrabajadas= len(str(valor_HorasTrabajadas)) 
        
          if   (nmb_longitud_valor_Cedula >= 1 and 
               nmb_longitud_valor_Nombre >= 1 and 
               nmb_longitud_valor_Correo >= 1 and 
               nmb_longitud_valor_Cargo >= 1 and 
               nmb_longitud_valor_ValorHora >= 1 and 
               nmb_longitud_HorasTrabajadas >= 1) :
                    SalarioaPagar = valor_ValorHora * valor_HorasTrabajadas
 
                    datos = {"Cedula": valor_Cedula,"Nombre": valor_Nombre,"Correo": valor_Correo,"Cargo": valor_Cargo,"ValorHora": valor_ValorHora,"HorasTrabajadas": valor_HorasTrabajadas,"SalarioaPagar": SalarioaPagar}
                    x = coleccion.insert_one(datos)

                    if x:
                        return "Empleado guardado correctamente." + "Cedula: " + str(valor_Cedula) + " , Nombre: " + str(valor_Nombre) + ", Correo:" + str(valor_Correo) + ", Cargo: " + str(valor_Cargo) + ", ValorHora: "  + str(valor_ValorHora) + ", HorasTrabajadas: " + str(valor_HorasTrabajadas) + ", SalarioaPagar : " + str(SalarioaPagar)
                    else:
                         return "Error al guardar el Empleado"
          else:
                    return "Debe ingresar datos para los campos respectivamente. "
             
#Insertar_Cliente = Insertar("8500600", "Andres Prieto", "andes@hotmail.com", "Deportologo",45000, 6)
#Insertar_Cliente = Insertar("8600700", "Ana Prieto", "ana@hotmail.com", "Contadora",5000, 6)
#Insertar_Cliente = Insertar("43700800", "Juliana Montoya", "montoya@hotmail.com", "Contadora",10000, 9)
Insertar_Cliente = Insertar("71700800", "Juan Montoya", "juamontoya@hotmail.com", "Conductor",5000, 5)

#print(Insertar_Cliente.insertado("8500600", "Andres Prieto", "andes@hotmail.com", "Deportologo",45000, 6))
#print(Insertar_Cliente.insertado("8600700", "Ana Prieto", "ana@hotmail.com", "Contadora",5000, 6))
#print(Insertar_Cliente.insertado("43700800", "Juliana Montoya", "montoya@hotmail.com", "Contadora",10000, 9))
print(Insertar_Cliente.insertado("71700800", "Juan Montoya", "juamontoya@hotmail.com", "Conductor",5000, 5))
