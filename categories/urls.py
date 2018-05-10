from .views import CategoryAdd, CategoryList
from django.urls import path, re_path

app_name = 'categories-app'

urlpatterns = [
	path('', CategoryAdd.as_view(), name='add-category'), #POST EndPoint
	re_path(r'^(?P<pk>\d+)/$', CategoryList.as_view(), name='list-category') #GET EndPoint
]
