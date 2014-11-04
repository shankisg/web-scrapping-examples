from mechanize import Browser

br = Browser() #get the browser instance
br.set_handle_robots(False) #ignore robot.txt
br.addheaders = [('User-agent', 'Firefox')] # setting browser agent
br.open("http://www.google.co.in/") # open url
br.select_form('f') #select form
br.form['q'] = 'python' #set input field data to be searched
br.submit()

for link in br.links():
	print link.text
