import json
import requests
import time
import os
from defs import form_date
from bs4 import BeautifulSoup

old_date = '2020-05-07T10:34:37Z'
my_url = 'https://api.covid19api.com/summary'

while True:
    #time.sleep(15)
    try:
        myjson = requests.get(my_url).json()
    except:
        print('Reloading...')
        os.system('C:/Users/ahmed/AppData/Local/Programs/Python/Python37/python.exe c:/Users/ahmed/OneDrive/Desktop/to-bash/main.py')
    new_date = myjson["Date"]
    if new_date != old_date:
        # taking data
        for i in myjson["Countries"]:
            if i["Country"] == "Azerbaijan":
                total_confirmed = i["TotalConfirmed"]
                new_cases = i["NewConfirmed"]
                total_death = i["TotalDeaths"]
                new_death = i["NewDeaths"]
                break

        # Validating Data
        if new_cases and new_death != 0:
        # Formatting Data
            print('-------------------------------------------')
            print('Azərbaycan Üçün COVİD-19 Statistikası')
            print(form_date(new_date))
            print('Ümumi yoluxanların sayı: ' + str(total_confirmed))
            print('Yeni yoluxanların sayı: +' + str(new_cases))
            print('Ümumi ölənlərin sayı: ' + str(total_death))
            print('Yeni ölənlərin sayı: +' + str(new_death))
        old_date = new_date