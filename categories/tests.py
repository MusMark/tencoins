from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from categories.models import Category
# Create your tests here.

class CategoryTestCase(APITestCase):

	def setUp(self):
		#Initialize solo category object
		cat_obj = Category.objects.create(name='Category 1')
		cat_obj.save()

	def test_single_category(self):
		#Check if object is added
		category_count = Category.objects.count()
		self.assertEqual(category_count, 1)

	def test_post_with_children(self):
		#create two more categories and check that amount of categories is equal to 3
		category = Category.objects.create(name='Category 2')
		sub_category = Category.objects.create(name='Category 2.1', parent=category)
		sub_category.save()
		category_count = Category.objects.count()
		self.assertEqual(category_count, 3)

	def test_get_category(self):
		#return first category object added and check status
		data = {}
		url = api_reverse("categories-app:list-category", kwargs={'pk' : 1})
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		print(response.data)


