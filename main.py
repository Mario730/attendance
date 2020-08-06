import requests
import time
import sys

cookies = {
    'S': "spreadsheet_forms=Y0nBs7KHXn1gnMMhF2vDR_QHAXIDT_Ug-QmlQWa7_to"
}

# url_list = ['https://docs.google.com/forms/d/e/1FAIpQLSdrRzPbLMMfgAPu9NRSX8qtgmkVAe6B9ASqabsnOEBqC2z1MQ/formResponse','https://docs.google.com/forms/d/e/1FAIpQLSdRv47P-xplRNcxX7gLwQ2zAICTNmXegI9TTFvbRpNxLFOi4Q/formResponse']
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdRv47P-xplRNcxX7gLwQ2zAICTNmXegI9TTFvbRpNxLFOi4Q/formResponse'

def get_values():

    values_list = []
    subjects_time =  ["Period 1","Period 2","Period 3","Period 10","Period 4","Period 6","Period 7"]

    for i in subjects_time:
        values = {
            # First Name
            "entry.602267705": str(sys.argv[1]),
            # Last Name
            "entry.1147887237": str(sys.argv[2]),
            # Student ID
            "entry.454542477": str(sys.argv[3]),
            # Class Period
            "entry.755105070": str(i),
            # Present
            "entry.1423938319": "Yes"
        }

        values_list.append(values)

    return values_list


def send_attendance(url, data):
    for d in data:
        try:
            requests.post(url, data=d, cookies=cookies)
            print("Form Submitted.")
            time.sleep(1)
        except:
            print("Error Occured!")


final_data = get_values()

send_attendance(url, final_data)