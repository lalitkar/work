from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()
browser.get('http://192.168.3.232:8080/login')
user_field=browser.find_element_by_name('uname')
pass_field=browser.find_element_by_name('pw')
user_field.send_keys('abc')
pass_field.send_keys('xyz')
pass_field.send_keys(Keys.RETURN)
try:
    assert 'log' in browser.title
    print('test case success')
except AssertionError:
    print('test failed')
finally:
    import time
    time.sleep(2)
    browser.close()
import unittest
class mytest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        print('in setup')
    def test_testcase1(self):
        browser=self.browser
        browser.get('http://192.168.3.232:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('test1 passed')
    def test_testcase2(self):
        browser=self.browser
        browser.get('http://192.168.3.232:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('test 2 pass')
    def test_testcase3(self):
        browser=self.browser
        browser.get('http://192.168.3.232:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('test 3 pass')
    def tearDown(self):
        print('in tear down')
        import time
        time.sleep(2)
        browser.close()
if __name__=='__main__':
    unittest.main()