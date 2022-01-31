import proxies
import requests
import time
from bs4 import BeautifulSoup

vote_for = '3967'
count = 0
tries = 0
n_votes = 10
proxies.get_proxies()
ips = proxies.get_ips()
#print("###\n#List of proxies\n###\n")
#proxies.print_ips()

def form_details(form, url):
    print(form)
    details = {}
    inputs = []
    method = form.attrs.get("method", "get").lower()

    for tag in form.find_all("input"):
        i_type = tag.attrs.get("type", "text")
        i_name = tag.attrs.get("name")
        i_value = tag.attrs.get("value", "")
        
        inputs.append({'type':i_type, 'name': i_name, 'value': ''})

    inputs[0]['value'] = vote_for
    
    details['action'] = url
    details['method'] = method
    details['inputs'] = inputs

    return(details)


def load_hodor():#proxy_ip, c, t):
    #print(f"trying: {proxy_ip}")
    #t += 1
    url = 'http://158.69.76.135/level0.php'
    try:
        s = requests.session()
    except Exception as ex:
        return 0#([c, t])

    #while c < n_votes: #must be 1024
    try:
        page = s.get(url)#, proxies={'http':proxy_ip, 'https': proxy_ip}, timeout=3)
        if page.status_code != 200:
            pass
    except Exception as ex:
        return 0#([c, t])
    #print(f"#{c}: Connected with: {proxy_ip}. tries: {t}")
    content = BeautifulSoup(page.text, 'html.parser')
    print(f"Voting for {vote_for}:")
    form = content.find('form')
    data = form_details(form, url)
    print(data)

    if data["method"] == "post":
        print("the method is post")
        res = s.post(f"{url}/{data['method']}", data=data)
        print(res.text)
    """
        if not form:
            return ([c, t])
        inp = [inp for inp in form.find_all('input')]

        for item in inp:
            print(item)
            print(f"{item.text}\n")
        data = {'id': vote_for}
        print(s.post(url, data).text)
        
        c += 1
        """
        #time.sleep(3)
    #return ([c, t])
    return (0)
    #request.post(url)
"""
while count < n_votes: #must be 1024
    print(count)
    for ip in ips:
        if (count >= n_votes): #must be 1024
            break
        count, tries = load_hodor(ip, count, tries)
"""
print("loading hodor")
count = load_hodor()

#print("\n\n\nNow im really calling")
#count = load_hodor("109.86.182.203:3128", count)
print(f"\n\n####\n#\n# Number of votes: {count}\n#\n####")