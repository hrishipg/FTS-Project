import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
UserDetails= "abc@grr.la"
Password = "ABCDqwe123!@#"


option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

driver.get("http://practice.automationtesting.in/")
myAccount = driver.find_element(By.XPATH,"//*[@id='menu-item-50']/a")
print("Cliking on My account option")
myAccount.click()

username = driver.find_element(By.ID,'username')
password = driver.find_element(By.ID,"password")
loginButton = driver.find_element(By.NAME,"login")
print("Entering User's details in Username field")
username.send_keys(UserDetails)
driver.implicitly_wait(5)
print("Entering Password in Password field")
password.send_keys(Password)
driver.implicitly_wait(5)
print("Clicking on Login button")
loginButton.click()
driver.implicitly_wait(5)
dashBoard = driver.find_element(By.XPATH,'//*[@id="page-36"]/div/div[1]/nav/ul/li[1]/a')
dashBoard.click()
driver.implicitly_wait(5)
logout = driver.find_element(By.XPATH,'//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a')
print("Clicking on Logout button")
logout.click()
driver.implicitly_wait(5)
print("Closing the browser")
driver.close()


