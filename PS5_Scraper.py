import requests
from bs4 import BeautifulSoup

target_console = requests.get('https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596')
target_controller = requests.get('https://www.target.com/p/dualsense-wireless-controller-for-playstation-5/-/A-81114477')
bb_controller = requests.get('https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163')
bb_console = requests.get('https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161')
newegg_console = requests.get('https://www.newegg.com/p/N82E16868110295')
soup = BeautifulSoup(newegg_console.text, 'html.parser')

body = soup.prettify()
print(body)