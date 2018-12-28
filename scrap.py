# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 12:46:07 2018

@author: Aditya
"""

from selenium import webdriver


def view_webpage(link_file):
    try:
        elem1 = browser.find_elements_by_tag_name('a')
    except:
        print('some error occured')
    try:
        for elem in elem1:
            if elem.get_attribute('title') == 'Download photo':
                print(elem.get_attribute('href'), file=link_file)
    except:
        print("No data in Element")

browser = webdriver.Firefox()
search_term = "mountains/"
url = "https://unsplash.com/search/photos/" + search_term
browser.get(url)
complete = False
# we will open the file in apend mode
link_file = open("links.txt", mode="a+")

while not complete:
    view_webpage(link_file)
    complete = True
    
# Closing the file to save in drive
link_file.close()