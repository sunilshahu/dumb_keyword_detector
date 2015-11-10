import sys
import urllib
import os
import time

web_url = "http://www.amazon.in/Kent-Ultra-UV-Water-Purifier/dp/B0073QKROI/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1447063042&sr=1-1&keywords=B0095S9JU0%7CB008LN5YA4%7CB0095PD2OC%7CB00HPTMWP0%7CB00WQTWXKS%7CB00HPTMQ1K%7CB00NL7LBES%7CB00WQTXCNK%7CB00GNZHAAE%7CB00HPTMN86%7CB010SDNIG6%7CB00E9G8LNO%7CB009PJ8Y3W%7CB0073QKROI%7CB008LN6156%7CB00G52GAQK%7CB00QEYWV8U"

err_count = 0;

web_url2 = "http://www.amazon.in/Kent-Ultra-UV-Water-Purifier/dp/B0073QKROI/ref=zg_bs_1380259031_2"

while True:
    sock = urllib.urlopen(web_url2)
    htmlSource = sock.read()
    sock.close()
    #Find the keyword
    if "Lightning Deal" in htmlSource:
        while True:
            os.system("notify-send 'Ligthning deal active'")
            time.sleep(10)
    #if product specs not found, verify page
    if "L 395 W 136 H 340 (mm)" not in htmlSource:
        err_count = err_count + 1;
        print "Error count"
        print err_count
        if (err_count > 10):
            while True:
                os.system("notify-send 'Url Error'")
                time.sleep(10)
    else:
        err_count = 0
    time.sleep(60)

