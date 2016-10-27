from spider import *

tag_info = db['tag_info']
tag_info_2 = db['tag_info_2']


def main():
    for i in tag_info.find():
        tag_url = i.get('tag_url', '')
        tag_name = i.get('tag_name', '')
        url_list = [tag_url + '?page={}'.format(i) for i in range(1000)]
        print(url_list)
        data = {
            'tag_name': tag_name,
            'tag_url': url_list,
        }
        tag_info_2.insert(data)


if __name__ == '__main__':
    main()