#import requests
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import getpass

# from http import cookies

# C = cookies.SimpleCookie()
# C.load('cookie: S=spreadsheet_forms=_SRAYibSgGw6XeIFK4VphUnIi6N8Ybn_pksmyyZEItU; SEARCH_SAMESITE=CgQIoY8B; SID=zwdnSILIL_34hHAeO9liu_lP5ecYppyrudZrOER9gDu5-9g7vnkewsXBsHlGY5TnspT7sA.; __Secure-3PSID=zwdnSILIL_34hHAeO9liu_lP5ecYppyrudZrOER9gDu5-9g7mdpX_88FukLkqv5pHc61KA.; HSID=A7420ffL5hCEBPyxN; SSID=ABrAo21_KIsCVpTeJ; APISID=Ss0yBbFg256Im-ra/AL2be60NNQoBx-A7q; SAPISID=KRqQjiZX1zZdOlRP/AKtUQw7ZuVb7KEzA5; __Secure-3PAPISID=KRqQjiZX1zZdOlRP/AKtUQw7ZuVb7KEzA5; ANID=AHWqTUl6QgUuu3sWQy5P8e7cPHuhF111kXrt447MBjIOLMc2wUnL1m5GrV6Xw99I; 1P_JAR=2020-8-5-14; NID=204=zd4R0N7lbCIP2vR2Z2bZ2LIDBUVFsJwUrBhjxHRxjb0u6ulNf7Ijb01ag7Xf9jyXA1Hn-obfHk2KVLfDwYa_8w1MVrlgD3rbi6Q4qCzw9FmHpPNBQwE9u-ExDuyg4aYzcVEaOAoLOBw4Vjw2wPboO3_7yjDt9UK5pt--jL8p9AjHoCFef7bwNAAxJz_HEVH0pGgolHVYOXc-4lkXB5-C8y5HbSS3mlUelil4AbhvNCY; SIDCC=AJi4QfHOqm3bMfkmBlCW0LxCrq5zLcC2NifPM3ygRrR3qpEDmgZqQTgOgBm3hnhGibIo7cbworM')

# rawdata = 'cookie: S=spreadsheet_forms=_SRAYibSgGw6XeIFK4VphUnIi6N8Ybn_pksmyyZEItU; SEARCH_SAMESITE=CgQIoY8B; SID=zwdnSILIL_34hHAeO9liu_lP5ecYppyrudZrOER9gDu5-9g7vnkewsXBsHlGY5TnspT7sA.; __Secure-3PSID=zwdnSILIL_34hHAeO9liu_lP5ecYppyrudZrOER9gDu5-9g7mdpX_88FukLkqv5pHc61KA.; HSID=A7420ffL5hCEBPyxN; SSID=ABrAo21_KIsCVpTeJ; APISID=Ss0yBbFg256Im-ra/AL2be60NNQoBx-A7q; SAPISID=KRqQjiZX1zZdOlRP/AKtUQw7ZuVb7KEzA5; __Secure-3PAPISID=KRqQjiZX1zZdOlRP/AKtUQw7ZuVb7KEzA5; ANID=AHWqTUl6QgUuu3sWQy5P8e7cPHuhF111kXrt447MBjIOLMc2wUnL1m5GrV6Xw99I; 1P_JAR=2020-8-5-14; NID=204=zd4R0N7lbCIP2vR2Z2bZ2LIDBUVFsJwUrBhjxHRxjb0u6ulNf7Ijb01ag7Xf9jyXA1Hn-obfHk2KVLfDwYa_8w1MVrlgD3rbi6Q4qCzw9FmHpPNBQwE9u-ExDuyg4aYzcVEaOAoLOBw4Vjw2wPboO3_7yjDt9UK5pt--jL8p9AjHoCFef7bwNAAxJz_HEVH0pGgolHVYOXc-4lkXB5-C8y5HbSS3mlUelil4AbhvNCY; SIDCC=AJi4QfHOqm3bMfkmBlCW0LxCrq5zLcC2NifPM3ygRrR3qpEDmgZqQTgOgBm3hnhGibIo7cbworM'
# cookie = SimpleCookie()
# cookie.load(rawdata)
# cookies = {}
# for key, morsel in cookie.items():
#     cookies[key] = morsel

cookies = {
    'S': "spreadsheet_forms=_SRAYibSgGw6XeIFK4VphUnIi6N8Ybn_pksmyyZEItU"
}

url = 'https://docs.google.com/forms/d/e/1FAIpQLSc086Hv3C5pnQb_r-lOsHIJCmiSItv521_YB4a-YAT9-cCXfA/formResponse'
driver = webdriver.Chrome()
driver.get(url)
inputElement = driver.find_element_by_name("entry.")
# inputElement.send_keys(email + Keys.RETURN)
# driver.implicitly_wait(10)

def get_values():

    values_list = []
    subjects_time =  [1,2,3,10,4,6,7]

    for i in subjects_time:
        values = {
            # First Name
            "entry.1933011615": str(sys.argv[1]),
            # Last Name
            "entry.1523459763": str(sys.argv[2]),
            # Student ID
            "entry.757962289": str(sys.argv[3]),
            # Class Period
            "entry.788775554": str(i),
            # Present
            "entry.368504989": "yes"
        }

        values_list.append(values)

    return values_list


def send_attendance(url, data):
    for d in data:
        try:


            # requests.post(url, data=d, cookies=cookies)
            print("Form Submitted.")
            time.sleep(1)
        except:
            print("Error Occured!")


final_data = get_values()

send_attendance(url, final_data)