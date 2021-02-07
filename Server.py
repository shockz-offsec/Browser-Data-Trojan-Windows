import sqlite3
import os

#obtener y leer
#Copiar a otro directorio o no

#Enviar de client a server , haciendo que en el serve se guarden en x sitio.

PathName = os.getenv('localappdata') + \
            '\\Google\\Chrome\\User Data\\Default\\History'
con = sqlite3.connect(PathName)
cursor = con.cursor()
cursor.execute("SELECT url FROM urls")
urls = cursor.fetchall()

for r in urls:
 print(r)