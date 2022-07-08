# from selenium import webdriver
# import unittest
# from selenium.webdriver.common.keys import Keys
# import time
# from django.test import LiveServerTestCase

# cWait = 2
# class PageTest(LiveServerTestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()
# 	#def tearDown(self):
# 	#	self.browser.quit()

# 	def check_rows_in_listtable(self, row_text):
# 		start_time = time.time()
# 		while time.time()-start_time<cWait:
# 		#	time.sleep(0.2)
# 			try:
# 				table = self.browser.find_element_by_id('commissionTable')
# 				rows = table.find_elements_by_tag_name('tr')
# 				self.assertIn(row_text,[row.text for row in rows])
# 				return
# 			except (AssertionError,WebDriverException) as e:
# 				if time.time()-start_time>cWait:
# 					raise e

# 	def test_application_and_review(self):
# 		self.browser.get(self.live_server_url)
# 		#self.browser.get('http://localhost:8000')
# 		self.assertIn('Art Commission Scheduling', self.browser.title)
# 		headerText = self.browser.find_element_by_tag_name('h1').text
# 		self.assertIn('Art Commission Scheduling', headerText)
# 		ClientSurname = self.browser.find_element_by_id('cl_surname')
# 		ClientFirstname = self.browser.find_element_by_id('cl_firstname')
# 		ClientMiddlename = self.browser.find_element_by_id('cl_middlename')
# 		ClientContact = self.browser.find_element_by_id('cl_phonenum')
# 		ClientEmail = self.browser.find_element_by_id('cl_email')
# 		ClientGcash = self.browser.find_element_by_id('cl_gcashnum')
# 		ClientGcashreceipient = self.browser.find_element_by_id('gcashown')
# 		btn_Asched_button = self.browser.find_element_by_id('btnConfirm') 
# 		self.assertEqual(ClientSurname.get_attribute('placeholder'),'Enter your SurName here.')

# 		#Client Name
		
# 		ClientSurname.click()
# 		time.sleep(1)
# 		ClientSurname.send_keys('De Belen')
# 		time.sleep(1)
		
		
# 		ClientFirstname.click()
# 		time.sleep(1)
# 		ClientFirstname.send_keys('Cyren Kate')
# 		time.sleep(1)
		
		
# 		ClientMiddlename.click()
# 		time.sleep(1)
# 		ClientMiddlename.send_keys('Violeta')
# 		time.sleep(1)

		
# 		ClientContact.click()
# 		time.sleep(1)
# 		ClientContact.send_keys('0905-545-3471')
# 		time.sleep(1)

# 		#Client Email
		
# 		ClientEmail.click()
# 		time.sleep(1)
# 		ClientEmail.send_keys('cyrenkate.debelen@gsfe.tupcavite.edu.ph')
# 		time.sleep(1)

		
# 		ClientGcash.click()
# 		time.sleep(1)
# 		ClientGcash.send_keys('0975-379-5933')
# 		time.sleep(1)

		
# 		ClientGcashreceipient.click()
# 		time.sleep(1)
# 		ClientGcashreceipient.send_keys('Maggie Mae D.')
# 		time.sleep(1)

# 		# Button Confirmation for fill up form
# 		time.sleep(1)
# 		btn_Asched_button.click()
		

# 		ClientSurname = self.browser.find_element_by_id('cl_surname')
# 		ClientFirstname = self.browser.find_element_by_id('cl_firstname')
# 		ClientMiddlename = self.browser.find_element_by_id('cl_middlename')
# 		ClientContact = self.browser.find_element_by_id('cl_phonenum')
# 		ClientEmail = self.browser.find_element_by_id('cl_email')
# 		ClientGcash = self.browser.find_element_by_id('cl_gcashnum')
# 		ClientGcashreceipient = self.browser.find_element_by_id('gcashown')
# 		btn_Asched_button = self.browser.find_element_by_id('btnConfirm') 
# 		self.assertEqual(ClientSurname.get_attribute('placeholder'),'Enter your SurName here.')
		
		
# 		ClientSurname.click()
# 		time.sleep(1)
# 		ClientSurname.send_keys('Dela Cruz')
# 		time.sleep(1)

		
# 		ClientFirstname.click()
# 		time.sleep(1)
# 		ClientFirstname.send_keys('Juan')
# 		time.sleep(1)
		
# 		ClientMiddlename.click()
# 		time.sleep(1)
# 		ClientMiddlename.send_keys('Vicente')
# 		time.sleep(1)
		
# 		ClientContact.click()
# 		time.sleep(1)
# 		ClientContact.send_keys('1234-567-1545')
# 		time.sleep(1)

# 		#Client Email
		
# 		ClientEmail.click()
# 		time.sleep(1)
# 		ClientEmail.send_keys('juan.delacruz@gsfe.tupcavite.edu.ph')
# 		time.sleep(1)
		
