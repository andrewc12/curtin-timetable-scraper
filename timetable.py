from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
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

#unit table
#allunits = driver.find_element_by_name("criteriaEntry:allUnits")
#print(allunits)



#get all units as csv
allclass = driver.find_elements_by_xpath("//select[@name='criteriaEntry:allUnits']/option")
#print(allclass)
for elm in allclass:
    split = elm.text.split(" ", 1)
#    print(elm.get_attribute("value") + "," + split[0] + "," + split[1] )
    unit = (elm.get_attribute("value"), split[0], split[1] )
    print(unit)
    #print(elm.text)





#select a unit
rndclass = driver.find_element_by_xpath("//option[@value='315560']")
rndclass.click()

#add unit
add = driver.find_element_by_name("criteriaEntry:addButton")
add.click()

#clear all units
clear = driver.find_element_by_name("criteriaEntry:removeAllButton")


#view timetable
view = driver.find_element_by_name("criteriaEntry:timetableForUnitsButton")
view.click()





sleep(1)




#get time table
classtimetable = driver.find_elements_by_xpath("//table[@class='unitList']/tbody/tr")
#classtimetable = driver.find_element_by_class_name("unitList")
#print(classtimetable.text)
for i in classtimetable:
    print(i.text)
    #for j in i.find_elements_by_tag_name("td"):
    #    print(j.text)
    comp_list = [j.text for j in i.find_elements_by_tag_name("td")]
    print(comp_list)




driver.close()

