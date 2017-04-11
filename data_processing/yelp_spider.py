import requests
import os
from bs4 import BeautifulSoup

WIDTH = "226"
IMAGES_PER_PAGE = 30
REST_PER_PAGE = 10
s = requests.session()


def find_page_number(webpage):
    num_pages = webpage.find("div", {"class": "page-of-pages"})
    if num_pages:
        num_pages = int(str(num_pages).split("Page 1 of ")[1].strip("</div>"))
    else:
        num_pages = 1
    return num_pages


def fetch_restaurant(url):
    links = []
    r = s.get(url)
    webpage = BeautifulSoup(r.content, 'lxml')
    num_pages = find_page_number(webpage)

    for i in range(1, num_pages + 1):
        for link in webpage.find_all('img'):
            source = str(link.get('src'))
            if str(link.get('width')) == WIDTH:
                links.append(source)
        next_page = url + "?start=" + str(i * IMAGES_PER_PAGE)
        r = s.get(next_page)
        webpage = BeautifulSoup(r.content, 'lxml')
    return links


def save_file(filename, link):
    r = s.get(link)
    f = open(filename, 'wb')
    f.write(r.content)
    f.close()


def search_city(city_url):
    restaurants = []

    r = s.get(city_url)
    webpage = BeautifulSoup(r.content, 'lxml')
    num_pages = find_page_number(webpage)

    new_city_url = "https://en.yelp.com.hk/search?find_loc=urbana&start="
    for i in range(1, num_pages + 1):
        for link in webpage.find_all('a'):
            if str(link.get('data-analytics-label')) == "biz-name":
                restaurants.append(str(link.get('href')))
        next_page = new_city_url + str(i * REST_PER_PAGE)
        r = s.get(next_page)
        webpage = BeautifulSoup(r.content, 'lxml')

        print("finish searching restaurant urls on page: {}/{}".format(i, num_pages))
    return restaurants


def save_from_url(url):
    restaurants = search_city(url)
    fout = open("restaurant_url.txt", "w")
    for item in restaurants:
        fout.write("%s\n" % item)
    fout.close()
    print("============ finish writing restaurant URLs ============")
    return restaurants


def save_from_file(filename):
    return open(filename).readlines()


def main():
    restaurants = save_from_file("restaurant_url.txt")

    total_num_restaurants = len(restaurants)
    current_restaurant = 0
    for restaurant in restaurants:
        current_restaurant += 1
        print("save photos progress: {}/{}".format(current_restaurant, total_num_restaurants))

        folder_name = restaurant[5:]
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        else:
            print("find restaurant exists!")
            continue

        biz_photo_url = "https://en.yelp.com.hk/biz_photos/" + restaurant[5:]
        urls = fetch_restaurant(biz_photo_url)

        counter = 0
        for link in urls:
            filename = folder_name + '/' + str(counter) + '.jpg'
            save_file(filename, link)
            counter += 1


if __name__ == "__main__":
    main()

