from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver= webdriver.Chrome(ChromeDriverManager().install)
sleep(10)