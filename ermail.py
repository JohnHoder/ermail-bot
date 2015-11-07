# -*- coding: utf-8 -*-
import re
import cookielib
import urllib
import urllib2


try:
	from requests import session
	import requests
	from bs4 import BeautifulSoup

except ImportError:
    	print "\nPlease make sure you have BeautifulSoup and requests modules installed!\n"
    	exit()

def banner():
	print "\nErmail bot v1.0 - Jan Hodermarsky a.k.a HardC0re, 2013"


banner()

url = 'http://www.ermail.cz/popup_page_ajax.php'
payload= {'command' : '111', 'email' : 'name@gmail.com', 'pwd' : 'myPassword123'}

with session() as c:
    c.post('http://www.ermail.cz/popup_page_ajax.php', data=payload)
    while(1):
	request = c.get('http://www.ermail.cz/mujucet/prehled')
    	#print request.headers
   	#print request.text
	soup = BeautifulSoup(request.text)
	soup.prettify()
	count = 1
	res = soup.find('div',{"class":"unreadEmails"})
	lis = res.findAll('li')
	for j in lis:
    		if(j.find('a') != None):
        		#no = j.contents[0].string
        		#print "Number\t:%s" % no
        		#print j.contents[1].string #1
        		print "link %(a)s\t:%(food)s" % {'a' : count, 'food' : j.contents[0]['href']}
			count = count + 1
			#------------------------------
			foodPage=requests.get(j.contents[0]['href'], headers={"Referer":"http://www.ermail.cz/mujucet/prehled", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0" });
			FoodSoup = BeautifulSoup(foodPage.text)
			FoodSoup.prettify()
			lol = FoodSoup.find('p',{"style":"margin: 16px 0;"})
			if(lol==None):
				finalUrl = FoodSoup('a')[0]['href']
				#print finalUrl
				foodPage=requests.get(finalUrl, headers={"Referer":j.contents[0]['href'], "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0" });
				continue
			lulz = lol.find('a') #lol.findAll
			try:
				finalUrl = FoodSoup('a', target="_blank")[0]['href']
			except:
				finalUrl = FoodSoup('a')[0]['href']
			foodPage=requests.get(finalUrl, headers={"Referer":j.contents[0]['href'], "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0" });

print 'No more emails to read'
raise SystemExit



#if __name__ == '__main__':
#    	main()
	
	
	





