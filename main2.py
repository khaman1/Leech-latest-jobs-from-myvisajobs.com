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



#browser = webdriver.PhantomJS(r"C:\\phantomjs\bin\phantomjs.exe")
#today = datetime.date.today()
#FileWriter = codecs.open('JobList' + str(today) + '.csv', 'wb', 'utf-8')
#YEAR='2017'


with open('JobLinksFull.txt') as JobLinks:
  for a in JobLinks.readlines():
    print a

      

#FileWriter.close()
#browser.quit() 
