import requests
from bs4 import BeautifulSoup

proxy_list = []

def get_proxies():
    url = "https://free-proxy-list.net/"
    page = requests.get(url)
    content = BeautifulSoup(page.text, 'html.parser')
    table = content.find('table')
    rows = table.find_all('tr')
    headers = [header.text for header in rows[0]]

    for row in rows:
        proxy_list.append([data.text for data in row.find_all('td')])
    

def print_ips():
    for line in proxy_list[1:]:
        print(f"{line[0]}:{line[1]}")

def get_ips():
    ips = []
    for line in proxy_list[1:]:
        ips.append(f"{line[0]}:{line[1]}")
    return ips