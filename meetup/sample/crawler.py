from selenium import webdriver
import os
import traceback
import time
import datetime
import re

def convert(str) :
    a = re.sub("[\(\[\<].*?[\>\)\]]", "", str)
    b = a.split("\n")[0].strip()
    return b

def fetch(site, br) :

    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M')
    list=[]

    if site == "PPOMPPU":

        br.get('http://m.ppomppu.co.kr/new/#hot_bbs')
        try:
            list = br.find_element_by_id("mainList").find_elements_by_tag_name("li")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try :
                title = str(i.find_element_by_class_name("main_text02").text).replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href"))
                comment_count = str(i.find_element_by_class_name("main_list_comment").text)
                result.append({'title' : title, 'href' : href, 'comment_count' : comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "BOBAE":

        br.get('http://m.bobaedream.co.kr/board/new_writing/best')
        try:
            list = br.find_element_by_class_name("rank").find_elements_by_class_name("info")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_class_name("cont").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str(i.find_element_by_class_name("num").text)
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "RULIWEB":

        br.get('https://m.ruliweb.com/best')
        try:
            list = br.find_element_by_id("board_list").find_elements_by_class_name("title")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_class_name("subject_link").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str(i.find_element_by_class_name("num").text)
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "INVEN":

        br.get('http://m.inven.co.kr/board/powerbbs.php?come_idx=2097')
        try:
            list = br.find_element_by_id("boardList").find_elements_by_class_name("articleSubject")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_class_name("title").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X")
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "SLR":

        br.get('http://m.slrclub.com/l/hot_article')
        try:
            list = br.find_element_by_class_name("list").find_elements_by_class_name("article")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str(i.parent.find_element_by_class_name("cmt2").text)
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "FM":

        br.get('https://m.fmkorea.com/best')
        try:
            list = br.find_element_by_class_name("fm_best_widget").find_elements_by_class_name("li")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_class_name("title").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X")
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)


    if site == "UNIV":

        br.get('http://m.humoruniv.com/board/list.html?table=pds')
        try:
            list = br.find_element_by_id("list_body").find_elements_by_class_name("list_body_href")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_class_name("li").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.get_attribute("href")).strip()
                comment_count = str(i.find_element_by_class_name("ok_num").text).strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)


    if site == "DOGDRIP":
        br.implicitly_wait(10)
        br.get('https://www.dogdrip.net/dogdrip')

        try:
            list = br.find_element_by_class_name("list").find_elements_by_tag_name("li")
        except:
            print("not parsed from the start")

        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)


    if site == "CLIEN":

        br.get('https://m.clien.net/service/group/clien_all?&od=T33')
        try:
            list = br.find_element_by_class_name("content_list").find_elements_by_class_name("list_item")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_class_name("list_subject").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)


    if site == "FOMOS":

        br.get('http://m.fomos.kr/talk/article_list?bbs_id=1')
        try:
            list = br.find_element_by_id("contents").find_elements_by_class_name("ut_item")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()[1:]
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "MLB":
        br.implicitly_wait(5)
        br.get('http://mlbpark.donga.com/mlbpark/b.php?b=bullpen')
        try:
            list = br.find_element_by_class_name("tbl_type01").find_elements_by_tag_name("tr")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_class_name("t_left").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "DDANZI":
        br.implicitly_wait(3)
        br.get('http://www.ddanzi.com/index.php?mid=free&statusList=HOT%2CHOTBEST')
        try:
            list = br.find_element_by_id("list_style").find_elements_by_class_name("title")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)


    if site == "INSTIZ":
        br.implicitly_wait(3)
        br.get('https://www.instiz.net/bbs/list.php?id=pt&srt=3')
        try:
            list = br.find_element_by_id("mainboard").find_elements_by_id("subject")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)



    if site == "YGOSU":
        br.implicitly_wait(3)
        br.get('https://www.ygosu.com/community/real_article')
        try:
            list = br.find_element_by_class_name("bd_list").find_elements_by_class_name("tit")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    if site == "NATE":
        br.implicitly_wait(3)
        br.get('https://m.pann.nate.com/talk/today')
        try:
            list = br.find_element_by_class_name("list").find_elements_by_tag_name("li")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)


    if site == "DC":
        br.implicitly_wait(3)
        br.get('http://gall.dcinside.com/board/lists/?id=hit')
        try:
            list = br.find_element_by_class_name("gall_list").find_elements_by_class_name("gall_tit")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                if "힛갤에 등록된 게시물은 방송에" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)


    if site == "TODAY":
        br.implicitly_wait(3)
        br.get('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')
        try:
            list = br.find_elements_by_class_name("subject")
        except:
            print("not parsed from the start")
        result = []
        for i in list:
            try:
                title = str(i.find_element_by_tag_name("a").text).strip().replace("/","_")
                if "공지" in title :
                    continue
                title = convert(title)
                href = str(i.find_element_by_tag_name("a").get_attribute("href")).strip()
                comment_count = str("X").strip()
                result.append({'title': title, 'href': href, 'comment_count': comment_count, 'site':site, 'timestamp': timestamp})
            except:
                print("error:")
                traceback.print_exc()
        print(result)

    return result

########################################
# ######################################################


