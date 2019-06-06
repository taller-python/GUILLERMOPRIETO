import mimodulo
import pymongo

#mymodules.greeting("Jonathan") 
mimodulo.conexion_pymongo()

cliente = pymongo.MongoClient("mongodb://52.90.145.195:27017/")
base_datos = cliente ["guillermoprieto"]
coleccion = base_datos ["clientes"]

datos = {"Cedula": "8400500","Name": "Jaime Prieto","Correo": "jaime@hotmail.com","Cargo": "Contador","ValorHora": 36000,"HorasTrabajadas": 8,"SalarioaPagar": 328000}
x = coleccion.insert_one(datos)

if x:
     print("Cliente guardado correctamente con id", x.inserted_id)
else:
     print("Error al guardar")

