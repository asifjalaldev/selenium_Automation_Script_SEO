import imp
from pathlib import Path
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
f= open("D:/My Projects/try_django/web scraping/p.text","r") 
contents=f.readlines()
for c in contents:
    driver.get("https://www.google.com/")
    googleTextBox=driver.find_element_by_name("q").send_keys(c+":youtube")
    SearchBtn=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)
    time.sleep(4)
    results=driver.find_elements_by_css_selector("#result-stats")
    for r in results:
        string=r.text.split()
        f1=open("research.csv","a")
        # print(type(c) )
        # print( type(string))
        s=string[1].replace(",","")
        data=f' {c} ,{s}\n'
        f1.write(data)
    time.sleep(2)
    driver.find_element_by_name("q").clear()
    f1.close()
time.sleep(2)
f.close()
time.sleep(4)
driver.quit()
