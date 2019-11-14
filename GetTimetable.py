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





    with open('units.csv', 'rt') as f:
        csv_reader = csv.reader(f)

        next(csv_reader) # skip the heading

        lines = []
        for line in csv_reader:
            lines.append(line)
    
    
    with open('timetable.csv', 'wt') as f:
        csv_writer = csv.writer(f)

        total = len(lines) 
        progress = 1



        while len(lines) > 0:
            
            driver = webdriver.Firefox(options=options)
            try:
                CurtinDriver.gotosearch(driver)
                CurtinDriver.blank(driver)
                CurtinDriver.search(driver)
                
                sleep(5)
            
                while len(lines) > 0:
                    linestograb = min(len(lines),12)
                    print("grabbing "  + str(progress) + " out of " + str(total)  , file=sys.stderr)
                    progress += linestograb
                    
                    CurtinDriver.gotosearch(driver)
                    CurtinDriver.clearunits(driver)
                    
                    heldlines = []
                    for i in range(1, linestograb):
                        heldlines.append( lines.pop(0))
                    
                    for line in heldlines:
                        CurtinDriver.selectunit(driver, line[0])
                        CurtinDriver.addunit(driver)
                    CurtinDriver.viewtimetable(driver)
                    #sleep(1)
                    info = CurtinExtractData.getdata(driver)
                    print(info)
                    csv_writer.writerows(info)
            except:


                try:
                    lines.extend(heldlines)
                except:
                    print("firefox crashed? before i poped units?")
                
                progress -= linestograb
                
                try:
                    driver.close()
                except:
                    print("firefox crashed?")

if __name__ == "__main__":
    main()
