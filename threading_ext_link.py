import os
from threading import Thread
from bs4 import BeautifulSoup as bs
from datetime import datetime

def search_replace():
    os.chdir("/Users/sanchos/Desktop/2tg1")
    count = 0
    start_time = datetime.now()
    files = os.listdir(".")
    ex_link = []
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name != ".DS_Store" and not name.endswith(".xml") and not name.endswith(".jpg") and not name.endswith(".png") \
                    and not name.endswith(".gif") and not name.endswith(".GIF"):
                with open(os.path.join(root, name)) as fp:
                    soup = bs(fp, 'html.parser')
                    count_links = 0
                    all_link = soup.findAll('a')
                    for link in all_link:
                        link_href = link.get('href')
                        if link_href is not None:
                            if link_href.startswith('http://'):
                                link_separate_data = link_href.split('/')
                                good_link = str('http://' + link_separate_data[2])
                                ex_link.append(good_link)
                            if link_href.startswith('https://'):
                                link_separate_data = link_href.split('/')
                                good_link = str('https://' + link_separate_data[2])
                                ex_link.append(good_link)
                                count_links += 1
                        try:
                            for one in ex_link:
                                link['href'] = link['href'].replace(one, "/")
                                if link['href'].startswith('//'):
                                    link['href'] = link['href'].replace('//', "/")
                        except Exception as e:
                            pass

                if ex_link:
                    with open(os.path.join(root, name), 'w') as file:
                        file.write(str(soup))
                print("Файл № " + str(count) + " ссылок: " + str(count_links))
            ex_link = []

            count += 1
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    print(count)
th = Thread(target=search_replace, args=())
th.start()