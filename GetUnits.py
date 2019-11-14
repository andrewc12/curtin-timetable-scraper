from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from time import sleep
import sys

import csv

import CurtinDriver
import CurtinExtractData


def main():
    options = Options()
    #options.headless = True

    driver = webdriver.Firefox(options=options)

    CurtinDriver.gotosearch(driver)
    CurtinDriver.blank(driver)
    CurtinDriver.search(driver)
    
    sleep(5)
    units = CurtinExtractData.getallunits(driver) 
    
    print(units)



    with open('units.csv', 'wt') as f:
        csv_writer = csv.writer(f)
        header = ['id', 'unitCode', 'unitName']

        csv_writer.writerow(header) # write header
        csv_writer.writerows(units)




    driver.close()

if __name__ == "__main__":
    main()
