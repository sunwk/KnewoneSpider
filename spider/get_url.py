from spider import *


url = 'https://knewone.com/things'

tag_info_collection = db['tag_info']

page = requests.get(url)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'lxml')
tag_list = soup.select('.nav .dropdown-menu li > a')


def main():
    for tag in tag_list:
        time.sleep(0.5)
        tag_name = tag.select('em')[0].string
        tag_url = urljoin(url, tag['href'])
        tag_info = {
            'tag_name': tag_name,
            'tag_url': tag_url
        }
        print(tag_info)
        tag_info_collection.insert(tag_info)


if __name__ == '__main__':
    main()
