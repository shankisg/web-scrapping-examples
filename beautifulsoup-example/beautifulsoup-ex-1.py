html_doc = """
<html>
	<head>
		<title>BeautifulSoup Example</title>
	</head>
	<body>
	<p class="title">
		<b>BeautifulSoup Example</b>
	</p>

	<p class="parent-text">Quick demo on BeautifulSoup,
	<a href="http://example.com/Text 1" class="sister-text" id="link1">Text 1</a>,
	<a href="http://example.com/Text 2" class="sister-text" id="link2">Text 2</a> and
	<a href="http://example.com/Text 3" class="sister-text" id="link3">Text 3</a>;
	do you like it.</p>

	<p class="parent-text">...</p>
"""
print html_doc
print ""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

print "command: soup.title" 
print soup.title   # <title>BeautifulSoup Example</title>
print ""

print "command: soup.p" 
print soup.p # <p class="title"><b>BeautifulSoup Example</b></p>
print ""

print "command: soup.p['class']" 
print soup.p['class'] # u'title'
print ""

print "command: soup.a" 
print soup.a  # <a class="sister-text" href="http://example.com/Text 1" id="link1">Text 1</a>
print ""

print "command: soup.find_all('a')" 
print soup.find_all('a')
# [<a class="sister" href="http://example.com/Text 1" id="link1">Text 1</a>,
#  <a class="sister" href="http://example.com/Text 2" id="link2">Text 2</a>,
#  <a class="sister" href="http://example.com/Text 3" id="link3">Text 3</a>]
print ""

print "command: soup.find(id='link3')" 
print soup.find(id="link3")
# <a class="sister" href="http://example.com/Text 3" id="link3">Text 3</a>