import telepot, time, os, json
import requests
from bs4 import BeautifulSoup

with open('token.json', 'r', encoding='UTF-8') as config: # read config file
    data = config.read()
    configData = json.loads(data)
    token = configData['Bot']['token']

userId = '698241176'
bot = telepot.Bot(token)

bot.sendMessage(userId, "안녕하세요 저는 와이즈 입니다!")

status = True

def isMeaning(word2find):
    url = "http://endic.naver.com/search.nhn?query=" + word2find
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    try:
        meaning = soup.find('dl', {'class':'list_e2'}).find('dd').find('span', {'class':'fnt_k05'}).get_text() +"\n"
        return meaning
    except:
        return '그런 단어는 없습니다 ㅠㅠ'

def handle(msg):
    content, chat, id = telepot.glance(msg)
    print(content, chat, id)
    if content == 'text':
        if msg[content] == '/migrate':
            print('migrate')
            bot.sendMessage(id, 'migrate fuction activated')
            # migrate
            exit()
        word = msg[content]
        wordMeaing = isMeaning(word)  
        print(wordMeaing)
        bot.sendMessage(id, isMeaning(word))
    else:
        bot.sendMessage(id, '아 뭐래')

bot.message_loop(handle)

while(True):
    time.sleep(10)