from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

options = Options()
# İstediğiniz seçenekleri burada ayarlayabilirsiniz, örneğin:
# options.add_argument("--headless")

##driver= webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver_path = ChromeDriverManager().install()  # ChromeDriver'ı indirip yükler
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
#sleep(10)
while True:
   continue
#HTML LOCATORS
