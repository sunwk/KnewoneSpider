from spider.get_url import main as get_url
from spider.urls_of_url import main as urls_of_url
from spider.product_items import main as product_items


def main():
    get_url()
    urls_of_url()
    product_items()

if __name__ == '__main__':
    main()