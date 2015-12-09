from bs4 import BeautifulSoup
import requests
r = []
content = []
# http://stackoverflow.com/questions/11331071/get-class-name-and-contents-using-beautiful-soup
def match_class(target):                                                        
    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
    return do_match   

#url=raw_input("Enter a website to extract the URL's from:")

r.append(requests.get("http://" +"www.reddit.com"))
r.append(requests.get("http://" +"www.reddit.com/r/technology"))

#search = raw_input("")

#content = soup.findAll('a', attrs={'class':'may-blank'})


for x in range(len(r)):

	data=r[x].text
	soup=BeautifulSoup(data)
	
	#for link in soup.find_all('a'):
	content = soup.findAll('a', attrs={'class':'may-blank'})

	#temp = BeautifulSoup(content)
	#content2 = content.findAll('a', attrs={'class':'title'})
	print ("\n")
	print content
	 	# print soup.findAll(match_class("title may-blank"))


