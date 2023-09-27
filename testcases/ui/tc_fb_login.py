from helpers import testconfig
from helpers import commonmethods as helper
from testdata.ui import td_fb_login as testdata
from pageobjects.ui import pg_fb_login
def test_verify_title(driver):
    helper.maximize(driver)
    driver.get(testconfig.base_url)
    helper.verify_page_title(driver,testdata.webpage_title)
    pg_fb_login.verify_text(driver)

def test_verify_login_fail(driver):
    helper.maximize()
    driver.get(testconfig.base_url)
    helper.verify_page_title(driver,testdata.webpage_title)
    pg_fb_login.verify_login(driver)