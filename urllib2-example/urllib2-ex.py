import urllib2
url_ref = urllib2.urlopen("https://www.python.org/") # Getting instance of url

print url_ref.msg # OK
print url_ref.code # 200
print url_ref.url # https://www.python.org/
print url_ref.read() # print the html content if the page
url_ref.close() # close the url 