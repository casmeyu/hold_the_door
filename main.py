import proxies
import requests
import time
from bs4 import BeautifulSoup

vote_for = '3965'
count = 0
tries = 0
n_votes = 10
proxies.get_proxies()
ips = proxies.get_ips()
#print("###\n#List of proxies\n###\n")
#proxies.print_ips()

def load_hodor(proxy_ip, c, t):
    print(f"trying: {proxy_ip}")
    t += 1
    url = 'http://158.69.76.135/level0.php'
    try:
        s = requests.session()
    except Exception as ex:
        return ([c, t])

    while c < n_votes: #must be 1024
        try:
            page = s.get(url, proxies={'http':proxy_ip, 'https': proxy_ip}, timeout=3)
            if page.status_code != 200:
                break
        except Exception as ex:
            return ([c, t])
        print(f"#{c}: Connected with: {proxy_ip}. tries: {t}")
        content = BeautifulSoup(page.text, 'html.parser')
        print(f"Voting for {vote_for}:")
        form = content.find('form')
        if not form:
            return ([c, t])
        inp = [inp for inp in form.find_all('input')]

        for item in inp:
            print(item)
            print(f"{item.text}\n")
        post = {'id': vote_for}

        c += 1
        #time.sleep(3)
    return ([c, t])
    #request.post(url)
while count < n_votes: #must be 1024
    print(count)
    for ip in ips:
        if (count >= n_votes): #must be 1024
            break
        count, tries = load_hodor(ip, count, tries)

#print("loading hodor")
#count = load_hodor(count)

#print("\n\n\nNow im really calling")
#count = load_hodor("109.86.182.203:3128", count)
print(f"\n\n####\n#\n# Number of votes: {count}\n#\n####")