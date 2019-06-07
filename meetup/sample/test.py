
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from random import shuffle
import urllib.request
import hashlib
from random import randint
from selenium import webdriver
import time
import datetime
import re
import random
import os
import traceback
from datetime import datetime

print('start')

list = [
    "PPOMPPU"
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
    phantomjs_path = "C://webdriver//chromedriver.exe"
    # phantomjs_path = "/usr/lib/chromium-browser/chromedriver"

    # br = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    br = webdriver.Chrome(executable_path=phantomjs_path, service_log_path=os.path.devnull, chrome_options=options)
    return br



# title 등에서 나오는 지저분한 형태 다 교체
def convert(str) :
    a = re.sub("[\(\[\<].*?[\>\)\]]", "", str)
    b = a.split("\n")[0].strip()
    return b



# 사이트별 특화로직
def __get_content(site, url, title) :

    br = prepareWebDriver()
    br.get(url)

    image_list = []  # href만을 따온다.
    storage_image_list = []  # 이미지 storage 경로를 따온다.
    content_text = ""

    def ___get_image_content(dom) :
        image_href = dom.get_attribute("src")  # 이미지의 링크를 따와서
        image_list.append(image_href)
        upload_storage_image_key = __upload_image_storage(image_href, title)
        storage_image_list.append(upload_storage_image_key)

    try :

        content = ""
        content_text = ""

        if site == "PPOMPPU": # 교체 ---------------------------------------
            content = br.find_element_by_class_name("cont")

        if site == "BOBAE":
            content = br.find_element_by_class_name("article-body")

        if site == "RULIWEB":
            content = br.find_element_by_class_name("view_content")

        if site == "INVEN":
            content = br.find_element_by_class_name("articleContent")

        if site == "SLR":
            content = br.find_element_by_id("userct")

        if site == "FM":
            content = br.find_element_by_class_name("rb_body")

        if site == "UNIV":
            content = br.find_element_by_class_name("wrap_body")

        if site == "DOGDRIP":
            content = br.find_element_by_id("article_1")

        if site == "CLIEN":
            content = br.find_element_by_class_name("post_article")

        if site == "FOMOS":
            content = br.find_element_by_class_name("view_cont")

        if site == "MLB":
            content = br.find_element_by_class_name("ar_txt")

        if site == "DDANZI":
            content = br.find_element_by_class_name("read_content")

        if site == "INSTIZ":
            content = br.find_element_by_id("memo_content_1")

        if site == "YGOSU":
            content = br.find_element_by_class_name("article")

        if site == "NATE":
            content = br.find_element_by_class_name("content")

        if site == "DC":
            content = br.find_element_by_class_name("thum-txt")

        if site == "TODAY":
            content = br.find_element_by_class_name("viewContent")

        content_text = content.text
        for img in content.find_elements_by_tag_name("img"):
            ___get_image_content(img)

    except :
        print("error:")
        traceback.print_exc()

    finally:
        br.quit()

    return content_text, image_list, storage_image_list

def __upload_image_storage(href,title) :
    st = storage.bucket()

    # 0~100사이의 대충 아무 파일이나 잡고 저장한다.
    outfile = str(randint(0, 100))
    urllib.request.urlretrieve(href, outfile)

    imageKey = hashlib.sha1(title.encode("utf-8")).hexdigest() + str(time.time())

    # 그리고 이미지 키에 따라서 저장한다.
    blob = st.blob('parsed_content/' + imageKey)

    with open(outfile, 'rb') as my_file :
        blob.upload_from_file(my_file)

    return imageKey

# 사이트별 특화로직
def fetch(site, br) :

    timestamp = datetime.now()

    content_candidate =[]
    result = []
    content = []

    try:
        if site == "PPOMPPU": # 교체 --------------------------------------------
            br.get('http://m.ppomppu.co.kr/new/#hot_bbs')
            content_candidate = br.find_element_by_id("mainList").find_elements_by_tag_name("li")

        if site == "BOBAE" :
            br.get('http://m.bobaedream.co.kr/board/new_writing/best')
            content_candidate = br.find_element_by_class_name("rank").find_elements_by_class_name("info")

        if site == "RULIWEB" :
            br.get('https://m.ruliweb.com/best')
            content_candidate = br.find_element_by_id("board_list").find_elements_by_class_name("title")

        if site == "INVEN" :
            br.get('http://m.inven.co.kr/board/powerbbs.php?come_idx=2097')
            content_candidate = br.find_element_by_id("boardList").find_elements_by_class_name("articleSubject")

        if site == "SLR" :
            br.get('http://m.slrclub.com/l/hot_article')
            content_candidate = br.find_element_by_class_name("list").find_elements_by_class_name("article")

        if site == "FM" :
            br.get('https://m.fmkorea.com/best')
            content_candidate = br.find_element_by_class_name("fm_best_widget").find_elements_by_class_name("li")


        if site == "UNIV" :
            br.get('http://m.humoruniv.com/board/list.html?table=pds')
            content_candidate = br.find_element_by_id("list_body").find_elements_by_class_name("list_body_href")

        if site == "DOGDRIP":
            br.get('https://www.dogdrip.net/dogdrip')
            content_candidate = br.find_element_by_class_name("list").find_elements_by_tag_name("li")

        if site == "CLIEN":
            br.get('https://m.clien.net/service/group/clien_all?&od=T33')
            content_candidate = br.find_element_by_class_name("content_list").find_elements_by_class_name("list_item")

        if site == "FOMOS":
            br.get('http://m.fomos.kr/talk/article_list?bbs_id=1')
            content_candidate = br.find_element_by_id("contents").find_elements_by_class_name("ut_item")

        if site == "MLB":
            br.get('http://mlbpark.donga.com/mp/best.php?b=bullpen')
            content_candidate = br.find_element_by_class_name("tbl_type01").find_elements_by_tag_name("tr")

        if site == "DDANZI":
            br.get('http://www.ddanzi.com/index.php?mid=free&statusList=HOT%2CHOTBEST')
            content_candidate = br.find_element_by_id("list_style").find_elements_by_class_name("title")

        if site == "INSTIZ":
            br.get('https://www.instiz.net/bbs/list.php?id=pt&srt=3')
            content_candidate = br.find_element_by_id("mainboard").find_elements_by_id("subject")

        if site == "YGOSU":
            br.get('https://m.ygosu.com/board/real_article')
            content_candidate = br.find_element_by_class_name("bd_list").find_elements_by_class_name("tit")

        if site == "NATE":
            br.get('https://m.pann.nate.com/talk/today')
            content_candidate = br.find_element_by_class_name("list").find_elements_by_tag_name("li")

        if site == "DC":
            br.get('https://m.dcinside.com/board/hit')
            content_candidate = br.find_element_by_class_name("gall_list").find_elements_by_class_name("gall_tit")

        if site == "TODAY":
            br.get('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')
            content_candidate = br.find_elements_by_class_name("subject")



    except:
        print("not parsed from the start")

    for i in content_candidate:
        try :

            href = str(i.find_element_by_tag_name("a").get_attribute("href"))
            key = str(time.time()) + "." + str(random.randint(1 ,10000))
            title = ""

            if site == "PPOMPPU" : # 교체 -------------------------------------
                title = str(i.find_element_by_class_name("main_text02").text).replace("/", "_")

            if site == "BOBAE":
                title = str(i.find_element_by_class_name("cont").text).strip().replace("/","_")

            if site == "RULIWEB":
                title = str(i.find_element_by_class_name("subject_link").text).strip().replace("/","_")

            if site == "INVEN":
                title = str(i.find_element_by_class_name("title").text).strip().replace("/","_")

            if site == "SLR":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "FM":
                title = str(i.find_element_by_class_name("title").text).strip().replace("/","_")

            if site == "UNIV":
                title = str(i.find_element_by_class_name("li").text).strip().replace("/","_")

            if site == "DOGDRIP":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "CLIEN":
                title = str(i.find_element_by_class_name("list_subject").text).strip().replace("/","_")



            if site == "FOMOS":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "MLB":
                title = str(i.find_element_by_class_name("t_left").text).strip().replace("/","_")

            if site == "DDANZI":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "INSTIZ":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "YGOSU":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "NATE":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "DC":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if site == "TODAY":
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")

            if "공지" in title or title == "" :
                continue

            title = convert(title)

            text, image, storage_source = __get_content(site, href, title) # text 와 image의 링크 및 image source파일 (storage에 저장된거) 모두를 빼온다.


            db.collection(u'posts_summary').document(title).create({'title' : title, 'href' : href, 'comment_count' : 0, 'site' :site, 'timestamp': timestamp, 'key' : key})
            db.collection(u'posts_content').document(title).create({'key' : key, 'text' : text, 'image' : image , 'timestamp': timestamp, 'title':title, 'storage_source' : storage_source  })

        except:
            print("error:")
            traceback.print_exc()
    print(result)

    return result, content

# cred = credentials.Certificate("/home/pi/commo/commo/python/commo-d07de-firebase-adminsdk-1vlkw-8ba45418c0.json")
cred = credentials.Certificate("commo-d07de-firebase-adminsdk-1vlkw-8ba45418c0.json")

firebase_admin.initialize_app(cred, {
    'projectId': 'commo-d07de',
    'storageBucket' : 'commo-d07de.appspot.com'
})

db = firestore.client()

br = prepareWebDriver()

result_list = []
content_list = []

for site in list :
    tup = fetch(site, br)

br.quit()


