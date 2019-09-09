import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL1 = 'https://www.amazon.in/Huawei-Prime-Sapphire-128GB-Storage/dp/B07S6V5VXR/ref=sr_1_1_sspa?_encoding=UTF8&keywords=B07PRYN3DR+%7C+B07PT145YT&pf_rd_i=desktop&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=cc9b62a5-2189-486a-89b4-4eda80243fbe&pf_rd_r=92QB804CED4HMNAE1A7F&pf_rd_t=36701&qid=1568058483&s=electronics&smid=A14CZOWI0VEHLG&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTkM3NkdKS1lVSEREJmVuY3J5cHRlZElkPUEwNjM1MzUxSEJRMjIxOVAzSUFSJmVuY3J5cHRlZEFkSWQ9QTA1Nzc4NzYzTjFJVEdKRldGRTBNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
r = requests.get(URL1, headers=headers)

soup = BeautifulSoup(r.content, "lxml")


def track_price():
    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[2:7].replace(",", "")
    lastprice = float(converted_price.strip())
    if lastprice < 8999.0:
        send_mail()

    print(title.strip())
    print(lastprice)
    if lastprice > 8999.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('Your_Email', 'Your_Password')
    Subject = 'Price Fell Down!'
    body = f'Check Amazon Link : {URL1}'
    msg = f"Subject:{Subject}\n\n{body}"
    server.sendmail('From', 'To', msg)
    print('Hey Email has been Sent!Check inbox.......')
    server.quit()


while True:
    track_price()
    time.sleep(60)
