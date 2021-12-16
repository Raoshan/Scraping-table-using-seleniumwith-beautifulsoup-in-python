from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"F:\\driver\\chromedriver.exe")
from bs4 import BeautifulSoup
import csv

def SeleniumUsing(startdate,enddate):
    url = "https://amg.gwynedd.llyw.cymru/planning/index.html?fa=search"
    driver.get(url)    
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@name='valid_date_from']").send_keys(startdate)
    driver.find_element_by_xpath("//input[@name='valid_date_to']").send_keys(enddate)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.implicitly_wait(30)
    pre = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height==pre:
            break
        pre=new_height   
   
def SoupUsing():
    # current_url = driver.current_url
    # print(current_url)
    html = driver.page_source  
    soup = BeautifulSoup(html, features='lxml')   
    table = soup.find('table',{'class':'table'})
    rows = []
    for row in table.find_all('tr'):
        for th in row.find_all('th'):
            thdata = th.text.strip()
            # rows.append(thdata)
            
    for row in table.find_all('tr'):
        for td in row.find_all('td'):
            tddata = td.text.strip()
            rows.append(tddata)    
    
    with open('amggwynedd.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f,quoting=csv.QUOTE_ALL,delimiter=',',quotechar='"')
        writer.writerow(['Application Reference', 'Application Type', 'Location Details', 'Proposal', 'Ward','Community','Decision','View'])
        writer.writerow(rows)

    # result = [list(val.replace('\n', '') for val in line) for line in csv.reader(open('indeed.csv', 'r'))]
    # print(result)
    print(rows)
    
    
SeleniumUsing('01-12-2020','01-12-2021') 
SoupUsing()

 