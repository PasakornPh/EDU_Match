from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_edu_match_and_retrieve_it_later(self):
        # Mok has trouble learning. So he went to see the home page
        # of the website that his friend introduced
        self.browser.get(self.live_server_url)

        # He saw that the title of this website is EDU-Match
        self.assertIn('EDU-MATCH', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to EDU-Match', header_text)

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

        # table = self.browser.find_element_by_id('id_list_matching')
        # rows = table.find_elements_by_tag_name('tr')

        # She visits that URL - her to-do list is still there.
        self.fail('Finish the test!')

    def test_can_user_register_login_and_edit_profile(self):
        # ตอนนี้ หมอกยังไม่ได้เป็นสมาชิก
        # ดังนั้น เขาจึงสมัครสมาชิก
        self.browser.get(self.live_server_url + '/signup')
        # เขาเห็นว่า title มีชื่อว่า Sign Up
        # ซึ่งเเสดงว่าเขาเข้ามาถูก
        self.assertIn('Sign Up', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Sign up into Website', header_text)

        # เขาจึงใส่ username เป็น somsak
        inputusername = self.browser.find_element_by_id('id_username')
        inputusername.send_keys('somsak')

        # เขาได้ใส่ชื่อเเละนามสกุลเป็น Pasakorn Phareyart เเต่เขาใส่ชื่อผิด จึงเป็น Paskorn
        input_firstname = self.browser.find_element_by_id('id_first_name')
        input_firstname.send_keys('Paskorn')
        input_lastname = self.browser.find_element_by_id('id_last_name')
        input_lastname.send_keys('Phareyart')

      # เขาได้ใส่ E-mail เป็น example@gmail.com
        input_email = self.browser.find_element_by_id('id_email')
        input_email.send_keys('example@gmail.com')

        # ต่อมาเขาใส่รหัสเป็น mok123456789
        inputpassword = self.browser.find_element_by_id('id_password1')
        inputpassword.send_keys('mok123456789')
        inputpassword2 = self.browser.find_element_by_id('id_password2')
        inputpassword2.send_keys('mok123456789')

        # เขาจึงกดปุ่ม Enter
        inputpassword2.send_keys(Keys.ENTER)
        time.sleep(1)

        # เมื่อเขาสมัครสมาชิกเสร็จเเล้ว
        # เขาจึงไปที่หน้า login
        self.assertIn('Login', self.browser.title)

        # เขาพิมพ์ Username เเละ password ลงไป
        # เขาจึงใส่ username เป็น somsak
        inputusername_login = self.browser.find_element_by_id('id_username')
        inputusername_login.send_keys('somsak')

        # ต่อมาเขาใส่รหัสเป็น mok123456789
        inputpassword = self.browser.find_element_by_id('id_password')
        inputpassword.send_keys('mok123456789')

        # จากนั้นเขาจึงกดปุ่ม Enter
        inputpassword.send_keys(Keys.ENTER)
        time.sleep(3)

        # เขาสังเกตเห็นว่าชื่อที่ปรากฏผิดจาก Pasakorn เป็น Paskorn
        name_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Paskorn', name_text)

        # เขาจึงเข้าไปที่หน้า Profile เพื่อแก้ไข
        text_profile = self.browser.find_element_by_id('id_profile')
        text_profile.send_keys(Keys.ENTER)
        time.sleep(1)

        self.assertIn('Profile', self.browser.title)

        # เขาเห็นชื่อที่ผิดรากฏอยู่ที่ textinput
        input_firstname_profile = self.browser.find_element_by_id('id_first_name')
        #print(input_firstname_profile)
        self.assertIn('Paskorn', input_firstname_profile.get_attribute("value"))

        # เขาจึงลบชื่อที่ผิดเเละเเก้เป็น Pasakorn
        input_firstname_profile.clear()
        input_firstname_profile.send_keys('Pasakorn')

        # จากนั้นเขาก็กด Enter
        input_firstname_profile.send_keys(Keys.ENTER)
        time.sleep(1)

        # เขาสังเกตเห็นว่าชื่อที่ปรากฏเป็น Pasakorn ซึ่งเป็นชื่อที่เขาต้องการ
        name_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Pasakorn', name_text)

        self.test_can_user_change_password()

        # หลังจากที่เขาเล่นเว็บ EDU-Match เสร็จเเล้ว
        # เขาจึงกดไปที่ Log out
        self.fail('Finish the test!')

    def test_can_user_change_password(self):
        # หลังจากที่เข้าสมัครเเละเปลียนชื่อเรียบร้อยเเล้ว
        # เขาจีงต้องการที่จะเปลี่ยนรหัสของเขา
        # เขาจึงเข้ามาที่หน้าเปลี่ยนรหัส
        self.browser.get(self.live_server_url + '/accounts/change_password/')
        time.sleep(1)

        # จากนั้นเห็นอีกว่าหัวข้อของหน้านี้คือ Change Password
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Change Password', header_text)

        # เมื่อเขาเข้ามาที่หน้านี้ เขาจึงใส่รหัสเก่าของเขาที่ช่อง Old password
        old_password = self.browser.find_element_by_id('id_old_password')
        old_password.send_keys('mok123456789')

        # จากนั้นเขาก็ใส่รหัสใหม่ของเขาคือ mok987654321
        new_password1 = self.browser.find_element_by_id('id_new_password1')
        new_password1.send_keys('mok987654321')

        # เเละยืนยันรหัสอีก 1 รอบ
        new_password2 = self.browser.find_element_by_id('id_new_password2')
        new_password2.send_keys('mok987654321')

        # เเละกดปุ่ม Enter
        new_password2.send_keys(Keys.ENTER)
        time.sleep(1)

        # เขาสังเกตเห็นคำว่า Password changed with success
        success_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Password changed with success!!!', success_text)

        # เเละเห็นคำว่า Logout ที่มันสามารถกดได้
        # เขาจึงกดคำนั้นเพื่อ Login ใหม่อีกครั้ง
        link_logout = self.browser.find_element_by_id('id_logout')
        link_logout.send_keys(Keys.ENTER)
        time.sleep(1)

        # เขามาที่หน้า Login เเล้ว เขาจึงใส่รหัสใหม่ทันที
        self.assertIn('Login', self.browser.title)

        # เขาพิมพ์ Username เเละ password ลงไป
        # เขาจึงใส่ username เป็น somsak
        inputusername_login = self.browser.find_element_by_id('id_username')
        inputusername_login.send_keys('somsak')

        # ต่อมาเขาใส่รหัสเป็น mok987654321
        inputpassword = self.browser.find_element_by_id('id_password')
        inputpassword.send_keys('mok987654321')

        # จากนั้นเขาจึงกดปุ่ม Enter
        inputpassword.send_keys(Keys.ENTER)
        time.sleep(1)

        # เเละในที่สุดรหัสของเขาก็ได้ถูกเปลี่ยนไปเเล้ว
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to EDU-Match', header_text)

        self.fail('Finish the test!')


    def test_to_search_for_matching(self):
        self.browser.get(self.live_server_url + '/signup')
        # เขาเห็นว่า title มีชื่อว่า Sign Up
        # ซึ่งเเสดงว่าเขาเข้ามาถูก
        self.assertIn('Sign Up', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Sign up into Website', header_text)

        # เขาจึงใส่ username เป็น detmonmok
        inputusername = self.browser.find_element_by_id('id_username')
        inputusername.send_keys('detmonmok')

        # ต่อมาเขาใส่รหัสเป็น mok123456789
        inputpassword = self.browser.find_element_by_id('id_password1')
        inputpassword.send_keys('mok123456789')
        inputpassword2 = self.browser.find_element_by_id('id_password2')
        inputpassword2.send_keys('mok123456789')

        # เขาจึงกดปุ่ม Enter
        inputpassword2.send_keys(Keys.ENTER)
        time.sleep(1)


        self.browser.get(self.live_server_url + '/account/login/')

        # เขาพิมพ์ Username เเละ password ลงไป
        # เขาจึงใส่ username เป็น moklnwza
        inputusername = self.browser.find_element_by_id('id_username')
        inputusername.send_keys('detmonmok')

        # ต่อมาเขาใส่รหัสเป็น Mokza007
        inputpassword = self.browser.find_element_by_id('id_password')
        inputpassword.send_keys('mok123456789')

        # จากนั้นเขาจึงกดปุ่ม Enter
        inputpassword.send_keys(Keys.ENTER)
        time.sleep(1)


        # From then, he added the names of subjects that he was not good at anymore
        self.browser.get(self.live_server_url)
        self.assertIn('EDU-MATCH', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to My Site , Hello Pasakorn !', header_text)

        inputbox = self.browser.find_element_by_id('id_new_subject')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a Subject'
        )
        # He typed "General Mathematics"
        inputbox.send_keys('General Mathematics')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    # The webpage shows more people who specialize in "General Mathematics"
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1:kitsanapong', [row.text for row in rows])
    # Later, he wanted to know what would happen if he typed a subject that didn't exist
        inputbox.send_keys('Nothing')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    # The webpage shows the message "No match found. Ready to match. Please re-match later."
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('No users were found matching', [row.text for row in rows])
        self.fail('Finish the test!')
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

