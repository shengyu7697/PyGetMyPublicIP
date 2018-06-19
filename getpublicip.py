#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

def getMyPublicIP1():
	r = requests.get('https://myip.com.tw')
	soup = BeautifulSoup(r.content, 'lxml')
	tag = soup.find('font').getText()
	return tag

def getMyPublicIP2():
	r = requests.get('https://www.rus.net.tw/myip.php')
	soup = BeautifulSoup(r.content, 'lxml')
	tag = soup.find_all('td', text='您 的 IP 是')[0].find_next_sibling('td').getText()
	return tag.strip()
	#<td class="myip" align="center" width="300">您 的 IP 是</td>
	#<td width="190">xx.xx.xx.xx    </td>

def getMyPublicIP3():
	return requests.get('https://api.ipify.org').text

def getMyPublicIP4():
	headers = {
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
	}
	rs = requests.session()
	r = rs.get('https://whatismyipaddress.com', headers=headers)
	soup = BeautifulSoup(r.content, 'lxml')
	return soup.find('div', id='ipv4').find('a').text

if __name__ == '__main__':
	print('My Public IP address is:')
	print('%s (https://myip.com.tw)' % getMyPublicIP1())
	print('%s (https://www.rus.net.tw/myip.php)' % getMyPublicIP2())
	print('%s (https://api.ipify.org)' % getMyPublicIP3())
	print('%s (https://whatismyipaddress.com)' % getMyPublicIP4())