# 		ClientGcash.click()
# 		time.sleep(1)
# 		ClientGcash.send_keys('0900-123-9932')
# 		time.sleep(1)
		
# 		ClientGcashreceipient.click()
# 		time.sleep(1)
# 		ClientGcashreceipient.send_keys('Cristine Hermesa')
# 		time.sleep(1)
		

		
# 		# Button Confirmation for fill up form
# 		time.sleep(1)
# 		btn_Asched_button.click()

# 		#self.check_rows_in_listtable('1: Juan Vicente Dela Cruz')
# 		self.check_rows_in_listtable('1: Cyren Kate Violeta De Belen 0905-545-3471 cyrenkate.debelen@gsfe.tupcavite.edu.ph 0975-379-5933 Maggie Mae D.')
# 		self.check_rows_in_listtable('2: Juan Vicente Dela Cruz 1234-567-1545 juan.delacruz@gsfe.tupcavite.edu.ph 0900-123-9932 Cristine Hermesa')
	
# 		#table = self.browser.find_element_by_id('commissionTable')
# 		#rows = table.find_elements_by_tag_name('tr')
# 		#self.assertIn('1: De Belen Cyren Kate Violeta 0905-545-3471 cyrenkate.debelen@gsfe.tupcavite.edu.ph 0975-379-5933 Maggie Mae D.',[row.text for row in rows])
		
# 		#self.assertTrue(any(row.text == '1: De Belen Cyren Kate Violeta'))


		
# 	def test_another_entry(self):
# 		self.browser.get(self.live_server_url)
# 		#self.browser.get('http://localhost:8000')
# 		self.assertIn('Art Commission Scheduling', self.browser.title)
# 		headerText = self.browser.find_element_by_tag_name('h1').text
# 		self.assertIn('Art Commission Scheduling', headerText)
# 		ClientSurname = self.browser.find_element_by_id('cl_surname')
# 		ClientFirstname = self.browser.find_element_by_id('cl_firstname')
# 		ClientMiddlename = self.browser.find_element_by_id('cl_middlename')
# 		ClientContact = self.browser.find_element_by_id('cl_phonenum')
# 		ClientEmail = self.browser.find_element_by_id('cl_email')
# 		ClientGcash = self.browser.find_element_by_id('cl_gcashnum')
# 		ClientGcashreceipient = self.browser.find_element_by_id('gcashown')
# 		btn_Asched_button = self.browser.find_element_by_id('btnConfirm') 
# 		self.assertEqual(ClientSurname.get_attribute('placeholder'),'Enter your SurName here.')
		
		
# 		ClientSurname.click()
# 		time.sleep(1)
# 		ClientSurname.send_keys('Dela Cruz')
# 		time.sleep(1)

		
# 		ClientFirstname.click()
# 		time.sleep(1)
# 		ClientFirstname.send_keys('Juan')
# 		time.sleep(1)
		
# 		ClientMiddlename.click()
# 		time.sleep(1)
# 		ClientMiddlename.send_keys('Vicente')
# 		time.sleep(1)
		
# 		ClientContact.click()
# 		time.sleep(1)
# 		ClientContact.send_keys('1234-567-1545')
# 		time.sleep(1)

# 		#Client Email
		
# 		ClientEmail.click()
# 		time.sleep(1)
# 		ClientEmail.send_keys('juan.delacruz@gsfe.tupcavite.edu.ph')
# 		time.sleep(1)
		
# 		ClientGcash.click()
# 		time.sleep(1)
# 		ClientGcash.send_keys('0900-123-9932')
# 		time.sleep(1)
		
# 		ClientGcashreceipient.click()
# 		time.sleep(1)
# 		ClientGcashreceipient.send_keys('Cristine Hermesa')
# 		time.sleep(1)
		

		
# 		# Button Confirmation for fill up form
# 		time.sleep(1)
# 		btn_Asched_button.click()
		
		
# 		self.check_rows_in_listtable('1: Juan Vicente Dela Cruz 1234-567-1545 juan.delacruz@gsfe.tupcavite.edu.ph 0900-123-9932 Cristine Hermesa')
		

# 		#self.checking_if_in_tabe_list( '1: Juan Vicente Dela Cruz')

# 		#inputbox = self.browser.find_element_by_id('idNewEntry')
# 		#self.assertEqual(inputbox.get_attribute('placeholder')), 'Persons name you have'
# 		#inputbox.send_keys('Mickey Mouse')
# 		#inputbox.send_keys(Keys.ENTER)
# 		#time.sleep(1)
# 		#table = self.browser.find_element_by_id('idListTable')
# 		#rows = table.find_element_by_tag_name('tr')
# 		#self.assertTrue(any(row.text == '1: Mickey Mouse'))

# #if __name__ == '__main__':
# #	unittest.main(warnings='ignore')