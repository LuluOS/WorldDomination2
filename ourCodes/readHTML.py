import codecs
from BeautifulSoup import BeautifulSoup

html_doc = codecs.open("technology.html", 'rb')

#soup = BeautifulSoup(html_doc, 'html.parser')

#print f.read()

parsed_html = BeautifulSoup(html_doc)

#for link in parsed_html.find_all('a'):
#    print(link.get('href'))
print parsed_html.body#.find('div', attrs={'class':'container'}).text