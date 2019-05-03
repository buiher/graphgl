#!D://Python37//python.exe
import json
print('Content-type: text/html\r\n\r')
from sgqlc.endpoint.http import HTTPEndpoint

url = 'https://sljb3i4wwfh2lnxfvwvrj5jjfe.appsync-api.us-east-2.amazonaws.com/graphql'
headers = {'x-api-key': 'da2-f4vpoh5xcngehbapcidqoldcmi'}

query = "query listLibros {  listLibros {    items {      id      titulo      subtitulo      autor      categoria      fecha_publicacion      editor      descripcion      imagen    }  }}"
variables = {'varName': 'value'}

endpoint = HTTPEndpoint(url, headers)
data = endpoint(query, variables)

print(json.dumps(data, indent=4))