# '''from django.urls import resolve'''
# from django.test import TestCase
# from asched.views import MainPage
# #from django.http import HttpRequest
# from asched.models import item

# class HomePageTest(TestCase):

# 	def test_mainpage_as_seen_slient(self):
# 		response = self.client.get('/')
# 		self.assertTemplateUsed(response,'mainpage.html')
	
# 	def test_save_POST_request(self):
# 		response = self.client.post('/',data={
# 			'cl_surname': 'newcl_surname',
# 			'cl_firstname': 'newcl_firstname', 
# 			'cl_middlename': 'newcl_middlename',
# 			'cl_phonenum': 'newcl_phonenum', 
# 			'cl_email': 'newcl_email', 
# 			'cl_gcashnum': 'newcl_gcashnum', 
# 			'gcashown': 'newgcashown'})
		
# 		self.assertEqual(item.objects.count(), 1)
# 		newEntry = item.objects.first()
# 		self.assertEqual(newEntry.sname, 'newcl_surname')

# 		#self.assertIn('newsurname', response.content.decode())	
# 		#self.assertTemplateUsed(response,'mainpage.html')

# 	def test_redirect_POST(self):
# 		response = self.client.post('/',data={
# 			'cl_surname': 'newcl_surname',
# 			'cl_firstname': 'newcl_firstname', 
# 			'cl_middlename': 'newcl_middlename',
# 			'cl_phonenum': 'newcl_phonenum', 
# 			'cl_email': 'newcl_email', 
# 			'cl_gcashnum': 'newcl_gcashnum', 
# 			'gcashown': 'newgcashown'})
		
# 		self.assertEqual(response.status_code, 302)
# 		self.assertEqual(response['location'], '/')

# 	def test_only_saves_items_if_necessary(self):
# 		self.client.get('/')
# 		self.assertEqual(item.objects.count(), 0)
	


# class ORMTest(TestCase):
# 	def test_saving_retrieving_list(self):
# 		entry1 = item()
# 		entry1.fname = 'Cyren Kate'
# 		entry1.mname = 'Violeta'
# 		entry1.sname = 'De Belen'
# 		entry1.email = 'cyrenkate.debelen@gsfe.tupcavite.edu.ph'
# 		entry1.contact = '0905-545-3471'
# 		entry1.gcashnum= '0975-379-5933'
# 		entry1.gcashown= 'Maggie Mae D.'
# 		entry1.save()
# 		entry2 = item()
# 		entry2.fname = 'Juan'
# 		entry2.mname = 'Vicente'
# 		entry2.sname = 'Dela Cruz'
# 		entry2.email = 'juan.delacruz@gsfe.tupcavite.edu.ph'
# 		entry2.contact = '1234-567-1545'
# 		entry2.gcashnum= '0900-123-9932'
# 		entry2.gcashown= 'Cristine Hermesa'
# 		entry2.save()
# 		items = item.objects.all()
# 		self.assertEqual(items.count(), 2)
# 		items1 = items[0]
# 		items2 = items[1]
# 		self.assertEqual(items1.fname, 'Cyren Kate')
# 		self.assertEqual(items2.fname, 'Juan')

# 	def test_template_displays_list(self):
# 		item.objects.create(sname='De Belen')
# 		item.objects.create(sname='Dela Cruz')
# 		response = self.client.get('/')
# 		self.assertIn('De Belen', response.content.decode())
# 		self.assertIn('Dela Cruz', response.content.decode())


# """
	
# 	def test_root_url_resolves_to_mainpage_view(self):
# 		found = resolve('/')
# 		self.assertEqual(found.func, MainPage)
		
# 	def test_mainpage_if_responding_view(self):
# 		response=self.client.get('/')
# 		'''request = HttpRequest()
# 		response = MainPage(request)'''
# 		html = response.content.decode('utf8')
# 		'''(deleted)
# 		self.assertTrue(html.startswith('<!DOCTYPE html>'))
# 		self.assertIn('<title>Art Commission Scheduling</title>', html)
# 		self.assertTrue(html.endswith(''))'''
# 		stringPage=render_to_string('mainpage.html')
# 		self.assertEqual(html, stringPage)
# 		self.assertTemplateUsed(response,'mainpage.html')
# """