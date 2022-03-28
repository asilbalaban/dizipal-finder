import re, os, requests, sys
from bs4 import BeautifulSoup

def send_request(url):
    try:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for title in soup.find_all('title'):
            print(url + " internet sitesi başlığı: " + title.get_text())
            if(title.get_text() == 'DiziPAL – yabancı dizi, film ve anime izle'):
                return url
            else:
                return None
    except:
        pass

def create_readme(url):
    f = open(get_current_path("README.md"), "w")
    f.write("# dizipal-finder\nher seferinde aramak istemeyenler için.\n\ndizipal güncel adres: " + str(url))
    f.close()

def get_last_url_digit():
    f = open(get_current_path("README.md"), "r")
    x = re.findall(r"[\d]{1,4}", f.read())
    return x[0]

def main():
    digit = int(get_last_url_digit())
    while(True):
        url = "http://www.dizipal" + str(digit) + ".com/"
        print(url)
        website = send_request(url)
        if(website != None):
            isItOk = input('Bu sayfayı yüklemek ister misiniz? (e/h)')
            if(isItOk == 'e'):
                print(website)
                create_readme(url)
                commit()
                exit()
            else:
                digit += 1
        else:
            digit += 1

def commit():
    os.system("git add .")
    os.system("git commit -m 'auto commit by dizipal-finder.py'")
    os.system("git push")

def get_current_path(filename = None):
    if(filename == None):
        return os.path.dirname(os.path.realpath(__file__))
    else:
        return os.path.dirname(os.path.realpath(__file__)) + "/" + filename

if __name__ == "__main__":
    main()
