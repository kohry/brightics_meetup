import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import crawler
from random import shuffle
from selenium import webdriver
import os

print('start')

list = [
"PPOMPPU",
"BOBAE",
"RULIWEB",
"INVEN",
"SLR",
"FM",
"UNIV",
"DOGDRIP",
"CLIEN",
"FOMOS",
"MLB",
"DDANZI",
"INSTIZ",
"YGOSU",
"NATE",
"DC",
"TODAY"
]

def prepareWebDriver() :
    # phantomjs_path = "C://webdriver//chromedriver.exe"
    phantomjs_path = "/usr/lib/chromium-browser/chromedriver"

    # br = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    br = webdriver.Chrome(executable_path=phantomjs_path, service_log_path=os.path.devnull, chrome_options=options)
    return br

cred = credentials.Certificate("/home/pi/commo/commo/python/commo-d07de-firebase-adminsdk-1vlkw-8ba45418c0.json")
# cred = credentials.Certificate("commo-d07de-firebase-adminsdk-1vlkw-8ba45418c0.json")

firebase_admin.initialize_app(cred, {
  'projectId': 'commo-d07de',
})

db = firestore.client()

br = prepareWebDriver()

result_list = []

for site in list :
    for post in crawler.fetch(site,br) :
        result_list.append(post)

shuffle(result_list)

for post in result_list:
    doc_ref = db.collection(u'posts').document(post['title'])
    try :
        doc_ref.create(post)
    except :
        pass
br.quit()


