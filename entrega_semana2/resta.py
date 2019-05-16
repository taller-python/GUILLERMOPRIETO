import openpyxl


FILE_NAME = '.\operaciones.xlsx'
SHEET =  'RESTA'

f = open("resultado_resta.txt", "a")
workbook = openpyxl.load_workbook(FILE_NAME, read_only=True)
sheet = workbook[SHEET]

for row in sheet.iter_rows(min_row=2):
    res1 = str(row[0].value)
    res2 = str(row[1].value)
    res3 = str(row[0].value)
    res4 = str(row[1].value)
    print(res1)
    print(res2)
    print(res1.isnumeric())
    print(res2.isnumeric())
    if res1.isnumeric() == True and res2.isnumeric() == True:
       #suma = sum(sum3,sum4)
       #suma = float(sum3) + float(sum4)
       resta = int(res3) - int(res4)
       print(str(resta))
       f.write(str(resta) + "\n\t")
    else:
       print("Error nro 1 = " + res1 + "   nro 2 = " + res2)
       respuesta = "Error nro 1 = " + res1 + "   nro 2 = " + res2
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