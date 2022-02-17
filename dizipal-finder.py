import requests
from bs4 import BeautifulSoup

def send_request(url):
    try:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        for title in soup.find_all('title'):
            # print(url + " internet sitesi başlığı: " + title.get_text())
            if(title.get_text() == 'DiziPAL – yabancı dizi, film ve anime izle'):
                return url
            else:
                return None

    except Exception as e:
        e

number = 150
while(number < 1000):
    url = "http://www.dizipal" + str(number) + ".com/"
    website = send_request(url)
    if(website != None):
        print(website)
        exit()
    else:
        number += 1
