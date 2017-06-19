from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from math import ceil
from time import sleep
from sys import exit
import time
import re
import csv
import codecs
import pickle
import os
import urllib
import datetime



browser = webdriver.PhantomJS(r"C:\\phantomjs\bin\phantomjs.exe")
today = datetime.date.today()
FileWriter = codecs.open('JobList' + str(today) + '.csv', 'wb', 'utf-8')
YEAR='2017'

## WRITE HEADER
FileWriter.write('Rank| H1B Visa Sponsor| Number of LCA  *| Average Salary| Job Title\n')
    
with open('JobLinksFull.txt') as JobLinks:
  for JobLink in JobLinks.readlines():
    print JobLink

    browser.get(JobLink)
    source = BeautifulSoup(browser.page_source, "html.parser")

    JobTitle = source.find('span', attrs={'id' : 'ctl00_ctl00_lblMenu'})
    JobTitle = JobTitle.text[42:]

    FIRST=0
    CurrentPage = 1

    while True:
      print 'Job Title: ' + JobTitle + ' - PAGE: ' + str(CurrentPage)

      JobTable = source.find('table', attrs={'class' : 'tbl'})
      JobTable = BeautifulSoup(str(JobTable), "lxml")

      for tr in JobTable.find_all('tr'):
        
        Count=0
        TEXT_TO_WRITE=''
        for td in tr.find_all('td'):
          Count = Count+1
          TEXT_TO_WRITE = TEXT_TO_WRITE + td.text + '|'

          if Count==4:
            if FIRST!=0:
              FileWriter.write(TEXT_TO_WRITE + JobTitle + '\n')
            else:
              FIRST=1

            Count=0
            TEXT_TO_WRITE=''

      PageTag1 = JobLink[JobLink.rfind('/')+1 : JobLink.rfind(YEAR)-1]
      PageTag2 = '-' + YEAR + 'JT.htm'


      ## GET THE CONTENT OF THE NEXT PAGE
      CurrentPage=CurrentPage+1
      NextPage = 'http://www.myvisajobs.com/' + PageTag1 + '_' + str(CurrentPage) + PageTag2
      browser.get(NextPage)
      source = BeautifulSoup(browser.page_source, "html.parser")

      if str(source).find('No records') != -1:
        break
      else:
        FIRST=0

FileWriter.close()
browser.quit() 
