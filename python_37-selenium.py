from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
import time

options = webdriver.FirefoxOptions()
# options.add_argument("--headless") # uncomment to run firefox without GUI

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://www.google.com")

time.sleep(5)
driver.quit()


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://www.github.com/login")
time.sleep(5)

username_field = driver.find_element(By.ID, "login_field")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("username")
password_field.send_keys("password")

login_button = driver.find_element(By.NAME, "commit")
login_button.click()

time.sleep(5)
driver.quit()


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://www.example.com")
time.sleep(2)

link = driver.find_element(By.TAG_NAME, "a")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])

print("Title of the new page:", driver.title)
driver.switch_to.window(windows[0])

time.sleep(2)
driver.quit()


options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://www.example.com")
time.sleep(2)

driver.quit()