from testdata.ui import td_fb_login as testdata
from helpers import commonmethods as helper

fb_subtitle_locator = "//*[@class='_8eso']"
fb_email = "//*[@name='email']"
fb_pass = "//*[@name='pass']"
fb_login_btn = "//*[@name='login']"
def verify_text(driver):
    try:
        txt = helper.get_element(driver, fb_subtitle_locator).text
        assert txt == testdata.sub_title
        helper.log("sub title verified","info")
    except AssertionError as e:
        helper.log("Error in sub title verification - "+str(e),"error")

def verify_login(driver):
    try:
        helper.get_element(driver, fb_email).send_keys(testdata.email)
        helper.get_element(driver, fb_pass).send_keys(testdata.password)
        helper.get_element(driver, fb_login_btn).click()
        helper.log("login verified", "info")
    except AssertionError as e:
        helper.log("Error in login verification - " + str(e), "error")


def verify_logincsv(driver,username,password):
    try:
        helper.get_element(driver, fb_email).send_keys(username)
        helper.get_element(driver, fb_pass).send_keys(password)
        helper.get_element(driver, fb_login_btn).click()
        helper.log("login verified", "info")
    except AssertionError as e:
        helper.log("Error in login verification - " + str(e), "error")