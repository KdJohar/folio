from .models import GetBook, Book, Category
from rest_framework import serializers
from django.utils.text import slugify

class GetBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetBook


class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=250, allow_blank=True)
    class Meta:
        model = Book
        fields = ('title',
'isbn',
'slug',
'category',
'description',
'image',
'publisher',
'author',
'pages',
'language',
'download',
'date',
'featured',
'most_downloaded', 'category', )

    def create(self, validated_data):
        category_name = validated_data.get('category', '')
        validated_data.pop('category')
        book_obj = Book.objects.create(**validated_data)
        if category_name:
            category_name = category_name.lower()

            try:
                category = Category.objects.get(name=category_name)

            except Category.DoesNotExist, e:
                category = Category.objects.create(name=category_name, slug=slugify(category_name))

            book_obj.category = category
            book_obj.save()
        return book_obj







'''
'title',
'isbn',
'slug',
'category',
'description',
'image',
'publisher',
'author',
'pages',
'language ',
'download ',
'date = mode',
'featured',
'most_downloaded',

'''
