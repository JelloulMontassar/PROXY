#!/usr/bin/env
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import os
class Prox:
	def __init__(self,ip,port):
		self.ua = UserAgent()
		self.headers = {'User-Agent': str(self.ua.chrome)}
		self.proxy = {}
		self.ip = ip
		self.port = port
		self.proxy['https'] = (self.ip+':'+self.port) 
		url = 'https://whatismyipaddress.com/'
		resp = requests.post(url, proxies=self.proxy,headers=self.headers)
		soup = BeautifulSoup(resp.text, 'lxml')
		url1 = 'https://whatismyipaddress.com/ip/'
		resp1 = requests.post(url1+ip)
		soup1 = BeautifulSoup(resp1.text, 'lxml')
		f= soup.find('table')
		f1 = soup1.find('table')
		os.system('clear')
		print(f.text)
		print('MORE INFORAMTIONS ABOUT THE IP ADRESS')
		print(f1.text)

def menu():
	os.system('clear')
	print('\t\tUSE HTTPS Proxies\n\n')
	ip = input('IP Adress (example:158.140.168.249): ')
	port = input ('Port (example: 3128 : ')
	x = Prox(ip,port)
menu() 
