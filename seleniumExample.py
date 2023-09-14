from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

options = Options()
# İstediğiniz seçenekleri burada ayarlayabilirsiniz, örneğin:
# options.add_argument("--headless")

# ChromeDriver'ı yönetmek için bir hizmet (service) oluşturun
chrome_service = ChromeService(ChromeDriverManager().install())

# WebDriver'ı başlatın ve hizmeti ve seçenekleri ileterek kullanın
driver = webdriver.Chrome(service=chrome_service, options=options)

driver.maximize_window()
driver.get("https://www.google.com/")
sleep(10)
while True:
   continue
#HTML LOCATORS
