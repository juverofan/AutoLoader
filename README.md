# AutoLoader
Automatical Web Loader by Python

The script, which was coded by Python, calls Firefox browser and uses GeckoDriver (you can download in this folder) to load the web (with inputed <b>URL</b>) <b>NUMHITS</b> times (<b>TIMEWAIT</b> seconds/each time), you can use HTTP/HTTPS Proxy or not.<br>
Requirement:
- Python 3
- Selenium, Webdriver

<b>Usage:</b>
<br> If config.txt is exists (you can create from config_sample.txt), the script uses it first, command:
<br><b>python auto_webLoader.py</b>
<br> If config.txt is not exists, the script uses the command:
<br><b>python auto_webLoader.py -u URL -n NUMHITS <i>[-p PROXY -t PROXYTYPE -f FireFoxPath -g GeckoDriverPath -w TIMEWAIT]</i></b>

