
from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from call import login_data
import time
class rich:
    def __init__(self):
        self.driver=webdriver.Chrome("/home/student/Downloads/chromedriver")
        self.wait = WebDriverWait(self.driver,15)
    def setup(self):
        self.driver.get("https://rrsso.onelogin.com/login")
        time.sleep(2)
        data=login_data()
        self.driver.find_element_by_xpath("//*[contains(@name,'email')]").send_keys(data["username"])
        self.driver.find_element_by_xpath("//*[contains(@name,'password')]").send_keys(data["password"])
        self.driver.save_screenshot("build/screenshot1.png")
        self.driver.find_element_by_xpath("//*[contains(@name,'commit')]").click()
        time.sleep(7)
    def log(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(@type,'button')]")))
        self.driver.find_element_by_xpath("//*[contains(@type,'button')]").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='apps-view-container']/div[2]/div/div/div/div/div[4]/a")))
        self.driver.find_element_by_xpath("//*[@id='apps-view-container']/div[2]/div/div/div/div/div[4]/a").click()
        self.driver.switch_to_window(self.driver.window_handles[1])        
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='select2-chosen-1']")))
        self.driver.find_element_by_xpath("//*[@id='select2-chosen-1']").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='s2id_autogen1_search']")))
        self.driver.find_element_by_xpath("//*[@id='s2id_autogen1_search']").send_keys("Carters")
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='select2-results-1']/li[1]")))
        self.driver.find_element_by_xpath("//*[@id='select2-results-1']/li[1]").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//a[contains(@href,'#recommendationsNavItem')]")))
        self.driver.find_element_by_xpath("//a[contains(@href,'#recommendationsNavItem')]").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//a[contains(@href,'//qa.richrelevance.com/rrportal/boostingRules.jsp')]")))
        self.driver.find_element_by_xpath("//a[contains(@href,'//qa.richrelevance.com/rrportal/boostingRules.jsp')]").click() 
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='searchFilter']")))
        self.driver.find_element_by_xpath("//*[@id='searchFilter']").send_keys("qa_test")
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='selectAll']")))
        k=self.driver.find_element_by_xpath("//*[@id='selectAll']")
        if(k):
            k.click()
            self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='deleteSelected']")))
            self.driver.find_element_by_xpath("//*[@id='deleteSelected']").click()
            self.driver.switch_to.alert.accept()
            self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='addRule']")))
        self.driver.find_element_by_xpath("//*[@id='addRule']").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='ruleName']")))
        self.driver.find_element_by_xpath("//*[@id='ruleName']").send_keys("qa_test")
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='noEndDate']")))
        self.driver.find_element_by_xpath("//*[@id='noEndDate']").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='categorySelector_filter']/div/div")))
        self.driver.find_element_by_xpath("//*[@id='categorySelector_filter']/div/div").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='s2id_autogen18']")))
        self.driver.find_element_by_xpath("//*[@id='s2id_autogen18']").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='s2id_autogen19_search']")))
        self.driver.find_element_by_xpath("//*[@id='s2id_autogen19_search']").send_keys("carter")
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[contains(@class,'select2-result-label')]")))
        self.driver.find_element_by_xpath("//*[contains(@class,'select2-result-label')]").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[contains(@class,'btn btn-default pull-right modal_close')]")))
        self.driver.find_element_by_xpath("//*[contains(@class,'btn btn-default pull-right modal_close')]").click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,"//*[contains(@id,'saveRule')]")))
        self.driver.find_element_by_xpath("//*[contains(@id,'saveRule')]").click()
        time.sleep(6)
        self.driver.save_screenshot("build/screenshot2.png")
        #self.driver.find_element_by_xpath("//*[@id='select2-result-label-32']").click()
        #time.sleep(4)
        #self.driver.find_element_by_xpath("//*[@id='modal_from_view1438']/div/div/div[3]/button").click()
        #time.sleep(4)
        #self.driver.find_element_by_xpath("//*[@id='saveRule']").click()
        #time.sleep(4)
    def teardown(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.close()
        print("task completed")
rich=rich()
rich.setup()
rich.log()
rich.teardown()

                
