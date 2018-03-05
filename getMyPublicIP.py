#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

def getMyPublicIP():
	r = requests.get('https://myip.com.tw/')
	c = r.content
	soup = BeautifulSoup(c, "lxml")
	tag = soup.find("font").getText()
	return tag

def getMyPublicIP2():
	r = requests.get('https://www.rus.net.tw/myip.php')
	c = r.content
	soup = BeautifulSoup(c, "lxml")
	tag = soup.find_all("td", text="您 的 IP 是")[0].find_next_sibling("td").getText()
	return tag.strip()
	#<td class="myip" align="center" width="300">您 的 IP 是</td>
	#<td width="190">219.87.64.222    </td>

def getMyPublicIP3():
	return requests.get('https://api.ipify.org').text

if __name__ == '__main__':
	ip = getMyPublicIP()
	print 'My Public IP address is: %s' % ip