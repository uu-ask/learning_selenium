import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class PythonOrgSerach(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("python",driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("about")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()