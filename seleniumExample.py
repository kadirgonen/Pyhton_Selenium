from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver= webdriver.Chrome(ChromeDriverManager().install)
driver.maximize_window()
driver.get("https://www.google.com/")
#sleep(10)
while True:
   continue
#HTML LOCATORS
