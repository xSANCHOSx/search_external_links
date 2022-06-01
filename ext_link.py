import os
from bs4 import BeautifulSoup as bs
from datetime import datetime

os.chdir("/Users/sanchos/Desktop/2tg1")
count = 0
start_time = datetime.now()
files = os.listdir(".")
ex_link = []
for root, dirs, files in os.walk('.'):
    for name in files:
        if name != ".DS_Store" and not name.endswith(".xml") and not name.endswith(".jpg") and not name.endswith(".png") \
                and not name.endswith(".gif") and not name.endswith(".GIF"):
            print(name)
            with open(os.path.join(root, name)) as fp:
                soup = bs(fp, 'html.parser')
                all_link = soup.findAll('a')
                for link in all_link:
                    link_href = link.get('href')
                    if link_href is not None:
                        if link_href.startswith(('http://', 'https://')):
                            link_separate_data = link_href.split('/')
                            good_link = str('http://' + link_separate_data[2])
                            ex_link.append(good_link)
                    try:
                        for one in ex_link:
                            link['href'] = link['href'].replace(one, "/")
                    except Exception as e:
                        pass

            with open(os.path.join(root, name), 'w') as file:
                file.write(str(soup))

        ex_link = []

        count += 1
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
