import requests
import os
from twilio.rest import Client
from bs4 import BeautifulSoup

# Twilio authentication
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
client = Client(account_sid, auth_token)


def send_sms():
    message = client.messages \
                .create(
                     body="PS5 current stock: Target - 0, Best Buy - 0, Newegg - 0, Walmart - 0, Amazon - 0",
                     from_='+19136672674',
                     to='+19802534526'
                 )

    print(message.sid)


print(send_sms())

"""
# Header info
header = {
    "authority": "www.bestbuy.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161"
}

# URLs to pull data
target_console = requests.get('https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596')
target_controller = requests.get('https://www.target.com/p/dualsense-wireless-controller-for-playstation-5/-/A-81114477')
bb_controller = requests.get('https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163')
bb_console = requests.get('https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161', headers=header)
newegg_console = requests.get('https://www.newegg.com/p/N82E16868110295')
soup = BeautifulSoup(bb_console.text, 'html.parser')

body = soup.prettify()
print(body)

"""