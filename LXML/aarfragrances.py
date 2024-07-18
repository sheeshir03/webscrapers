# Getting fragrance details a simple webscraper using lxml library and requests
import requests
from lxml import html

url = 'https://www.aarfragrances.com/search?collection=true'

while True:
    print("====================================================================")
    print(url)
    response = requests.get(url)
    xmltree = html.fromstring(response.content)

    items = xmltree.xpath('//form[@id="search-form"]//div[@class="col"]')

    for item in items:
        a_tag = item.xpath(".//a[@class='d-block']")[0]
        source_url = a_tag.get("href")
        title = item.xpath(".//h3//a")[0].text_content().strip()
        price = item.xpath(".//div[@class='fs-15']//span")[0].text_content()
        print(source_url, title, price)
    next_page = xmltree.xpath("//li//a[@rel='next']")
    if not next_page:
        print(url, "was the last page")
        break
    next_url = next_page[0].get("href")
    url = next_url
    
    
    
    
    
