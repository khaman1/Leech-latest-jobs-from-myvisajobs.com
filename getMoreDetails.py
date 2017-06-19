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
from pickle import dumps



  
browser = webdriver.PhantomJS(r"C:\\phantomjs\bin\phantomjs.exe")
today = datetime.date.today()
FileWriter = codecs.open('AllJobs' + str(today) + '.csv', 'wb', 'utf-8')
NUMBER_OF_APPROVED_H1B_CANDIDATES_IN_A_COMPANY_AT_LEAST = 20

##################################################################
FileWriter.write('Rank,H1B Visa Sponsor,Number of LCA,Average Salary,Job Title,,Job Openings, Homepage Link,Glassdoor,Indeed\n')
input_file = csv.DictReader(open('JobList2017-06-19-RemoveDuplicatedSponsor.csv'))

LineCnt=0
for row in input_file:
  LineCnt = LineCnt+1
  if int(row['Number of LCA']) >= NUMBER_OF_APPROVED_H1B_CANDIDATES_IN_A_COMPANY_AT_LEAST:
    
    ## GET HOMEPAGE OF H1B Visa Sponsor
    HomePageLink = 'https://www.google.com/search?q=' + row['H1B Visa Sponsor']
##    browser.get('https://www.google.com/search?q=' + row['H1B Visa Sponsor'])
##    source = BeautifulSoup(browser.page_source, "html.parser")
##
##    try:
##      HomePageLink = source.find('cite').text
##    except AttributeError:
##      HomePageLink = ''
##      print "Can't get the homepage link"


    ## MAKE JOB LINK FROM GLASSDOOR
    Glassdoor_JobLink = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + row['H1B Visa Sponsor'] + '&locT=N&locId=1'

    ## INDEED
    Indeed_JobLink = 'https://www.indeed.com/jobs?q=' + row['H1B Visa Sponsor'] + '&l=United+States'

    ## GET NUMBER OF JOB OPENINGS
    browser.get(Glassdoor_JobLink)
    source = BeautifulSoup(browser.page_source, "html.parser")
    
    LeftColumn = source.find_all('div', attrs={'class' : 'logoWrap'})
    JobOpenings = len(LeftColumn)
  
    PageNum = source.find_all('li', attrs={'class' : 'page'})
    if len(PageNum) > 1:
      JobOpenings = JobOpenings*len(PageNum)

    print str(LineCnt) + ' - ' + row['H1B Visa Sponsor']  + ' - Job Openings: ' + str(JobOpenings)
    ##
    TEXT_TO_WRITE = row['Rank'] + ',' + row['H1B Visa Sponsor'] + ',' + row['Number of LCA'] +\
                    ',"' + row['Average Salary'] + '",' + row['Job Title']
    FileWriter.write(TEXT_TO_WRITE + ',' + str(JobOpenings) + ',' + HomePageLink\
                     + ',' + Glassdoor_JobLink + ',' + Indeed_JobLink + '\n')
 

browser.quit()
FileWriter.close()
