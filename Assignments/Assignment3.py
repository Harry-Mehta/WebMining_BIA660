#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[ ]:





# In[ ]:



                    


# In[1]:


import requests
import time
import re 
import csv
from bs4 import BeautifulSoup
result=set()
r = requests.get("https://www.stevens.edu/school-business/faculty")
html = r.content
soup = BeautifulSoup(html.decode('ascii','ignore'), 'html5lib')
links = soup.findAll('a')
for a in links:
  q=a['href']
  if q.startswith('http://web.stevens.edu/'):
    result.add(q)
list_result=list(result)
myfile=open('xyz.csv','w')
f = csv.writer(myfile)
# f.writerow([item])
for item in list_result:
  req= requests.get(item)
  print(item)
  f.writerow([item])
  myfile.flush()
myfile.close()


# In[15]:


import requests
import time
import re 
import csv
from selenium import webdriver
email_addresses=[]
links=[]
chromedriver = "C:\\Users\\mehta\\Anaconda3\\Lib\\site-packages\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

with open('xyz.csv', 'rt') as csvfile:
  readCSV = csv.reader(csvfile)
  for row in readCSV:
    row=str(row)
    row=row.replace('[','').replace(']','').replace('\'','').strip()
    if row:
        links.append(row)
file1 = open("emails.txt","w") 
for row in links:
    driver.get(row)
    soup = BeautifulSoup(driver.page_source, 'html.parser')    # Extract all email addresses.    # print(soup.get_text())    
    email_addresses += re.findall("\S+@stevens.edu", soup.get_text())    
    email_addresses = list(set(email_addresses))
for row in email_addresses:
    file1.write(row+"\n")
file1.close()


# In[ ]:




