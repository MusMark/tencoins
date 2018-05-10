#
# create view endpoints for API
#

from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryAdd(generics.CreateAPIView):
	# POST API Endpoint - callable through /categories/

	lookup_field = 'pk'
	serializer_class = CategorySerializer

	def get_queryset(self):
		return Category.objects.all()


class CategoryList(generics.RetrieveAPIView):
	#GET API Endpoint - callable through /categories/<id>

	lookup_field = 'pk'
	serializer_class = CategorySerializer
	queryset = Category.objects.all()

	def get_queryset(self):
		return Category.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}






