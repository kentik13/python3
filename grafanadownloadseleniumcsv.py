from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os

option = webdriver.ChromeOptions()
preferances = {"download.default_directory": "/home/antond/performance/dev/sandbox/Anton/Dashboard to csv/Download/"} # put your path!
option.add_experimental_option("prefs", preferances)
driver = webdriver.Chrome(options=option)
actions=ActionChains(driver)

user = "admin"                   #input username
password = "gHjvtntec19#"        #input password
server = "ua161ipmp0.visonic.com" #input your server
time_from = "2020-06-23 00:00:00" # time from
time_to = "2020-06-24 00:00:00"   # time to

#open url
driver.maximize_window()
driver.get("http://192.168.10.43:3000/login")

#login
driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_xpath("//*[@id='login-view']/form/div[3]/button").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='panel-3']/div/div/div/plugin-component/panel-plugin-dashlist/grafana-panel/div/div[2]/ng-transclude/div/div[1]/div/div[1]/a/span[1]").click()
time.sleep(1)

# #server selection
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[2]/div/div[1]/div/div[1]/dashboard-submenu/div/div[1]/div/value-select-dropdown/div/a").click()
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[2]/div/div[1]/div/div[1]/dashboard-submenu/div/div[1]/div/value-select-dropdown/div/input").send_keys(server)
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[2]/div/div[1]/div/div[1]/dashboard-submenu/div/div[1]/div/value-select-dropdown/div/div/div").click()
#
# #time range selection:
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div/div/button").click()
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div/div/button").send_keys(Keys.RETURN)
# #time from
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/input").clear()
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/input").send_keys(time_from)
# #time to
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/input").clear()
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/input").send_keys(time_to)
# #appliy
# driver.find_element_by_xpath("/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div[2]/div[2]/button").click()


##############################################################################
##############################Load / Software stats and limits################
##############################################################################

# #Connected Panels csv download
# driver.find_element_by_xpath("//*[text()='Connected Panels']").click()
# more=driver.find_element_by_xpath("//*[text()='More ...']")
# export_csv=driver.find_element_by_xpath("//*[text()='Export CSV']")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/Connected Panels.csv')


# #Discovery count csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='Discovery count']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-52']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-52']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/Discovery count.csv')
#
# #Offlene BBA and GPRS events csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='Offline BBA and GPRS events']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-56']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-56']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/Offline BBA and GPRS events.csv')
#
# # Online BBA and GPRS events csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='Online BBA and GPRS events']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-54']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-54']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/Online BBA and GPRS events.csv')
#
# # Processed films frames csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='Processed films frames']").location_once_scrolled_into_view
# driver.find_element_by_xpath("//*[text()='Processed films frames']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-62']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-62']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/Processed films frames.csv')
#
# # Total/video events rate csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='Total/video events rate']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-64']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-64']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/Total video events rate.csv')
#
# # itv2, fibro and pmax events rate csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='itv2, fibro and pmax events rate']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-58']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-58']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/itv2, fibro and pmax events rate.csv')
#
# # itv2, fibro and pmax events latency csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='itv2, fibro and pmax events latency']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-60']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-60']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/software/itv2, fibro and pmax events latency.csv')

##############################################################################
##############################Hardware stats and limits#######################
##############################################################################

#change location to Load / Hardware stats and limits
driver.find_element_by_xpath("//*[text()='Load / Hardware stats and limits']").click()
time.sleep(1)

# # CPU csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='CPU']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-98']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-98']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/hardware/CPU.csv')
#
# # CPU System csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='CPU System']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-134']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-134']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/hardware/CPU System.csv')
#
# # CPU User csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='CPU User']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-102']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-102']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/hardware/CPU User.csv')
#
#
# # Load avarage csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='Load avarage']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-100']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-100']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/hardware/Load avarage.csv')


##############################################################################
##############################MySQL Performance################################
##############################################################################

driver.find_element_by_xpath("//*[text()='MySQL Overview']").click()
time.sleep(1)

# MySQL Connections csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='MySQL Connections']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-92']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-92']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/mysql/MySQL Connections.csv')

# # MySQL Client Thread Activity csv download
# actions=ActionChains(driver)
# driver.find_element_by_xpath("//*[text()='MySQL Client Thread Activity']").click()
# more=driver.find_element_by_xpath("//*[@id='panel-10']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
# export_csv=driver.find_element_by_xpath("//*[@id='panel-10']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
# actions.move_to_element(more).move_to_element(export_csv).click().perform()
# driver.find_element_by_xpath("//*[text()='Export']").click()
# time.sleep(1)
# os.rename('Download/grafana_data_export.csv','Ready/mysql/MySQL Client Thread Activity.csv')


# MySQL Questions csv download
actions=ActionChains(driver)
driver.find_element_by_xpath("//*[text()='MySQL Questions']").click()
more=driver.find_element_by_xpath("//*[@id='panel-53']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/a/span")
export_csv=driver.find_element_by_xpath("//*[@id='panel-53']/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[5]/ul/li[4]/a/span")
actions.move_to_element(more).move_to_element(export_csv).click().perform()
driver.find_element_by_xpath("//*[text()='Export']").click()
time.sleep(1)
os.rename('Download/grafana_data_export.csv','Ready/mysql/MySQL Questions.csv')

# driver.quit()
