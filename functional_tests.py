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

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Services', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a Service'

        )
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Disease Similarity' for row in rows )
        )


        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
# Enter a disease or associated terms
# Obtain drugs indicated for the disease
# Obtain known side effects for the drugs
# Obtain drug-drug interactions for the disease data
# The  first change to 'functional_tests' after pushing to github

browser.quit()
