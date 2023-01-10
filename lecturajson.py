from urllib.request import urlopen
import json

url = "http://jvilches.tk/jsonpersonas.php"

response = urlopen(url)

data_json = json.loads(response.read())

for data in data_json:
    print(data['rut'])
    print(data['nombre'])
    print(data['apellidop'])
    print(data['apellidom'])
    print(data['correo']) 

#print(data_json)