from movie_app.views import *
from rest_framework import serializers
from movie_app.models import *
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = '__all__'
    def get_count_movie(self, directors):
        r = directors.movie.all()
        return len(r)

class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class MovieReviewSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'id title description duration director rating model fields'.split()
    def average_rating(self, movie):
        r = [review.stars for review in movie.reviews.all()]
        return sum(r) / len(r)

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    director = serializers.IntegerField()
    duration = serializers.IntegerField()

    def validate_director(self, director):
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError("Director not found!")
        return director


class MovieCreateSerializer(MovieValidateSerializer):
    def validate_title(self, title):
        if Movie.objects.filter(title=title).count() > 0:
            raise ValidationError("title must be unique!")
        return title


class MovieUpdateSerializer(MovieValidateSerializer):
       def validate_title(self, title):
        if Movie.objects.filter(title=title).exclude(id=self.context.get("id")).count() > 0:
            raise ValidationError("title must be unique!")
        return title

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, name):
        if Director.objects.filter(name=name).count() > 0:
            raise ValidationError("name must be unique!")
        return name

class DirectorUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, name):
        if Director.objects.filter(name=name).exclude(id=self.context.get("id")).count() > 0:
            raise ValidationError("name must be unique!")
        return name

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError("Movie not found!")
        return movie

