#
#Serialize data models - turn data into JSON and back
#

from rest_framework import serializers
from categories.models import Category
import json

class RecursiveSerializer(serializers.Serializer):
	def to_representation(self, value):
		serializer = self.parent.parent.__class__(value, context = self.context)
		return serializer.data


class CategorySerializer(serializers.ModelSerializer):

	children = RecursiveSerializer(many=True)
	depth = 3
	#parent = serializers.PrimaryKeyRelatedField()

	class Meta:
		model = Category
		fields = ['id', 'name', 'children', ]
		read_only_fields = ['id', ]


	def create(self, validated_data):
		category_data = validated_data.pop('children', None)  #returning empty OrderecDict()
		print(json.dumps(category_data))
		current_category = Category.objects.create(**validated_data) #first object parsed OK

		if category_data is not None:
			for elem in category_data: #loop through children nodes
				new_category = Category.objects.create(parent=current_category, **elem) #name not getting passed
				current_category.children.add(new_category)
			return current_category


	def validate_name(self, value):
		# validation of name duplicates
		qs = Category.objects.filter(name__iexact=value)
		if self.instance:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise serializers.ValidationError("Name already in use.")
		return value



