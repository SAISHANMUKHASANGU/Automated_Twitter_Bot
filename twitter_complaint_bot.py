import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PROMISED_DOWN=150
PROMISED_UP=10
CHROME_DRIVER_PATH="Users/shanu/development/chromedriver"
TWITTER_EMAIL="Your mail"
TWITTER_PASSWORD="Your password3"
USERNAME="Your username"

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.up=0
        self.down=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        self.pop_up=self.driver.find_element(By.XPATH,value='//*[@id="onetrust-accept-btn-handler"]')
        self.pop_up.click()
        time.sleep(3)
        self.go=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go.click()
        time.sleep(60)
        down=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down=down.text
        time.sleep(3)
        up=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up=up.text
        return
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(10)
        email=self.driver.find_element(By.NAME,value='text')
        email.send_keys(TWITTER_EMAIL)
        next_button=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        time.sleep(10)
        username=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(USERNAME)
        next_button2=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        next_button2.click()
        time.sleep(10)
        password= self.driver.find_element(By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD)
        login=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login.click()
        time.sleep(10)
        tweet_msg_input=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_msg=f"the network speed is: download={self.down},Upload={self.up}"
        tweet_msg_input.send_keys(tweet_msg)
        post=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()
        time.sleep(600)

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

