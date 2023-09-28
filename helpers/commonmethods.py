import datetime
import logging
import logging as logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import csv

from helpers import testconfig

logger.basicConfig(filename='../../reports/logs/fb.log', datefmt='%m/%d/%Y %I:%M:%S %p',filemode='w',encoding='utf-8',level=logger.DEBUG)

"""
    This function is used to capture the logs
    input : message and type of message
    return: None  
"""
def log(msg,type):
    nw = datetime.datetime.now()
    if type=="error":
        logger.error(msg+" - "+str(nw))
    elif type == "info":
        logger.info(msg+" - "+str(nw))
def verify_page_title(driver,exptitle):
    try:
        assert driver.title == exptitle
        log("Web Page title verified","info")
    except AssertionError as e:
        print("Error in title verification - ",str(e))
        log("Error in title verification - "+str(e),"error")

def maximize(driver):
    driver.maximize_window()

def get_element(driver,locator):
    try:
        wait = WebDriverWait(driver, 10)
        web_element =wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return web_element
    except Exception as e:
        log("Error in element finding - "+str(e),"error")
        return None
def close_browser(driver):
    driver.close()

def read_csv_cred():
    with open(testconfig.csv_cred_path, mode='r') as file:
        csvreader = csv.reader(file)
        creds =[]
        for lines in csvreader:
            creds.append([lines[0],lines[1]])
    return creds