from rest_framework import serializers
from .models import Author, Book, Genre


class AuthorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        author = Author.objects.create(**validated_data)
        return author

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.biography = validated_data.get('biography', instance.biography)
        instance.save()
        return instance

    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        genre = Genre.objects.create(**validated_data)
        return genre

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = '__all__'
