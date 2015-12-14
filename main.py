from bs4 import BeautifulSoup #""" http://www.crummy.com/software/BeautifulSoup/bs4/doc/ """
import requests

#############################################################################################################
#""" Functions """
#""" function to check if a substring is part of a string """
def checkSubInStr(substring, string):
	if (substring in string):
		return True
	else:
		return False

#""" function to check if a given word is part of a phrase """
def checkWordInPhrase(givenWord, phrase):
	words = phrase.split()  #""" split the sentence into individual words """

	for i in range(len(words)):
		if (givenWord.lower() ==  words[i].lower()):  #""" see if one of the words in the sentence is the word we want """
			return True

	return False

#""" function that returns the index of the position from the string in the phrase """
def indexStr(phrase, string):
	#""" string = "href" #link starts after 2 more char """
    index = 0

    if (string in phrase):
        letter = string[0]
        #""" loop to navagate in the phrase """
        for char in phrase:
      		#""" if char is a substring of letter """
            if (char == letter):
            	#""" if the sublist from index to (index+len(string)) contains the string """
                if (phrase[index : (index+len(string))] == string):
                    return index #""" return the index """
 
            index += 1

    return -1 #""" if the string is not in the phare  """  


#""" function that returns the link from the entire tag """  
def getLink(tag, position):
	char = tag[position] #""" char is the first character of the link """

	link = []

	#""" keep copying char by char to the link until find a quote """
	while (char != "\""):
		#print char
		link.append(char)
		position += 1
		char = tag[position]

	#""" transform link in a string and atribute it to href """
	href = ''.join(link)

	string = "http://"
	#""" if is a link return it """
	if (string in href):
		return href
	#""" if is not a link return -1 (error) """
	else:
		return -1

#""" function that returns the title from the entire tag """  
def getTitle(tag):
	index = 0
	
	text = []

	char = tag[index]

	#""" find the position of '>' on the tag """
	while (char != ">"):
		index += 1
		char = tag[index]
	
	#""" pick the next char """
	index += 1
	char = tag[index]

	#""" add each char in the text until find a '<' """
	while (char != "<"):
		text.append(char)
		index += 1
		char = tag[index]

	#""" transform text in a string and atribute it to title """
	title = ''.join(text)
	return title

#""" function that returns the list b but without the elements that contained in a (difference between two lists) """
#""" http://stackoverflow.com/questions/3462143/get-difference-between-two-lists """
def listB_A(b, a):
	return list(set(b) - set(a))

#############################################################################################################
#""" _Main_ """
if __name__ == '__main__':
	givenWord = raw_input("What do you want to search for? ") #""" input given word (to search) """

	webPages = [] #"""  is a list of url that we want to check """

	intersection = [] #"""  is a list of the html tags (<a>) that contains the classes 'title may-blank' """

	links = [] #""" is a list of links that contains the given word """
	recommended = [] #""" is a list of links that contains similar words with the given word """

	webPages.append(requests.get("http://" +"www.reddit.com"))
	webPages.append(requests.get("http://" +"www.reddit.com/r/technology/"))

	pagesNumbers = len(webPages) #""" number of webPages """

	#""" loop to search into all pages """
	for i in range(pagesNumbers):
		data = webPages[i].text
		soup = BeautifulSoup(data,"lxml")
		
		#""" returns all tags that contains the class 'may-blank' to the list called mayblank """
		mayblank = soup.findAll('a', attrs={'class':'may-blank'}) #""" returns a list with all class called 'may-blank' """

		#""" size of the list mayblank """
		sizeMB = len(mayblank)

		#""" loop to check if in each mayblank[i] has the word 'title' to store the tags that contains 'title may-blank' """
		for j in range(sizeMB):
			if (checkSubInStr("title", str(mayblank[j])) == True): #""" if the tag contains the class 'title may-blank' """
				intersection.append(str(mayblank[j])) #""" add the tag to the intersection list """

	#print ("intersection: "),
	#print intersection

	sizeInter = len(intersection)

	#""" loop to check if in each intersection[i] has the given word to store the links """
	for i in range(sizeInter):
		if (checkWordInPhrase(givenWord, str(intersection[i])) == True): #""" if the tag contains the given word """
			links.append(str(intersection[i])) #""" add the tag to the links list """

		if (checkSubInStr(givenWord, str(intersection[i])) == True): #""" if the tag contains a similar word """
			recommended.append(str(intersection[i])) #""" add the tag to the links list """

	href = [] #""" is a list of just the href of the links """
	titleL = [] #""" is a list of the title of the links """
	recom = [] #""" is a list of just the href of the recommended """
	titleR = [] #""" is a list of the title of the recommended """

	#""" because all the time is going to be with this pattern """
	#""" [<a class="title may-blank " href="] the link start in """
	#""" the position 33 of the tag """
	if ((len(links) != 0) or (len(recommended) != 0)):
		#""" if there is a link or more save the title(s) and the link(s) """
		if (len(links) != 0):
			for i in range(len(links)):
				titleL.append(getTitle(links[i]))
				if (getLink(links[i], 34) != -1):
					href.append(getLink(links[i], 34))

			#""" output: title and href """
			if (len(href) != 0):
				print ("Links: ")
				for i in range(len(href)):
					print ("> %s: \n\t%s\n" %(titleL[i],href[i]))

		#""" if there is a recommended or more save the title(s) and the recommended(s) """
		if (len(recommended) != 0):
			for i in range(len(recommended)):
				titleR.append(getTitle(recommended[i]))
				if (getLink(recommended[i], 34) != -1):
					recom.append(getLink(recommended[i], 34))

			#""" take out the repeated links """
			if (len(href) != 0):
				recom = listB_A(recom, href)

			#""" output: title and recom """
			if (len(recom) != 0):
				print ("Recommended: ")
				for i in range(len(recom)):
					print ("> %s: \n\t%s\n" %(titleR[i],recom[i]))
	else:
		print ("Sorry, but nothing on these pages match with your given word!")

#############################################################################################################