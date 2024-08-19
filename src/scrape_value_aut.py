from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time 
from selenium.webdriver.common.keys import Keys

service = Service('C:\\Users\\jayes\\Downloads\\chromedriver.exe')


def clean_text(text):
  """Extract only temprature from the text"""
  output = float(text.split(": ") [1])
  return output

def get_driver():
#Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(service = service,options = options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def main():
  driver = get_driver()
  driver.find_element(by = "id",value ="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by = "id", value = "id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value= "/html/body/nav/div/a").click()
  time.sleep(2)

  text = driver.find_element(by ="xpath", value = "/html/body/div[1]/div/h1[2]").text
  return clean_text(text)

print(main())