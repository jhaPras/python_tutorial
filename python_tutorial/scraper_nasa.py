#!/usr/bin/env python3


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
# import splinter


# splinter and selenium are same the only difference is splinter is python based whereas later on is java based 

##  1. first we will activate our browser in selenium

browser = webdriver.Chrome('/usr/local/bin/chromedriver 2')

##  2. We will try to access the page 

page = browser.get('https://mars.nasa.gov/news/')


## 3. we will convert the page in beautiful soup object and further we will save it into file for inspection with the help /
##    of beautiful soup prettify method

doc_obj = bs(browser.page_source,'html.parser')

## 4. We are trying to find the tag and extract all the title info about the post and saving it to a list 


title = doc_obj.find_all('div',{'class':'content_title'})

paragraph_text = doc_obj.find_all('div',{'class':'article_teaser_body'})



paragraph_text_list = [t.get_text() for t in paragraph_text]

# for t in paragraph_text:
#     paragraph_text_list.append(t.get_text())


title_list = [t.get_text().replace('\n','') for t in title]



with open('title.txt','w+') as f:
     f.write(str(title_list))

results_var = {'title':title_list,'title_text':paragraph_text_list}

print(results_var)



# pretty_obj = bs_obj.prettify()

# with open('nasa.html','w+') as f:
#     f.write(pretty_obj)
