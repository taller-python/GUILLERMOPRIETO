import pymongo
from bson.objectid import ObjectId

#import boto3

#import Flask
#from flask 

#import  render_template

cliente = pymongo.MongoClient("mongodb://52.90.145.195:27017/")
base_datos = cliente ["guillermoprieto"]
cole_cliente = base_datos ["empleados"]

#cliente_iddociden =  "1000300400"
#cliente_iddociden =  "71700800"
#print (cliente_iddociden)

#def ConCliente (cliente_iddociden):
 #   try:
        
        #cliente_iddociden = recdatcliente["documentoIdentidad"]
        #cliente_iddociden =  "17778889999"
        #cliente_iddociden =  "1000300400"
        #print(cliente_iddociden)        
        #cliente_id = $_GET["cliente_iddociden"] 
        #print(cliente_id)        
        #cliente_iddociden = $_GET["cliente_iddociden"] 

        #cliente_iddociden = recdatcliente["documentoIdentidad"]
        #print(cliente_iddociden)        
        
#asigcliente_id = "5ca9790ca24b2018b0c84aef"
#asigcliente_id = "5ceca50bd5306c4c70e8f482"
#print(asigcliente_id)

#print (cliente_iddociden)
#_id = base_datos.cole_cliente.find_one({"Cedula": cliente_iddociden})
#_id = base_datos.cole_cliente.find({"Cedula": "71700800"})
#print (_id)

#dfor i in base_datos.cole_cliente.find({"_id": ObjectId(_id)})  
#dprint(i)
#for i in cole_cliente.find({"_id": ObjectId(asigcliente_id)})  
#print(i)
#i = cole_cliente.find({"_id": ObjectId(asigcliente_id)}) 
#print(i)
 
#cursor = collection.find()
#for fut in cursor:
#    print "%s - %s - %i - %s - %r" \
#          %(fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'], fut['internacional'])

# Parent class
class Empleado():

   # Initializer / Instance attributes
    def __init__(self, valor_Cedula):
          self.valor_Cedula = valor_Cedula
 
# Child class (inherits from Compuerta class)
class Actualizar(Empleado):
     def actualizado(self, valor_Cedula):
          #LONGITUD DE LOS VALAORES INGRESADOS
          nmb_longitud_valor_Cedula = len(str(valor_Cedula)) 
          #print(nmb_longitud_A)
          
          if   (nmb_longitud_valor_Cedula >= 1)  : 
            try:
                cursor = cole_cliente.update_one(({"Cedula":{"$in":[valor_Cedula]}}),{"$inc":{"ValorHora":2000}}, upsert = False)
                #cursor = cole_cliente.update_one(({"Cedula":{"$in":[cedula_empleado]}}),{"$eq":{"HorasTrabajadas":6}}, upsert = False)
                cursor = cole_cliente.update_one(({"Cedula":{"$in":[valor_Cedula]}}),{"$inc":{"SalarioaPagar":12000}}, upsert = False)
                #for emp in cursor:
                #print( "%s  - %s- %s - %i - %i - %i"  %(emp['Cedula'], emp['Cargo'], emp['Correo'], emp['ValorHora'], emp['HorasTrabajadas'], emp['SalarioaPagar']))
 
            except Exception as excep:
                print(excep)         
          else:
                return "Debe ingresar el numero de la cedula. "
   #print( "%s - %s"  %(emp['Cedula'], emp['Nombre']))

        #print(respuesta)
    #except Exception as excep:
    #    print(excep)       


    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    #43700800
    #71700800

    #8600700
    #8400500
    #8500600
Actualizar_Empleado = Actualizar("8600700")
print(Actualizar_Empleado.actualizado("8600700"))