#two libraries is needed
#textbelt and schedules
import requests
import schedule
import time

def sendSMS():
    resp = requests.post('https://textbelt.com/text', {     
    'phone': +2349030299983,
    'message': 'Good morning, this is a test message',
    'key': 'textbelt',
    })
    
    print(resp.json())
    
    # schedule.every().day.at("15:00").do(sendSMS)
    # 
    # 
schedule.every(10).seconds.do(sendSMS)
while True:
    schedule.run_pending()
    time.sleep(1)
    
