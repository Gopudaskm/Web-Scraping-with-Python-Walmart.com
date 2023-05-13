import requests
from lxml import html
import json

#Finding the product ID and name from the webpage.

headers = {
    'authority': 'www.walmart.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    'referer': 'https://www.walmart.com/',
    'sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}
proxy="47.98.219.185:8999"
# proxy="186.121.235.66:8080"

response = requests.get('https://www.walmart.com/search?q=laptop', headers=headers,proxies={"http":proxy, "https":proxy})

cookies=response.cookies

tree=html.fromstring(response.text)

product=tree.xpath('//script[@id="__NEXT_DATA__"]//text()')

data=json.loads(product[0])

product_list=data['props']['pageProps']['initialData']['searchResult']['itemStacks'][0]['items']


#Creating a dictionary with key as product ID and value as title of the product.

products={}


for i in product_list:
    temp={}
    if i.get('usItemId') != None:
        temp["Title"]=i.get('name')
        products[i.get('usItemId')]=temp


#Collecting seller information for items and updating the dictionary with that information.
pro_id=products.keys()



for i in pro_id:
    headers = {
        'authority': 'www.walmart.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.8',
        'content-type': 'application/json',
        'device_profile_ref_id': 'v6Z9J4B7HjAQt2Isu52P1dIQ0D1hfRy1GHpq',
        'referer': f'https://www.walmart.com/ip/{i}',
        'sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'traceparent': '00-97712de7758f005a56a0d3fccc8292c1-d6b32cffaacd0d28-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'wm_mp': 'true',
        'wm_page_url': f'https://www.walmart.com/ip/{i}',
        'wm_qos.correlation_id': 'K-pD85Q2jTlqnOB-H4L2vi0vtXVcGpuPblkR',
        'x-apollo-operation-name': 'GetAllSellerOffers',
        'x-enable-server-timing': '1',
        'x-latency-trace': '1',
        'x-o-bu': 'WALMART-US',
        'x-o-ccm': 'server',
        'x-o-correlation-id': 'K-pD85Q2jTlqnOB-H4L2vi0vtXVcGpuPblkR',
        'x-o-gql-query': 'query GetAllSellerOffers',
        'x-o-mart': 'B2C',
        'x-o-platform': 'rweb',
        'x-o-platform-version': 'main-1.69.0-a9377b-0504T2039',
        'x-o-segment': 'oaoh',
    }

    params = {
        'variables': '{"itemId":"'+i+'","isSubscriptionEligible":false}',
    }

    response = requests.get(
        'https://www.walmart.com/orchestra/home/graphql/GetAllSellerOffers/d194b8b5f2b10e2bcef845cf48dad79e8fb95350f21e341c7de17aa2b2a90caf',
        params=params,
        cookies=cookies,
        headers=headers,
        proxies={"http":proxy, "https":proxy},
    )
    
    all_offers=response.json().get('data').get('product').get('allOffers')
    for j in range(len(all_offers)):
        products[i][j+1]=all_offers[j]

with open("Data.json", "w") as f:
    json.dump(products,f,indent=4)

