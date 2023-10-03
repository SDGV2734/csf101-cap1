import requests, time
from selenium import webdriver                                              
from selenium.webdriver.common.by import By

# use selenium loop through all my peer's leetcode profile
# get their last activity using xpath
# check if it has been more than a dqay/24hours
# if yes send message in telegram group that they did not dom leetcode

# wrong username      
# Chunku tamang 'Hleeseu'
usernames = [
        'SDGV2734',
        'khemraj9815',
        'C-gyeltshen',
        'DwangShers',
        'Dupchuwangmo7',
        'Kanishapradhan13',
        'SoftwareBob12345678910',
        'KeldenPDorji',
        'kinley_pal8',
        'Tobgaybolo',
        'Rabtens',
        'Namgay282004',
        'NamgyelHuk708',
        'Nidup21',
        'Norbu-d',
        'pemadolker',
        'pomegranateis ',
        'pyudey',
        'Rynorbu',
        'SangayZin',
        'zanyy',
        'SonamWangyelDorji',
        'tandinomu',
        'tanzzard',
        'UnknowingTW',
        'TandinZangmo456',
        'Baluthegoat ',
        'Eyemusician',
        'tdorji',
        'T-nobu',
        'tsheringphuntsho18',
        'twangpodorji',
        'Tshewangdorji7257',
        'user8860gL'
    ]

driver = webdriver.Chrome()

def last_activity_and_send_message(username):
    driver.get(f"https://leetcode.com/{username}")
    time.sleep(5)
    last_activity_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[2]')
    last_activity_text = last_activity_element.text
    time.sleep(5)
    print(last_activity_text)

    if "days" in last_activity_text or "day" in last_activity_text:
        print('BAD')
        send_telegram_message(f"{username} did not do LeetCode for more than 24 hours.")
    elif "weeks" in last_activity_text or "week" in last_activity_text:
        print('BAD')
        send_telegram_message(f"{username} did not do LeetCode for more than a week.")
    elif "months" in last_activity_text or "month" in last_activity_text:
        print('BAD')
        send_telegram_message(f"{username} did not do LeetCode for more than a month.")
    elif "years" in last_activity_text or "year" in last_activity_text:
        print('BAD')
        send_telegram_message(f"{username} did not do LeetCode for more than a year.")
          
        
def send_telegram_message(message):

    token = "6340249508:AAEEOqOv7Jt1VnLfAxrObQE1-0h-xdBUKEg"
    chat_id = "@cstsweleetcode"
    #message = requests.get(url).json()
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    time.sleep(1)
    print(requests.get(url).json()) # this sends the message

for username in usernames:
    last_activity_and_send_message(username)

# last_activity_and_send_message(usernames[2])








'''import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

usernames = [
    "SDGV2734",
    "khemraj9815"
]

driver = webdriver.Chrome()

def last_activity_and_send_message(username):
    driver.get(f"https://leetcode.com/{username}")

    last_activity_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[2]")
    last_activity_text = last_activity_element.text

    if "day" in last_activity_text:
        days_ago = int(last_activity_text.split()[0])
        if days_ago > 1:
            send_telegram_message(f"{username} please do your LeetCode problems")

    elif "hour" in last_activity_text:
        hours_ago = int(last_activity_text.split()[0])
        if hours_ago > 24:
            send_telegram_message(f"{username} did not do LeetCode for more than 24 hours.")

def send_telegram_message(message):
    token = "6340249508:AAEEOqOv7Jt1VnLfAxrObQE1-0h-xdBUKEg"
    chat_id = "@cstsweleetcode"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url)
    print(response.json())  # This sends the message

for username in usernames:
    last_activity_and_send_message(username)'''
