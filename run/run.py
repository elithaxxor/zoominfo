from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import os, re, time, random
#from ..fileparsers import FileParser as FP
import keyboard
import pyautogui

import sys
sys.path.insert(0, '/Users/adelal-aali/Documents/ZoomInfo/pythonProject/project/fileparsers')  # Add the path to the utils directory
import FileParser as FP


# #import project.resources.resourcesInfo as INFO
# #from ..resources import resourcesInfo
# from project.downloaders import fileDownloader as DOWN
# # from downloaders import fileDownloader as DOWN
# import runpy as RUN
# import sys, time, datetime
# from project.fileparsers import fileParser as FP ## ACCESS TO FILE PARSERS
# from project.downloaders import fileDownloaderV as DWN  ## ACCESS TO DOWNLOADERS
# from ..resources import resourcesInfo



# fp = FP.fileParser("/Users/adelal-aali/Documents/ZoomInfo/pythonProject/project/fileparsers/hrefdata.txt")
#fp.read_file()

# svc = webdriver.ChromeService(executable_path=binary_path)
# driver = webdriver.Chrome(service=svc)
#
# driver.get("http://www.python.org")
# assert "Python" in driver.title

# make sure this path is correct
PATH = "/Users/adelal-aali/Documents/ZoomInfo/pythonProject/project/resources/chromedriver"
HREF = "/Users/adelal-aali/Documents/ZoomInfo/pythonProject/project/fileparsers/hrefdata.txt"
# driver = webdriver.Chrome(PATH)
# LOGIN = "https://login.zoominfo.com/"
# USER = resourcesInfo.resourcesInfo.ADDR
# PASS = resourcesInfo.resourcesInfo.PASS
#
# print(f"[!] USER: \{USER} \n [!] PASS: \{PASS}")


''' * This function will parse the file(after user adds sites)  and add the data to a list for selenium to access'''
def fileParser():
    FP.fileParser.addToList("/Users/adelal-aali/Documents/ZoomInfo/pythonProject/project/fileparsers/hrefdata.txt")
    FP.fileParser.read_file("/Users/adelal-aali/Documents/ZoomInfo/pythonProject/project/fileparsers/hrefdata.txt")


def setupDrive(url):
    # Set the path to the chromedriver executable
    chrome_driver_path = '/Users/adelal-aali/Documents/ZoomInfo/pythonProject/project/run/chromedriver'
    # Set up Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'

    # Add headers
    user_agent =  ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/39.0.2171.95 Safari/537.36')

    #chrome_options.add_argument('user-agent={0}'.format(user_agent))
    chrome_options.add_argument(f'user-agent={user_agent}')
    # Remove the Automation Info
    chrome_options.add_argument('--disable-infobars')

    # Initialize the Chrome WebDriver
    service = Service(chrome_driver_path)

    ## SO THE PRINT INTERFACE DOES NOT SHOW UP
    chrome_options.add_argument('--kiosk-printing')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 20)
    action = ActionChains(driver)

    def stop_driver(e):
        if e.name == 'esc':
            driver.quit()
    def runDriver():
        # Open a webpage
        runUrl = url
        driver.get(runUrl)

        # Get the page title
        title = driver.title
        print("Page title:", title)
        driver.execute_script("window.print();")
        # Wait for a few seconds to allow the print dialog to appear
        print("****************************************************************")
        print("[!] Clicking ")
        driver.implicitly_wait(3)
        pyautogui.click()
        pyautogui.press('enter')
        pyautogui.press('enter')
        #keyboard.KeyboardEvent('enter')
        # Close the browser
        driver.quit()

    keyboard.on_press(stop_driver)
    runDriver()


fileParser()
import_websites = FP.fileParser.websites
print("[!] Website List \n", import_websites)
print("[!] Website List \n", type(import_websites), "\n[LENGTH]", len(import_websites), "sites added")

for(i) in range(0, len(import_websites)):
    print(f"[!] processing Site: {import_websites[i]}")
    url = import_websites[i]
    setupDrive(url)
    i+= 1
#
#
# class Run() :
#     def __init__(self):
#         self.driver = webdriver.Chrome(PATH)
#         self.driver.get(LOGIN)
#         self.maximize_window()
#         key = Keys()
#
#         ''' USE THIS TO ADD EXTENSIONS TO CHROME (ADBLOCKER, ETC) '''
#         # options = self.chrome_options()
#         # self.driver = webdriver.Chrome(PATH, options=options)
#
#     def getHREF(self):
#         print("[!] Getting HREF from file")
#         with open(HREF, 'r') as f:
#             href = f.read()
#             print(f"[!] HREF: {href}")
#             return href
# Run.getHREF()
