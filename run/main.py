import fileParser as FP # Import the fileParser module
import sys
import time, datetime
import webdrivers as WD
import fileParser as FP
from ..resources import colors as C # Import the color module

from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
import os, re, time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def auto_print(driver):
    """Initiates the browser's print dialog and attempts to handle potential print preview scenarios."""

    try:
        # Trigger print dialog using JavaScript
        driver.execute_script("window.print();")

        # Wait for print dialog to appear (adjust timeout as needed)
        time.sleep(2)

        # Handle potential print preview scenarios
        print_preview_handles = driver.window_handles
        for handle in print_preview_handles:
            driver.switch_to.window(handle)
            try:
                # Click the "Print" button within the print preview (adjust selector as needed)
                print_button = driver.find_element_by_css_selector("button[aria-label='Print']")  # Example selector
                print_button.click()
            except Exception as e:
                print("Print button not found in preview:", e)
            finally:
                driver.switch_to.default_content()  # Return to main window

    except Exception as e:
        print("Error during printing:", e)

# Example usage:
driver = webdriver.Chrome()  # Replace with your desired browser driver
driver.get("https://www.example.com")
auto_print(driver)
driver.quit()



class ZoomInfoApp(webdriver.Chrome):
#class BestBuy_ripper (webdriver.Chrome(ChromeDriverManager().install())):
    # cart_wait = WebDriverWait
    global timer
    timer = random.randrange(5.0, 8.0)
    global OS
    OS = os.name
    print(OS, 111111)
    chrome_options = Options
   # driver = webdriver.Chrome(options=chrome_options, executable_path= r"/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi/chromedriver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    executable_path = r"/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi/chromedriver"
    os.environ['PATH'] += executable_path

    def __init__(self): #teardown=False):
        super(ZoomInfoApp, self).__init__(r"/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi/chromedriver")
        #super(BestBuy_ripper, self).__init__(DesiredCapabilities.CHROME['browserName'])
        #self.os.environ['PATH'] += executable_path'

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        # driver = webdriver.Chrome(options=chrome_options, executable_path= r"/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi")
        #self.driver = webdriver.Chrome(options=chrome_options, executable_path= r"/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi")
        self.implicitly_wait(20)
        self.executable_path = r"/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi/chromedriver"
        # self.os.environ['PATH'] += self.executable_path
        self.implicitly_wait(15)
        self.maximize_window()
        self.By = By
        self.Keys = Keys
        self.WebDriverWait = WebDriverWait
        self.Options = Options


    @staticmethod
    def program_dependancies():
        print('Will Add Dependencies Later')
        #### pip install webdriver-manager
        pass

    def install_plugins(self):
        print('Will install plugins later Later')

        pass

    def install_plugin(self):
        chrome_options = Options()
        chrome_options.add_extension("/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi/ad_blocker.crx")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path= r"/home/frank/PycharmProjects/pythonProject/gpu_scraper-main_pi/chromedriver")
        if self.driver:
            print(f'{C.yellow}[ADBLOCKER INSTALLATION -- SUCCESSFUL]{reset}')
        else:
            print(f'{C.red}[ADBLOCKER INSTALLATION -- UNSUCCESSFUL]{reset}')

        time.sleep(3)
        self.get(BB.URL)
        self.implicitly_wait(15)
        time.sleep(timer)
        print(OS)
        print('Random Wait Time', timer)
        time.sleep(3)

        nav_click = self.find_element_by_xpath('//*[@id="site-control-content"]')
        nav_click.click()
        print('Exiting install plugin module')


    def login_info(self):
        self.implicitly_wait(15)
        counter = 1
        print('X'*50)
        print(f'[{counter}]{C.yellow} **[Starting BBY Sequence]**{reset}')
        time.sleep(2)
        self.get(BB.URL)
        if self.get:
            print(f'{C.yellow}[{counter}]** [Successfully loaded BBY page]{reset}')
        else:
            print(f'{C.red}[{counter}]** [FAILED TO LOAD BBY PAGE] **{reset}')

        print()
        print('X'*50)
        try:
            print(f'[{counter}]{C.yellow} **[Moving Display Banner]**{reset}')
            nav_copy = self.find_element_by_xpath('//*[@id="site-control-content"]')
            nav_copy.click()
            if nav_copy.click():
                print(f'{C.yellow}[{counter}]** [Successfully Averted Banner] **{reset}')
            else:
                print(f'{C.red}[{counter}]** [Failed to Avert Banner] **{reset}')
            print('X'*50)
            print()
        except Exception as e:
            print(f'{red}[{counter}]** [Failed to Avert Banner] **{reset}\n {str(e)}')
            print('X'*50)
            print()

    def first_page(self):
        print(f'**[PARSING GPU SEQUENCE]\n{yellow}*[NVIDIA GeForce RTX 3070 8GB GDDR6 PCI Express 4.0 Graphics Card - Dark Platinum and Black]{reset} ')
        self.get(BB.URL01)
        if self.get(BB.URL01):
            print(f'{yellow}**[RTX-3070 (8gb) Loaded{reset}')
        else:
            print(f'{red}**[FAIL TO LOAD] -- [RTX-3070 (8gb) {reset}')


    def iterate(self): ## may need to fix logix here
        try:
            time.sleep(2)
            ret = WebDriverWait(self, timer).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart-button")))
            ret.click()
            if ret.click():
                return 'True'
        except Exception as fail:
            print('error in checkout box iteration', str(fail))
            self.refresh()
    def click_thru_page(self):
        self.get("https://www.bestbuy.com/cart")

        checkoutBtn = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button")).click())
        if checkoutBtn == True:
            print("Successfully added to cart")


    def parse_login(self):
        nav_click00 = self.find_element_by_xpath(r'/html/body/div[2]/div/div/div[1]/header/div[2]/nav/ul/li[1]/div/button/span')
        nav_click00.click()
        print('1111')
        time.sleep(3)
        nav_click01 = self.find_element_by_xpath(r'/html/body/div[2]/div/div/div[1]/header/div[2]/nav/ul/li[1]/div/div/div/div[1]/div/div/div/div/div/a[1]')
        nav_click01.click()

        time.sleep(3)

        email_login = self.find_element_by_id("fld-e")
        email_login.click()
        email_login.send_keys(BBL.ADDR)

        print('33333')
        pword_login = self.find_element_by_id("fld-p1")
        pword_login.click()
        print('4444444')

        final_click = self.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/div/form/div[4]/button")
        final_click.click()

        print('555555555')

        pword_login.send_keys(BBL.PASS, Keys.ENTER)
        pword_login.click()
        time.sleep(5)


        ############ EMAIL FIELD ##############
        ############ EMAIL FIELD ##############
    def send_email(self): ## add email / password
        emailField = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e")).send_keys(bbyemail.ADDR))

        pwField = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1")).send_keys(bbyemail.PASS))

        signInBtn = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button")).click())

        print("Signing in")

        cvvField = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")

        placeOrderBtn = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track").click())
        )


    def card_and_order(self):
        EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")
        complete = false


