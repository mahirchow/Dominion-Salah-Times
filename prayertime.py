#import the necessary libraries
import requests
import pprint
import re
from bs4 import BeautifulSoup
# import pandas as pd

# make a url, get the html file as text, then convert the page into bs4 object
url = 'https://windsorislamicassociation.com/'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify()) #prints out contents of soup

# find the table that contains our desired information
table = soup.find('table', {'class': 'dptTimetable customStyles dptUserStyles'})

# make a list for all the major salahs and times of the day/week
prayers = ['Fajr', 'Sunrise', 'Zuhr', 'Asr', 'Maghrib', 'Isha', 'Jummah']

# extract the table for salah timings from the html file
times = table.findAll('td')

# initialize the prayer dict with every one of the salah names
prayer_dict = {i: [] for i in prayers}

# find all the timings within the table of html file
timings = re.findall(r'(\d{1,2}:\d\d\s(am|pm))', str(times))

# set the timings for athaan and iqama inside the dictionary
prayer_dict['Fajr'].append(timings[0][0])
prayer_dict['Fajr'].append(timings[1][0])
prayer_dict['Sunrise'].append(timings[2][0])
prayer_dict['Zuhr'].append(timings[3][0])
prayer_dict['Zuhr'].append(timings[4][0])
prayer_dict['Asr'].append(timings[5][0])
prayer_dict['Asr'].append(timings[6][0])
prayer_dict['Maghrib'].append(timings[7][0])
prayer_dict['Maghrib'].append(timings[8][0])
prayer_dict['Isha'].append(timings[9][0])
prayer_dict['Isha'].append(timings[10][0])
prayer_dict['Jummah'].append(timings[11][0])
prayer_dict['Jummah'].append(timings[12][0])

# print out the dictionary
# pprint.pprint(prayer_dict)

print('_'*38)
print('PRAYER         ATHAAN          IQAMA')
print('_'*38)
print('Fajr           ' + prayer_dict['Fajr'][0] + '         ' + prayer_dict['Fajr'][1])
print('Sunrise        ' + prayer_dict['Sunrise'][0])
print('Zuhr           ' + prayer_dict['Zuhr'][0] + '        ' + prayer_dict['Zuhr'][1])
print('Asr            ' + prayer_dict['Asr'][0] + '         ' + prayer_dict['Asr'][1])
print('Maghrib        ' + prayer_dict['Maghrib'][0] + '         ' + prayer_dict['Maghrib'][1])
print('Isha           ' + prayer_dict['Isha'][0] + '         ' + prayer_dict['Isha'][1])
print('_'*38)
print('1ST Jummah: ' + prayer_dict['Jummah'][0])
print('2ND Jummah: ' + prayer_dict['Jummah'][1])
print('_'*38)
