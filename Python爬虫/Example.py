
#2020.03.26第一章#
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
print(bsObj.html.body.h1)
print(bsObj.body.h1)
print(bsObj.html.h1)

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title
if __name__ == "__main__":
	title = getTitle("http://www.pythonscraping.com/pages/page1.html")
	if title == None:
		print("Title could not be found!")
	else:
		print(title)

#2020.03.26第二章#
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class" : "green"})
for name in nameList:
	print(name.get_text())
nameList = bsObj.findAll("span", {"class" : {"red", "green"}})
for name in nameList:
	print(name.get_text())
nameList = bsObj.findAll(text = "the prince")
print(len(nameList))
allText = bsObj.findAll(id = "text")
print(allText[0].get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for child in bsObj.find("table", {"id" : "giftList"}).children:
	print(child)
for descendant in bsObj.find("table", {"id" : "giftList"}).descendants:
	print(descendant)

for sibling in bsObj.find("table", {"id" : "giftList"}).tr.next_siblings:
	print(sibling)

print(bsObj.find("img", {"src" : "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

images = bsObj.findAll("img", {"src" : re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
	print(image["src"])

#2020.03.26第三章#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
	if "href" in link.attrs:
		print(link.attrs["href"])

for link in bsObj.find("div", {"id" : "bodyContent"}).findAll("a", 
									href = re.compile("^(/wiki/)((?!:).)*$")):
	if "href" in link.attrs:
		print(link.attrs["href"])

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org" + articleUrl)
	bsObj = BeautifulSoup(html)
	return bsObj.find("div", {"id" : "bodyContent"}).findAll("a", 
									href = re.compile("^(/wiki/)((?!:).)*$"))
if __name__ == "__main__":
	links = getLinks("/wiki/Kevin_Bacon")
	while len(links) > 0:
		newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
		print(newArticle)
		links = getLinks(newArticle)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org" + pageUrl)
	bsObj = BeautifulSoup(html)
	for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
		if "href" in link.attrs:
			if link.attrs["href"] not in pages:
				newPage = link.attrs["href"]
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)
if __name__ == "__main__":
	getLinks("")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	for link in bsObj.findAll("a", href = re.compile("^(/|.*" + includeUrl + ")")):
		if link.attrs["href"] is not None:
			if link.attrs["href"] not in internalLinks:
				internalLinks.append(link.attrs["href"])
	return internalLinks
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
		if link.attrs["href"] is not None:
			if link.attrs["href"] not in externalLinks:
				externalLinks.append(link.attrs["href"])
	return externalLinks
def splitAddress(address):
	addressParts = address.replace("http://", "").split("/")
	return addressParts
def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bsObj = BeautifulSoup(html)
	externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
	print(externalLinks)
	if len(externalLinks) == 0:
		internalLinks = getInternalLinks(startingPage)
		return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
	else:
		return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink("http://oreilly.com")
	print("随机外链是: " + externalLink)
	followExternalOnly(externalLink)

if __name__ == "__main__":
	followExternalOnly("http://oreilly.com")

allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl)
	bsObj = BeautifulSoup(html)
	internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
	externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			print(link)
			allIntLinks.add(link)
			getAllExternalLinks(link)

if __name__ == "__main__":
	getAllExternalLinks("http://oreilly.com")


#2020.03.27第四章#
import json
from urllib.request import urlopen

def getCountry(ipAddress):
	response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode("utf-8")
	print(response)
	responseJson = json.loads(response)
	return responseJson.get("country_code")
if __name__ == "__main__":
	print(getCountry("50.78.253.58"))

import json
jsonString = {"arrayOfNums" : [{"number" : 0}, {"number" : 1}, {"number" : 2}], 
			"arrayOfFruits" : [{"fruit" : "apple"}, {"fruit" : "banana"}, {"fruit" : "pear"}]}
jsonString = str(jsonString)
print(jsonString)
jsonObj = json.loads(jsonString)
print(jsonObj)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number") + jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bsObj = BeautifulSoup(html)
	return bsObj.find("div", {"id":"bodyContent"}).findAll("a", 
				href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
	#Format of history pages is: http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
	pageUrl = pageUrl.replace("/wiki/", "")
	historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
	print("history url is: "+historyUrl)
	html = urlopen(historyUrl)
	bsObj = BeautifulSoup(html)
	#finds only the links with class "mw-anonuserlink" which has IP addresses instead of usernames
	ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList

def getCountry(ipAddress):
	try:
		response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
	except HTTPError:
		return None
	responseJson = json.loads(response)
	return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
	for link in links:
		print("-------------------") 
		historyIPs = getHistoryIPs(link.attrs["href"])
		for historyIP in historyIPs:
			country = getCountry(historyIP)
			if country is not None:
				print(historyIP+" is from "+country)

	newLink = links[random.randint(0, len(links)-1)].attrs["href"]
	links = getLinks(newLink)


#2020.03.27第五章#
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a", {"id" : "logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"
def getAbsoluteURL(baseUrl, source):
	if source.startswith("http://www."):
		url = "http://" + source[11:]
	elif source.startswith("http://"):
		url = source
	elif source.startswith("www."):
		url = source[4:]
		url = "http://" + url
	else:
		url = baseUrl + "/" + source
	if baseUrl not in url:
		return None
	return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
	path = absoluteUrl.replace("www.", "")
	path = path.replace(baseUrl, "")
	path = downloadDirectory + path
	directory = os.path.dirname(path)
	if not os.path.exists(directory):
		os.makedirs(directory)
	return path
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src = True)
for download in downloadList:
	fileUrl = getAbsoluteURL(baseUrl, download["src"])
	if fileUrl is not None:
		print(fileUrl)
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))

import csv
csvFile = open("./test.csv", "w+")
try:
	writer = csv.writer(csvFile)
	writer.writerow(("number", "number plus 2", "number times 2"))
	for i in range(10):
		writer.writerow((i, i + 2, i * 2))
finally:
	csvFile.close()

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html)
table = bsObj.findAll("table", {"class" : "wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("./editors.csv","wt", newline = " ", encoding = "utf-8")
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
		for cell in row.findAll(["td", "th"]):
			csvRow.append(cell.get_text())
			writer.writerow(csvRow)
finally:
	csvFile.close()

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
	msg = MIMEText(body)
	msg["Subject"] = "An Email Alert"
	msg["From"] = "ryan@pythonscraping.com"
	msg["To"] = "webmaster@pythonscraping.com"
s = smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()
bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bsObj.find("a", {"id" : "answer"}).attrs["title"] == "NO"):
	print("It is not Christmas yet.")
	time.sleep(3600)
bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")

#第六章2020.03.30#
from urllib.request import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())

from urllib.request import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read(), "utf-8"))

