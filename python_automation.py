# Save mobile number in another file called credentials.py
# and import it from their to maintain privacy
from credentials import mobile_number
import requests
import time
import schedule

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : mobile_number,
        'message' : 'Kay kartoyes?',
        'key' : 'textbelt'
    })
    print(resp.json())

# schedule.every().day.at('06:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)