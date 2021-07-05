from selenium import webdriver
import unittest

class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PATH = "F:\chrome driver\chromedriver.exe"
        cls.driver = webdriver.Chrome(PATH)

        cls.driver.implicitly_wait(10)

        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")

        self.driver.find_element_by_name('q').send_keys("w3schools.com")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")







