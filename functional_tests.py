from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_user_register(self):
        # ตอนนี้ หมอกยังไม่ได้เป็นสมาชิก
        # ดังนั้น เขาจึงสมัครสมาชิก
        self.browser.get('http://localhost:8000/signup')
        # เขาเห็นว่า title มีชื่อว่า Sign Up
        # ซึ่งเเสดงว่าเขาเข้ามาถูก
        self.assertIn('Sign Up', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Sign up into Website', header_text)

        # เขาจึงใส่ username เป็น moklnwza
        inputusername = self.browser.find_element_by_id('id_username')
        inputusername.send_keys('moklnwza')

        # ต่อมาเขาใส่รหัสเป็น Mokza007
        inputpassword = self.browser.find_element_by_id('id_password1')
        inputpassword.send_keys('Mokza007')
        inputpassword2 = self.browser.find_element_by_id('id_password2')
        inputpassword2.send_keys('Mokza007')

        # เขาจึงกดปุ่ม Enter
        inputpassword2.send_keys(Keys.ENTER)
        time.sleep(1)

        # เขาได้เห็นจำนวนผู้ที่สมัครเพิ่มขึ้น
        count_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered', count_text)

        self.fail('Finish the test!')


    def test_can_start_edu_match_and_retrieve_it_later(self):
        # Mok has trouble learning. So he went to see the home page
        # of the website that his friend introduced
        self.browser.get('http://localhost:8000/home')

        # He saw that the title of this website is EDU-Match
        self.assertIn('EDU-MATCH', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to My Site', header_text)

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

    # From then, he added the names of subjects that he was not good at anymore

    # He typed "General Mathematics"

    # The webpage shows more people who specialize in "General Mathematics"

    # Later, he wanted to know what would happen if he typed a subject that didn't exist

    # The webpage shows the message "No match found. Ready to match. Please re-match later."

    # He takes the time to choose someone to tutor for a long time

    # He feels like this website very much

    # He therefore prepared the stuff to tutor

#        # He click on Profile button
#         buttontoprofile = self.browser.find_element_by_id('id_to_profile')
#         buttontoprofile.send_keys(Keys.ENTER)
#         self.browser.get('http://localhost:8000/profile')
        # He saw that the header of this website is My profile
#        pheader_text = self.browser.find_element_by_tag_name('h2').text
#        self.assertIn('My Profile', pheader_text)
        # He type his favorite subject
        # He type "Math2" and "Biology" into the Text box
#        inputbox = self.browser.find_element_by_id('id_new_subject')
#        inputbox.send_keys('Math2')
#        inputbox.send_keys(Keys.ENTER)
#        time.sleep(1)
#        inputbox = self.browser.find_element_by_id('id_new_subject')
#        inputbox.send_keys('Biology')
#        inputbox.send_keys(Keys.ENTER)
#        time.sleep(1)

        # The page shows both subject on his list
#        table = self.browser.find_element_by_id('id_list_table')
#        rows = table.find_elements_by_tag_name('tr')
#        self.assertIn('1: Math2', [row.text for row in rows])
#        self.assertIn(
#            '2: Biology',
#             [row.text for row in rows]
#        )
        # He select Biology and Math2 subject for remove and press remove
#        checkbox1 = self.browser.find_element_by_id('new_subject1')
#        checkbox1.send_keys(Keys.SPACE)
#        checkbox2 = self.browser.find_element_by_id('new_subject2')
#        checkbox2.send_keys(Keys.SPACE)
#        deletebutton = self.browser.find_element_by_id('id_delete_subject')
#        deletebutton.send_keys(Keys.ENTER)

        # She visits that URL - her to-do list is still there.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')