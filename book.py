import requests
import csv
from bs4 import BeautifulSoup
import re

list_head = ['书名','书籍链接','跳转百度链接','百度网盘链接','提取码']
f = open(r'C:\Users\Public\Documents\itPanda1.csv', 'w+')
f_csv = csv.writer(f)
f_csv.writerow(list_head)
url = "https://itpanda.net/book/"
for i in range(1,423):
    u_url = url+str(i)
    response = requests.get(u_url)
    print(response.status_code)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        a = soup.find('h4')
        name = a.get_text()
        baidu = re.findall(r'href="/book/(.*?)"', html)
        pan = 'https://itpanda.net/book/'+ str(baidu[-1])
        print(baidu[-1], pan)
        pan_d = requests.get(pan)
        p_soup = BeautifulSoup(pan_d.text,'html.parser')
        pan_href = p_soup.find("a",{"class":"text-danger alert-link"})
        pan_link = pan_href.get_text()
        tiquma = re.findall(r'提取码:(.*?)</p>',pan_d.text)
        b = [name,u_url,pan,pan_link,str(tiquma[0])]
        f_csv.writerow(b)
    else:
        continue
f.close()
