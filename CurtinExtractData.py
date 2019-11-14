from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from time import sleep
import sys

import csv

class CurtinExtractData:
    '''methods for each task you want to do'''

def getallunits(driver):
    assert "Plan Your Timetable" in driver.title

    allclass = driver.find_elements_by_xpath("//select[@name='criteriaEntry:allUnits']/option")
    units = []
    for elm in allclass:
        split = elm.text.split(" ", 1)
        unit = (elm.get_attribute("value"), split[0], split[1] )
        units.append(unit)
    #print(units)
    print(units , file=sys.stderr)
    return units




def getdata(driver):
    #get time table
    classtimetable = driver.find_elements_by_xpath("//table[@class='unitList']/tbody/tr")
    #classtimetable = driver.find_element_by_class_name("unitList")
    #print(classtimetable.text)
    sessions = []
    for i in classtimetable:
        #print(i.text)
        #for j in i.find_elements_by_tag_name("td"):
        #    print(j.text)
        comp_list = [j.text for j in i.find_elements_by_tag_name("td")]
        print(comp_list)
        print(comp_list  , file=sys.stderr)
        sessions.append(comp_list)
    return sessions

