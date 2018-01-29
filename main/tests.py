from django.test import TestCase
from main.models import Tag
from django.urls import reverse
from selenium import webdriver

# Create your tests here.

class ModelsTest(TestCase):

	def create_tag(self, name):
		return Tag.objects.create(name=name)

	def test_tag_creation(self):
		tag = self.create_tag("Sport")
		self.assertTrue(isinstance(tag, Tag))
		self.assertEqual(tag.name, "Sport")
		self.assertEqual(tag.__str__(), "Sport")

class ViewsTest(TestCase):

	def test_index_view(self):
		url = reverse("index")
		request = self.client.get(url)

		self.assertEqual(request.status_code, 200)
		# self.assertIn("Strona Adama", request.content)
class SignupTest(TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.hostname = "http://127.0.0.1:8000"
		self.successText = 'Account created successfully'
		self.successTextUserAlreadyRegistered = 'Użytkownik o tej nazwie już istnieje.'

	def test_sign_up(self):
		url = reverse("index")
		self.driver.get(self.hostname + url)
		self.driver.find_element_by_id('register_link').click()
		self.driver.find_element_by_id('id_username').send_keys('uzytkownikTestowy')
		self.driver.find_element_by_id('id_password1').send_keys('qwerty12345')
		self.driver.find_element_by_id('id_password2').send_keys('qwerty12345')
		self.driver.find_element_by_id('submit_register').click()
		page = self.driver.page_source
		self.assertIn(self.successTextUserAlreadyRegistered, page)

	def tearDown(self):
		self.driver.quit()