import re
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
    except:
        pass

def create_readme(url):
    f = open("README.md", "w")
    f.write("# dizipal-finder\nher seferinde aramak istemeyenler için.\n\ndizipal güncel adres: " + str(url))
    f.close()

def get_last_url_digit():
    f = open("README.md", "r")
    x = re.findall(r"[\d]{1,4}", f.read())
    return x[0]

def main():
    digit = int(get_last_url_digit())
    while(digit < (digit + 100)):
        url = "http://www.dizipal" + str(digit) + ".com/"
        website = send_request(url)
        if(website != None):
            print(website)
            create_readme(url)
            exit()
        else:
            digit += 1

main()