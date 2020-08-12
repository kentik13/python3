from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


server="http://94.125.123.164/"

login="admin@tycomonitor.com"
passwd="Admin123"

while(True): # each 6 min
    driver = webdriver.Chrome('/home/antond/performance/dev/sandbox/Anton/chromedriver')
    #open server window and login
    driver.get(server)
    #driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/form/div/div[2]/label[1]/span/input").send_keys(login)
    driver.find_element_by_xpath("//*[@id='root']/div/form/div/div[2]/label[2]/span/input").send_keys(passwd)
    driver.find_element_by_xpath("//*[@id='root']/div/form/div/div[3]/button/span").click()


    #uncomment only first time for choose by 200 panels
    #time.sleep(1)
    #driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[3]/div[1]").click()
    #time.sleep(1)
    #driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[4]").click()

    #select 1000 panels
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/span/label/span").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[5]/div[2]/button[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/span/label/span").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[5]/div[2]/button[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/span/label/span").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[5]/div[2]/button[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/span/label/span").click()
    time.sleep(1)
    # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[5]/div[2]/button[2]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/span/label/span").click()
    # time.sleep(3)s


    #service->delete->yes
    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]/div[2]/span").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[9]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[2]/div/div/div[3]/button[2]/span").click()
    time.sleep(14)

    #quit
    driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[2]/div[5]").click()
    driver.quit()
