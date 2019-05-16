import openpyxl


FILE_NAME = '.\operaciones.xlsx'
SHEET =  'DIVISIÓN'

f = open("resultado_division.txt", "a")
workbook = openpyxl.load_workbook(FILE_NAME, read_only=True)
sheet = workbook[SHEET]

for row in sheet.iter_rows(min_row=2):
    div1 = str(row[0].value)
    div2 = str(row[1].value)
    div3 = str(row[0].value)
    div4 = str(row[1].value)
    print(div1)
    print(div2)
    print(div1.isnumeric())
    print(div2.isnumeric())
    if div1.isnumeric() == True and div2.isnumeric() == True:
       #suma = sum(sum3,sum4)
       #suma = float(sum3) + float(sum4)
       if int(div4) != 0:
          division = int(div3) / int(div4)
          print(str(division))
          f.write(str(division) + "\n\t")
       else:
          print("Error nro 1 = " + div1 + "   nro 2 = " + div2)
          respuesta = "Error nro 1 = " + div1 + "   nro 2 = " + div2
          f.write(respuesta + "\n\t")   
    else:
       print("Error nro 1 = " + div1 + "   nro 2 = " + div2)
       respuesta = "Error nro 1 = " + div1 + "   nro 2 = " + div2
       f.write(respuesta + "\n\t")

       


#""" Prueba del hello world  """
#MSG = "Hello World"
#print(MSG)
#if __name__ ==  "__main__":
#    f = open(".\operaciones.xlsx", "r")
#json_schema = json.loads(schemacliente)

#respuesta =  "Esquema valido"
    
#f.close()     
try:
    #jsonschema.validate(event, json_schema)
    #jsonschema.validate(instance=cargar_cliente (ruta), schema=json_schema)
    #errors = jsonschema.Draft7Validator(json_schema)   
#print(errors(0).message)
    print(respuesta)
    respuesta = "Error nro 1 = " + div1 + "   nro 2 = " + div2
    f.write(respuesta + "\n\t")   
 
  
except: 
    print(respuesta)
    respuesta = "Error nro 1 = " + div1 + "   nro 2 = " + div2
    f.write(respuesta + "\n\t")   