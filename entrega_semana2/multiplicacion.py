import openpyxl


FILE_NAME = '.\operaciones.xlsx'
SHEET =  'MULTIPLICACIÓN'

f = open("resultado_multiplicacion.txt", "a")
workbook = openpyxl.load_workbook(FILE_NAME, read_only=True)
sheet = workbook[SHEET]

for row in sheet.iter_rows(min_row=2):
    mul1 = str(row[0].value)
    mul2 = str(row[1].value)
    mul3 = str(row[0].value)
    mul4 = str(row[1].value)
    print(mul1)
    print(mul2)
    print(mul1.isnumeric())
    print(mul2.isnumeric())
    if mul1.isnumeric() == True and mul2.isnumeric() == True:
       #suma = sum(sum3,sum4)
       #suma = float(sum3) + float(sum4)
       multiplicacion = int(mul3) * int(mul4)
       print(str(multiplicacion))
       f.write(str(multiplicacion) + "\n\t")
    else:
       print("Error nro 1 = " + mul1 + "   nro 2 = " + mul2)
       respuesta = "Error nro 1 = " + mul1 + "   nro 2 = " + mul2
       f.write(respuesta + "\n\t")

       


#""" Prueba del hello world  """
#MSG = "Hello World"
#print(MSG)
#if __name__ ==  "__main__":
#    f = open(".\operaciones.xlsx", "r")
#json_schema = json.loads(schemacliente)

#respuesta =  "Esquema valido"
    
  
#try:
    #jsonschema.validate(event, json_schema)
    #jsonschema.validate(instance=cargar_cliente (ruta), schema=json_schema)
    #errors = jsonschema.Draft7Validator(json_schema)   
#print(errors(0).message)
print(respuesta)
f.close()    
#except jsonschema.ValidationError :