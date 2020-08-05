import requests
from bs4 import BeautifulSoup

def coastcapital():

    URL = 'https://www.coastcapitalsavings.com/rates/mortgages'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find('table')
    
    return(results)