from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id" : "mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")

from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii", "ignore")
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
for row in csvReader:
	print(row)

dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
	print(row)

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
def readPDF(pdfFile):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, laparams = laparams)
	process_pdf(rsrcmgr, device, pdfFile)
	device.close()
	content = retstr.getvalue()
	retstr.close()
	return content
pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read("word/document.xml")
wordObj = BeautifulSoup(xml_content.decode("utf-8"))
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
	print(textElem.text)

#第七章2020.04.01#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
def ngramsOne(input, n):
	input = input.split(" ")
	output = []
	for i in range(len(input) - n + 1):
		output.append(input[i:i + n])
	return output
def ngramsTwo(input, n):
	content = re.sub("\n+", " ", content)
	content = re.sub(" +", " ", content)
	content = bytes(content, "utf-8")
	content =content.decode("ascii", "ignore")
	print(content)
	input = input.split(" ")
	output = []
	for i in range(len(input) - n + 1):
		output.append(input[i : i + n])
	return output

if __name__ == "__main__":
	html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
	bsObj = BeautifulSoup(html)
	content = bsObj.find("div", {"id" : "mw-content-text"}).get_text()
	ngramsOne = ngramsOne(content, 2)
	ngramsTwo = ngramsTwo(content, 2)
	print(ngramsOne)
	print("2-grams count is: " + str(len(ngramsOne)))
	print(ngramsTwo)
	print("2-grams count is: " + str(len(ngramsTwo)))

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
def cleanInput(input):
	input = re.sub("\n+", " ", input)
	input = re.sub("\[[0-9]*\]", "", input)
	input = re.sub(" +", " ", input)
	input = bytes(input, "utf-8")
	input = input.decode("ascii", "ignore")
	cleanInput = []
	for item in input:
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower() == "a" or item.lower() == "i"):
			cleanInput.append(item)
	return cleanInput
def ngrams(input, n):
	input = cleanInput(input)
	output = []
	for i in range(len(input) - n + 1):
		output.append(input[i : i + n])
	return output

if __name__ == "__main__":
	html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
	bsObj = BeautifulSoup(html)
	content = bsObj.find("div", {"id" : "mw-content-text"}).get_text()
	ngrams = ngrams(content, 2)
	print(ngrams)

#第八章2020.04.01#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator
def cleanInput(input):
	input = re.sub("\n+", " ", input).lower()
	input = re.sub("\[[0-9]*\]", "", input)
	input = re.sub(" +", " ", input)
	input = bytes(input, "utf-8")
	input = input.decode("ascii", "ignore")
	cleanInput = []
	input = input.split(" ")
	for item in input:
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower() == "a" or item.lower() == "i"):
			cleanInput.append(item)
	return cleanInput
