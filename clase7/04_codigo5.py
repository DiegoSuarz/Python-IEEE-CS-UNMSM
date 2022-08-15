import csv
import urllib.request as url2

url = "https://datahub.smcgov.org/id/mb6a-xn89.json"

#conexion al archivo JSON:
response = url2.urlopen(url)

print(response)

head = ["geografía", "tipo_geografía", "tiempo"]
