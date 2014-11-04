import urllib2
from IPython.display import display
from IPython.display import Image
from bs4 import BeautifulSoup as BS

URL = "http://www.flipkart.com/search?q=htc+mobiles&as=off&as-show=off&otracker=start"
url_ref = urllib2.urlopen(URL)

soup = BS(url_ref.read())
url_ref.close()

for data in soup.find_all('div', class_=" product-unit unit-4  browse-product  "):
	img_src = data.select('div.pu-visual-section img')[0]['data-src']
	display(Image(url=img_src))
	print data.select('a.fk-display-block')[0].text
	print img_src
    
