from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mok has trouble learning. So he went to see the home page
        # of the website that his friend introduced
        self.browser.get('http://localhost:8000')

        # He saw that the title of this website is EDU-Match
        self.assertIn('EDU-Match', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('EDU-Match', header_text)

        inputbox = self.browser.find_element_by_id('id_new_subject')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a Subject'
        )

        # He type the name of the subject that was not good
        # He type "Statistics in everyday life" into the Text box
        inputbox.send_keys('Statistics in everyday life')

        # When he press Enter, the page shows the name of a person who is good at "Statistics in everyday life"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Statistics in everyday life' for row in rows)
        )

        self.fail('Finish the test!')
    # From then, he added the names of subjects that he was not good at anymore

    # He typed "General Mathematics"

    # The webpage shows more people who specialize in "General Mathematics"

    # Later, he wanted to know what would happen if he typed a subject that didn't exist

    # The webpage shows the message "No match found. Ready to match. Please re-match later."

    # He takes the time to choose someone to tutor for a long time

    # He feels like this website very much

    # He therefore prepared the stuff to tutor

if __name__ == '__main__':
    unittest.main(warnings='ignore')