
# Author : Akshay Tripathi
# Description: Automating Amazon Shopping Cart with Selenium
# Version: 3.10.6
# Date: 16-Aug-2023

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonCartAutomation:

    def __init__(self):
        # Define the ChromeDriver executable path
        self.chromedriver_path = '/home/shtlp_0015/Downloads/Projects/AmazonAutomation/Drivers/chromedriver'
        
        # Set the executable path for the ChromeService
        os.environ["webdriver.chrome.driver"] = self.chromedriver_path
        
        # an instance of ChromeService and ChromeOptions
        self.service = ChromeService()
        #self.options = webdriver.ChromeOptions()
        
        # an instance of the Chrome WebDriver
        self.driver = webdriver.Chrome(service=self.service)

        self.driver.delete_all_cookies()
    
    def setup(self):
        # Maximize the browser window
        self.driver.maximize_window()
        
    def search_and_add_to_cart(self, product_name):
        # Open Amazon homepage
        self.driver.get("https://www.amazon.com/")
        
        # Find the search input field and enter the product name
        search_input = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_input.send_keys(product_name)
        
        # Submit the search
        search_input.submit()
        
        # Click on the first product
        first_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a")))
        first_product.click()
        
        # Add the product to the cart
        add_to_cart_button = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.ID, "wishListMainButton")))
        #id="exportsUndeliverable-cart-announce"
        add_to_cart_button.click()
    
    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    cart_automation = AmazonCartAutomation()
    cart_automation.setup()
    cart_automation.search_and_add_to_cart("Wireless Earbuds")
    cart_automation.close_browser()
