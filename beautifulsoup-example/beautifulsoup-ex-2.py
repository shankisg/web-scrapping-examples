import urllib2
from IPython.display import display
from IPython.display import Image
from bs4 import BeautifulSoup as BS

URL = "http://www.flipkart.com/search?q=sony&as=on&as-show=on&otracker=start&as-pos=1_q"
url_ref = urllib2.urlopen(URL)

soup = BS(url_ref.read())
url_ref.close()

for data in soup.find_all('div', class_=" product-unit unit-4  browse-product  "):
    div_data = data.find('div', class_="pu-visual-section")  
    img_data = div_data.find('img')
    img_src = img_data['data-src']
    display(Image(url=img_src))
    print data.find('a', class_="fk-display-block").text
    print img_src