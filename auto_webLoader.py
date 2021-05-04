from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import os
import sys
import argparse

text = "Auto Web Loader by Python\nUsing config.txt or the below parameters:"

parser = argparse.ArgumentParser(description = text)  

parser.add_argument("-u", "--url", help="The URL")
parser.add_argument("-n", "--numHits", help="Num of hits")
parser.add_argument("-p", "--proxy", help="proxy [PROXY_HOST:PROXY_PORT] *optional")
parser.add_argument("-t", "--proxyType", help="proxy type: 1 - HTTP Proxy, 2 - HTTPS Proxy, 3 - Both HTTP/HTTPS Proxy, 0 - No Proxy *optional")
parser.add_argument("-f", "--firefoxPath", help="FirefoxPath - default: C:\\Program Files\\Mozilla Firefox\\firefox.exe (no need if correct)")
parser.add_argument("-g", "--geckodriver", help="Geckodriver Folder - default: current path (no need if correct)")
parser.add_argument("-w", "--timeWait", help="the seconds of the waiting-browser between 2 times - default: 15 seconds")

args = parser.parse_args()
url = "https://topvl.net"
if args.url:
	url = args.url

FIREFOX_PATH = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
if args.firefoxPath:
	FIREFOX_PATH = args.firefoxPath

geckodriver_path = r'geckodriver.exe'
if args.geckodriver:
	geckodriver_path = args.geckodriver

proxyType = 0
if args.proxyType:
	proxyType = int(args.proxyType)

timeWait = 15
if args.timeWait:
	timeWait = int(args.timeWait)

PROXY_HOST = ""
PROXY_PORT = 0
if proxyType > 0 and not args.proxy:
	sys.exit("Proxy is required. Please input -p [PROXY_HOST:PROXY_PORT]")
elif proxyType > 0 and ":" not in args.proxy:
	sys.exit("Proxy's invalid. Please input -p [PROXY_HOST:PROXY_PORT]")
elif proxyType > 0:
	proxy = args.proxy
	PROXY_HOST = proxy.split(":")[0]
	PROXY_PORT = int(proxy.split(":")[1])
	

numHit = 100
if args.numHits:
	numHit = int(args.numHits)

def resetConf():
	numHit = 0
	url = ""
	proxyType = 0
	timeWait = 15
	geckodriver_path = r'geckodriver-v0.29.0-win65\\geckodriver.exe'
	FIREFOX_PATH = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
	PROXY_HOST = ""
	PROXY_PORT = 0

if os.path.isfile("config.txt"):
	resetConf()
	rfile = open("config.txt")
	for line in rfile:
		ldata = line.strip().split("#")[0]
		if "URL =" in ldata.upper() or "URL=" in ldata.upper():
			url = ldata.upper().replace("URL =","").replace("URL=","").strip().lower()
		if "NUMHITS =" in ldata.upper() or "NUMHITS=" in ldata.upper():
			numHit = int(ldata.upper().replace("NUMHITS =","").replace("NUMHITS=","").strip())
		if "timeWait =".upper() in ldata.upper() or "timeWait=".upper() in ldata.upper():
			change = "timeWait".upper()
			timeWait = int(ldata.upper().replace(change+" =","").replace(change+"=","").strip())
		if "proxyType =".upper() in ldata.upper() or "proxyType=".upper() in ldata.upper():
			change = "proxyType".upper()
			proxyType = int(ldata.upper().replace(change+" =","").replace(change+"=","").strip())

		if "proxy =".upper() in ldata.upper() or "proxy=".upper() in ldata.upper():
			change = "proxy".upper()
			proxy = ldata.upper().replace(change+" =","").replace(change+"=","").strip()
			if ":" not in proxy:
				sys.exit("Proxy's invalid. Please change PROXY option to [PROXY_HOST:PROXY_PORT]")
			else:
				PROXY_HOST = proxy.split(":")[0]
				PROXY_PORT = int(proxy.split(":")[1])

		if "geckodriver_path =".upper() in ldata.upper() or "geckodriver_path=".upper() in ldata.upper():
			change = "geckodriver_path".upper()
			geckodriver_path = ldata.upper().replace(change+" =","").replace(change+"=","").strip()

		if "FIREFOX_PATH =".upper() in ldata.upper() or "FIREFOX_PATH=".upper() in ldata.upper():
			change = "FIREFOX_PATH".upper()
			FIREFOX_PATH = ldata.upper().replace(change+" =","").replace(change+"=","").strip()
	rfile.close()

if(url == "") or "http" not in url.lower():
	sys.exit("URL's invalid. Please re-check your URL.")

if(not os.path.isfile(FIREFOX_PATH) or not os.path.isfile(geckodriver_path)):
	sys.exit("Firefox Path or GeckoDriver's invalid. Please re-check.\nFireFox Path: "+FIREFOX_PATH+"\nGeckoDriver: "+geckodriver_path)

i = 0
while i < numHit:
	binary = FirefoxBinary(FIREFOX_PATH)
	
	firefox_profile = webdriver.FirefoxProfile()
	if(proxyType > 0):
		firefox_profile.set_preference("network.proxy.type", 1)

	if proxyType == 1 or proxyType == 3:
		firefox_profile.set_preference("network.proxy.http", PROXY_HOST)
		firefox_profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
	if proxyType == 2 or proxyType == 3:
		firefox_profile.set_preference("network.proxy.ssl", PROXY_HOST)
		firefox_profile.set_preference("network.proxy.ssl_port", int(PROXY_PORT))
	#firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
	firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
	firefox_profile.update_preferences()

	#driver = webdriver.Firefox(firefox_profile=firefox_profile,firefox_binary=binary,capabilities=firefox_capabilities,executable_path=geckodriver_path)
	driver = webdriver.Firefox(firefox_profile=firefox_profile,firefox_binary=binary,executable_path=geckodriver_path)
	driver.get(url)#put here the adress of your page
	#elements = driver.find_elements_by_class_name("mb-6p")
	#for e in elements:
	#	e.click()
	time.sleep(timeWait)
	driver.close()
	#time.sleep(15)
	print("Seq: "+str(i+1))
	i += 1