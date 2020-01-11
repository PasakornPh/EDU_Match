from selenium import webdriver
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
        self.fail('Finish the test!')

    # He type the name of the subject that was not good

    # He type "Statistics in everyday life" into the Text box

    # When he press Enter, the page shows the name of a person who is good at "Statistics in everyday life"

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