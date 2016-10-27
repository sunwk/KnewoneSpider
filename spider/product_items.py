from spider import *

tag_info_2 = db['tag_info_2']
item_info = db['items_info']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
    'cookies': 'gr_user_id=d4ae1184-0181-4615-abd7-e939a3e06ab7; _ga=GA1.2.1906898280.1475571862; _gat=1; Hm_lvt_b44696b80ba45a90a23982e53f8347d0=1475572751,1475844435,1476511018,1477071709; Hm_lpvt_b44696b80ba45a90a23982e53f8347d0=1477125913; gr_session_id_e7b7e334c98d4530928513e7439f9ed2=8d06d4a5-877a-4f40-9577-4074d40c27f6; _knewone_v2_session=Z2pzVDZ4QmJKUGgzMFRHSUtad0JRYWdlcEt3VjJXOW9nNGJSanNlaDQ1Z0x2TVE1ZUNRT0hJeU5IVXpZak5WekFCVWtSakJ0elhNNExLK05ROFlQYmVoV1Y0ZXAzZWZrRlpTOEpYcHA4eFV1ZWlRZFBOTGZDZjRDQk1xYWtZUTE2ZCtNbHlPOU55Qzl0eTVWY1AwQzliamxTeVRHNmJPSVJhUnIwTGxhRDR2ODJYTGprVE5HTVpiR3M2Q3NMTEIybjEraU9rWXpEb3FkTFh4eEw5TDFCQndVZk52Mys5MzhMRmNBbmc4TXhzelZJaWhIVjJIcElZRjdHZnEwa2JGdy0tT3l6TEdBU3o1QWx0UysxMGk3c05oQT09--5042267fb64a47609b5a4ecef53c560329e98077',
    'Connection': 'keep-alive'
}

proxy_list = [
    # '106.39.160.121:80',
    # '122.116.102.113:3128',
    # '115.28.101.22:3128',
    # '49.86.122.134:8088',
    # '113.105.185.10:3128',
    # '123.125.122.205:80',
    # '112.112.70.115:80',
    '119.53.122.70:8118',
    '220.184.221.242:8118',
    '222.181.198.143:1080',
    '121.31.50.174:8123',
    '103.239.247.103:8080',
]


def info_from_items(items):
    info_list = []
    for item in items:
        url = 'https://knewone.com/things'
        product_url = urljoin(url, item.select('header > a')[0]['href'])
        product_name = item.select('h4 > a')[0].string
        product_likes = item.select('.interactions > .fancy_button .fanciers_count')[0].string
        product_img = item.select('img')[0]['src']
        data = {
            'product_url': product_url,
            'product_name': product_name,
            'product_likes': product_likes,
            'product_img': product_img,
        }
        print(data)
        info_list.append(data)
    return info_list


def main():
    tag_info = list(tag_info_2.find())
    for i in tag_info[7:]:
        data_list = []
        tag_name = i.get('tag_name', '')
        url_list = i.get('tag_url', '')
        for url in url_list:
            print(url)
            # 随机获取代理ip
            proxy_ip = random.choice(proxy_list)
            proxies = {'http': proxy_ip}
            print('proxies:', proxies)

            time.sleep(random.uniform(0, random.randint(1, 3)))
            page = requests.get(url, headers=headers, proxies=proxies)
            page.encoding = 'utf-8'
            soup = BeautifulSoup(page.text, 'lxml')
            items = soup.select('.thing')
            if len(items) == 0:
                break
            info_list = info_from_items(items)
            data_list.extend(info_list)
        print('准备插入数据库', len(data_list), tag_name)
        if len(data_list) != 0:
            item_info.insert({
                'tag_name': tag_name,
                'product_data': data_list
            })
        else:
            pass


if __name__ == '__main__':
    main()
