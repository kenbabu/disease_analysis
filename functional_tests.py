from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# assert  'Services' in browser.title

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_show_a_list_of_services(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Services', self.browser.title)
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
# Enter a disease or associated terms
# Obtain drugs indicated for the disease
# Obtain known side effects for the drugs
# Obtain drug-drug interactions for the disease data
# The  first change to 'functional_tests' after pushing to github

browser.quit()
