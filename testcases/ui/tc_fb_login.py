import pytest

from helpers import testconfig
from helpers import commonmethods as helper
from testdata.ui import td_fb_login as testdata
from pageobjects.ui import pg_fb_login
@pytest.mark.smoke
def test_verify_title(driver):
    helper.maximize(driver)
    driver.get(testconfig.base_url)
    helper.verify_page_title(driver,testdata.webpage_title)
    pg_fb_login.verify_text(driver)
    helper.close_browser(driver)
def test_verify_login_fail(driver):
    helper.maximize(driver)
    driver.get(testconfig.base_url)
    helper.verify_page_title(driver,testdata.webpage_title)
    pg_fb_login.verify_login(driver)
    helper.close_browser(driver)

@pytest.mark.smoke
@pytest.mark.parametrize("cred",helper.read_csv_cred())
def test_verify_login_csv(driver,cred):
    helper.maximize(driver)
    driver.get(testconfig.base_url)
    helper.verify_page_title(driver,testdata.webpage_title)
    pg_fb_login.verify_logincsv(driver,cred[0],cred[1])
    helper.close_browser(driver)

