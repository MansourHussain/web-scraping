import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import lxml

# 1 lists
district_Name = []
property_size = []
property_price = []

page_num = 0

# 2 the link of website
while True:
    result = requests.get(f"https://sa.aqar.fm/%D9%81%D9%84%D9%84-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6/{page_num}")
    # 3 step save page
    src = result.content

    # 4 create soup
    soup = BeautifulSoup(src, "lxml")
    if page_num > 500:
        break


    # 5 titles we need: districtName, property Age, size, rooms, price
    districtName = soup.findAll("a", {"class": "listTitle"})
    size = soup.findAll("span", {"class": "size"})
    price = soup.findAll("span", {"class": "price"})




    # 6 for loop to get text and append it to a list

    for i in range(len(districtName)):
        district_Name.append(districtName[i].text)
        property_size.append(size[i].text)
        property_price.append(price[i].text)


    page_num+=1



file_list = [district_Name, property_size, property_price]
exported = zip_longest(*file_list)
# 7 create a csv file and fill it with values
with open("C:/Users/Manso/Desktop/files\Data Analysis\Aqar.csv", "w") as aqar_file:
    wr = csv.writer(aqar_file)
    wr.writerow(['district_Name', 'property_size', 'property_price'])
    wr.writerows(exported)
