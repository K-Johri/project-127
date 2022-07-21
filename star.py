from bs4 import BeautifulSoup as bs
##from selenium import selenium
import requests
import pandas as pd

stars = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(stars)
print(page)

soup = bs(page.text,'html.parser')
str_table = soup.find('table')

temp = []
table_rows = str_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)

star_name = []
star_distance = []
star_mass = []
star_radius = []
star_lum = []

for i in range(1,len(temp)):
    star_name.append(temp[i][1])
    star_distance.append(temp[i][3])
    star_mass.append(temp[i][5])
    star_radius.append(temp[i][6])
    star_lum.append(temp[i][7])

df2 = pd.DataFrame(list(zip(star_name,star_distance,star_mass,star_radius,star_lum)),columns = ['STAR NAME','DISTANCE','MASS','RADIUS','LUMINOUS'])
print(df2)

df2.to_csv('stars.csv')
