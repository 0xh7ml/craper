from bs4 import BeautifulSoup as sp
import requests
first = input("Enter Ip Plz ::")
url = "https://ipinfo.io/ips/"+first+"/24"
url_2 = "https://ipinfo.io/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
r = requests.get(url , headers = headers)
op = r.text
soup = sp(op , 'html.parser')
td = soup.find_all('td')
for a in td:
    d = a.findChildren("a" , recursive=True)
    for links in d:
        i = links.text
        f = open("ips.txt" ,"a" )
        b = f.write(i+ "\n")
s = open("ips.txt" , "r")
for link in s :
    re = requests.get(url_2 + link , headers=headers)
    op_2 = re.text
    soup_2 = sp(op_2 , 'html.parser')
    ul = soup_2.find_all('ul' , class_="address-list domains-list")
    for urls in ul:
        diba = urls.text
        saikat = open("domains.txt" , "a")
        saikat.write(diba + "\n")
print("done")
