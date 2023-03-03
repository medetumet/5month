from movie_app.views import *
from rest_framework import serializers
from movie_app.models import *


class DirectorSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = '__all__'
    def get_count_movie(self, directors):
        r = directors.movie.all()
        return len(r)

class MovieSerializers(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class MovieReviewSerializers(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'
    def average_rating(self, movie):
        r = [review.stars for review in movie.reviews.all()]
        return sum(r) / len(r)