def ngrams(input, n):
	input = cleanInput(input)
	output = {}
	for i in range(len(input) - n + 1):
		ngramTemp = " ".join(input[i : i + n])
		if ngramTemp not in output:
			output[ngramTemp] = 0
		output[ngramTemp] = 1
	return output

if __name__ == "__main__":
	content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), "utf-8")
	ngrams = ngrams(content, 2)
	sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse = True)
	print(sortedNGrams)

from urllib.request import urlopen
from random import randint
def wordListSum(wordList):
	sum = 0
	for word, value in wordList.items():
		sum += value
	return sum
def retrieveRandomWord(wordList):
	randIndex = randint(1, wordListSum(wordList))
	for word, value in wordList.items():
		randIndex -= value
		if randIndex <= 0:
			return word
def buildWordDict(text):
	text = text.replace("\n", " ")
	text = text.replace("\"", "")
	punctuation = [",", ".", ";", ":"]
	for symbol in punctuation:
		text = text.replace(symbol, " " + symbol + " ")
	words = text.split(" ")
	words = [word for word in words if word != ""]
	wordDict = {}
	for i in range(1, len(words)):
		if words[i - 1] not in wordDict:
			wordDict[words[i - 1]] = {}
		if words[i] not in wordDict[words[i - 1]]:
			wordDict[words[i - 1]][words[i]] = 0
		wordDict[words[i - 1]][words[i]] = wordDict[words[i - 1]][words[i]] + 1
	return wordDict

if __name__ == "__main__":
	text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), "utf-8")
	wordDict = buildWordDict(text)
	length = 100
	chain = ""
	currentWord = "I"
	for i in range(0, length):
		chain += currentWord + " "
		currentWord = retrieveRandomWord(wordDict[currentWord])
	print(chain)

from nltk import FreqDist
fdist = FreqDist(text6)
fdist.most_common(10)

from nltk import bigrams
bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
bigramsDist[("Sir", "Robin")]

from nltk import ngrams
from nltk import FreqDist
fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
fourgramsDist[("father", "smelt", "of", "elderberries")]

from nltk.book import *
from nltk import word_tokenize
text = word_tokenize("Strange women lying in ponds distributing swords is \
						no basis for a system of government. Superme executive power \
						derives from a mandate from the masses, not from some farcical aquatic ceremony.")
from nltk import pos_tag
print(pos_tag(text))

from nltk import word_tokenize, sent_tokenize, pos_tag
sentences = sent_tokenize("Google is one of the best companies in the world. \
									I constantly google myself to see what I'm up to.")
nouns = ["NN", "NMS", "NNP", "NNPS"]
for sentence in sentences:
	if "google" in sentence.lower():
		taggedWords = pos_tag(word_tokenize(sentence))
		for word in taggedWords:
			if word[0].lower() == "google" and word[1] in nouns:
				print(sentence)

#第九章2020.04.01#
import requests
params = {'firstname': "Ryan", "lastname": "Mitchell"}
r = requests.post("http://pythonscraping.com/files/processing.php", data = params)
print(r.text)

params = {'email_addr': "ryan.e.mitchell@gmail.com"}
r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data = params)
print(r.text)

import requests
params = {"username": "Ryan", "password": "password"}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(r.cookies.get_dict())
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies = r.cookies)
print(r.text)

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth("ryan", "password")
r = requests.post(url = "http://pythonscraping.com/pages/auth/login.php", auth = auth)
print(r.text)

#第十章2020.04.02#
from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path = "")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.PhantomJS(executable_path = "")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, "loadedButton"))
finally:
	print(driver.find_element_by_id("content").text)
	driver.close()

from selenium import webdriver
from time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
	elem = driver.find_element_by_tag_name("html")
	count = 0
	while True:
		count += 1
		if count > 20:
			print("Timing out after 10 seconds and returning")
			return
		time.sleep(0.5)
		try:
			elem == driver.find_element_by_tag_name("html")
		except StaleElementReferenceException:
			return 
if __name__ == "__main__":
	driver = webdriver.PhantomJS(executable_path = "")
	driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
	waitForLoad(driver)
	print(driver.page_source)

#第十二章2020.04.02#
import requests
from bs4 import BeautifulSoup
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 \
			(KHTML, like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,\
			application/xml;q=0.9,image/webp,*/*;q=0.8"}
url = "http://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
req = session.get(url, headers = headers)
bsObj = BeautifulSoup(req.text)
print(bsObj.find("table", {"class" : "table-striped"}).get_text)

from selenium import webdriver
driver = webdriver.PhantomJS(executable_path = "")
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

