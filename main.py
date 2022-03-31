import requests
import csv

shopee_url = 'https://shopee.co.id'
keyword = 'baju anak'

headers = {
    'user-agent' : 'chrome',
    'Referer' : f'{shopee_url}search?keyword={keyword}'
}

url = f'https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword={keyword}&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'

datas = []

#API request
req = requests.get(url, headers=headers).json()
items = req['items']
for item in items:
    name = item['item_basic']['name']
    price = item['item_basic']['price']
    sold = item['item_basic']['sold']
    datas.append([name, price, sold])

headers_exel = ['Product Name', 'Price', 'Sold']
writer = csv.writer(open(f'result/Scraping-shopee-{keyword}', 'w', newline=''))

writer.writerow(headers_exel)
for data in datas:
    writer.writerow(data)