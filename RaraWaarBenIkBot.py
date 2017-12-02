#importing things for bot
import json 
import requests
import time
import urllib

#importing and defining things for the spreadsheet and link to it
import gspread
import math
from oauth2client.service_account import ServiceAccountCredentials

scope = ['http://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('TelegramBot.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Telegram Bot').sheet1

#defining things for bot

TOKEN = "494183459:AAEDLvYpthr3dPZxK2qlQNHJU9JthRatLps"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

#bot code to get information

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
	if text == "Yoram +1": #code voor yoram
		sheet_input_yoram = sheet.cell(1,2).value
		def add(a_yoram, b_yoram):
			return a_yoram + b_yoram
		a_yoram = eval(sheet_input_yoram)
		b_yoram = 1
		score_yoram = eval('add(a_yoram, b_yoram)')
		sheet.update_cell(1,2, score_yoram)
		text = "Yoram received one point!"
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)
	elif text == "David +1": #code voor david
		sheet_input_david = sheet.cell(2,2).value
		def add(a_david, b_david):
			return a_david + b_david
		a_david = eval(sheet_input_david)
		b_david = 1
		score_david = eval('add(a_david, b_david)')
		sheet.update_cell(2,2, score_david)
		text = "David received one point!"
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)
	elif text == "Henrike +1": #code voor henrike
		sheet_input_henrike = sheet.cell(3,2).value
		def add(a_henrike, b_henrike):
			return a_henrike + b_henrike
		a_henrike = eval(sheet_input_henrike)
		b_henrike = 1
		score_henrike = eval('add(a_henrike, b_henrike)')
		sheet.update_cell(3,2, score_henrike)
		text = "Henrike received one point!"
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)
	elif text == "Reset all":
		sheet.update_cell(1,2, 0)
		sheet.update_cell(2,2, 0)
		sheet.update_cell(3,2, 0)
		text = "All scores are back to zero!"
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)
	elif text == "What is Yoram's score?":
		sheet_input_yoram = sheet.cell(1,2).value
		text = "Yoram's score is {}".format(sheet_input_yoram)
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)
	elif text == "What is David's score?":
		sheet_input_david = sheet.cell(2,2).value
		text = "David's score is {}".format(sheet_input_david)
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)
	elif text == "What is Henrike's score?":
		sheet_input_henrike = sheet.cell(3,2).value
		text = "Henrike's score is {}".format(sheet_input_henrike)
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)
	elif text == "Bot help":
		text = "You can ask me:\n \nTo give points with: Name +1\nWhat someone's score is with: What is Name's score?\nReset everything with: Reset all\n \nPlease note that I am sensitive for capitals"
		url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)
        print("getting updates")


if __name__ == '__main__':
    main()