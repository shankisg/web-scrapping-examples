import urllib2
from mechanize import Browser
from bs4 import BeautifulSoup as BS
from IPython.display import display
from IPython.display import Image


def get_product_url(item_list):
	"""
	Return the url for each item in item_list from flipkart.
	"""

	url_list = []
	br = Browser() #get the browser instance
	br.set_handle_robots(False) #ignore robot.txt
	br.addheaders = [('User-agent', 'Firefox')] # setting browser agent
	br.open("http://www.flipkart.com/") # open url

	for item in item_list:
		br.select_form(nr=1) #select form using postion, as form name is nor available
		br.form['q'] = item # set item to be searched
		br.submit()
		url_list.append(br.geturl())

	return url_list


def get_products(url_list):
	"""
	Would parse each url in url_list and print the required info.
	"""

	for urls in url_list:
		url_ref = urllib2.urlopen(urls)
		soup = BS(url_ref.read())
		url_ref.close()

		for data in soup.find_all('div', class_=" product-unit unit-4  browse-product  "):
		    div_data = data.find('div', class_="pu-visual-section")  
		    img_data = div_data.find('img')
		    img_src = img_data['data-src']
		    display(Image(url=img_src))
		    print data.find('a', class_="fk-display-block").text
		    print img_src


if __name__ == '__main__':
	item_list = ["htc", "sony", "dell"]
	url_list = get_product_url(item_list)
	get_products(url_list)