from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from time import sleep
import sys

import csv

def getallunits(driver):
    allclass = driver.find_elements_by_xpath("//select[@name='criteriaEntry:allUnits']/option")
    units = []
    for elm in allclass:
        split = elm.text.split(" ", 1)
        unit = (elm.get_attribute("value"), split[0], split[1] )
        units.append(unit)
    print(units)
    print(units , file=sys.stderr)
    return units


def blankandsearch(driver):
    driver.get("http://timetable.student.curtin.edu.au/criteriaEntry.jsf")
    assert "Plan Your Timetable" in driver.title
    #clear search
    elem = driver.find_element_by_name("criteriaEntry:filterUnitCodeOrTitle")
    elem.clear()
    #elem.send_keys("pycon")
    #elem.send_keys(Keys.RETURN)
    #assert "No results found." not in driver.page_source
    
    #search for all units
    srch = driver.find_element_by_name("criteriaEntry:unitSearchButton")
    srch.click()




def viewtimetable(driver, classcode):
    #driver = webdriver.Firefox()
    #driver = webdriver.Firefox(options=options)
    driver.get("http://timetable.student.curtin.edu.au/criteriaEntry.jsf")
    assert "Plan Your Timetable" in driver.title

    #clear all units
    clear = driver.find_element_by_name("criteriaEntry:removeAllButton")
    clear.click()

    #select a unit
    rndclass = driver.find_element_by_xpath("//option[@value=" + classcode[0] + "]")
    rndclass.click()

    #add unit
    add = driver.find_element_by_name("criteriaEntry:addButton")
    add.click()


    #view timetable
    view = driver.find_element_by_name("criteriaEntry:timetableForUnitsButton")
    view.click()


def getdata(driver, csv):
    #get time table
    classtimetable = driver.find_elements_by_xpath("//table[@class='unitList']/tbody/tr")
    #classtimetable = driver.find_element_by_class_name("unitList")
    #print(classtimetable.text)
    for i in classtimetable:
        #print(i.text)
        #for j in i.find_elements_by_tag_name("td"):
        #    print(j.text)
        comp_list = [j.text for j in i.find_elements_by_tag_name("td")]
        print(comp_list)
        print(comp_list  , file=sys.stderr)
        csv.writerow(comp_list)





def main():
    options = Options()
    #options.headless = True

    driver = webdriver.Firefox(options=options)

    blankandsearch(driver)

    units = getallunits(driver) 

    sleep(5)


    with open('units.csv', 'wt') as f:
        csv_writer = csv.writer(f)

        total = len(units) 
        progress = 1

        for i in units:
        #    if (progress < 1116):
        #        progress = progress + 1
        #        continue
            for count in range(3):
                print("grabbing " + str(i[:]) + " " + str(progress) + " out of " + str(total)  , file=sys.stderr)
                try:
                    viewtimetable(driver, i)
                    getdata(driver, csv_writer)
                    break
                except:
                    driver.close()
                    sleep(10)
                    driver = webdriver.Firefox(options=options)
                    blankandsearch(driver)



        #    driver.close()
            #sleep(3)
            progress = progress + 1


    driver.close()

if __name__ == "__main__":
    main()
