import openpyxl


FILE_NAME = '.\operaciones.xlsx'
SHEET =  'SUMA'

f = open("resultado_suma.txt", "a")
workbook = openpyxl.load_workbook(FILE_NAME, read_only=True)
sheet = workbook[SHEET]

for row in sheet.iter_rows(min_row=2):
    sum1 = str(row[0].value)
    sum2 = str(row[1].value)
    sum3 = str(row[0].value)
    sum4 = str(row[1].value)
    print(sum1)
    print(sum2)
    print(sum1.isnumeric())
    print(sum2.isnumeric())
    if sum1.isnumeric() == True and sum2.isnumeric() == True:
       #suma = sum(sum3,sum4)
       #suma = float(sum3) + float(sum4)
       suma = int(sum3) + int(sum4)
       print(str(suma))
       f.write(str(suma) + "\n\t")
    else:
       print("Error nro 1 = " + sum1 + "   nro 2 = " + sum2)
       respuesta = "Error nro 1 = " + sum1 + "   nro 2 = " + sum2
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