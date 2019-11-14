from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from time import sleep
import sys

import csv

class CurtinDriver:
    '''methods for each task you want to do'''

def gotosearch(driver):
    driver.get("http://timetable.student.curtin.edu.au/criteriaEntry.jsf")
    assert "Plan Your Timetable" in driver.title

def blank(driver):
    assert "Plan Your Timetable" in driver.title
    #clear search
    elem = driver.find_element_by_name("criteriaEntry:filterUnitCodeOrTitle")
    elem.clear()
    #elem.send_keys("pycon")
    #elem.send_keys(Keys.RETURN)
    #assert "No results found." not in driver.page_source

def clearunits(driver):
    clear = driver.find_element_by_name("criteriaEntry:removeAllButton")
    clear.click()


def search(driver):
    assert "Plan Your Timetable" in driver.title

    #search for all units
    srch = driver.find_element_by_name("criteriaEntry:unitSearchButton")
    srch.click()


def selectunit(driver, classcode):
    assert "Plan Your Timetable" in driver.title

    rndclass = driver.find_element_by_xpath("//option[@value=" + classcode + "]")
    rndclass.click()


def addunit(driver):
    assert "Plan Your Timetable" in driver.title

    add = driver.find_element_by_name("criteriaEntry:addButton")
    add.click()




def viewtimetable(driver):
    assert "Plan Your Timetable" in driver.title

    view = driver.find_element_by_name("criteriaEntry:timetableForUnitsButton")
    view.click()





