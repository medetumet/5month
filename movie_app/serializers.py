from movie_app.views import *
from rest_framework import serializers
from movie_app.models import *
from rest_framework.exceptions import ValidationError

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
        fields = 'id title description duration director rating model fields'.split()
    def average_rating(self, movie):
        r = [review.stars for review in movie.reviews.all()]
        return sum(r) / len(r)

class MovieValidateSerialiser(serializers.Serializer):
    title = serializers.CharField(max_length=200, min_length=3)
    description = serialisers.CharField(requaired=False)
    duration = serializers.FloatField()
    director = serializers.TextField()
    category_id = serializers.IntegerField()
    review = serializers.CharField()

    def validate_category_id(self, category_id): #100
        try:
           Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('This category does not exist!')
        return category_id
    def validate_review(self, review): # [1,2,100]
        review_db = Review.objects.filter(id_in=reviews)
        if len(reviews_db) != len(reviews):
            raise ValidationError('Review does not exist')
        return reviews
class MovieCreateSerializer(ProductValidateSerializer):
    pass
class MovieUpdateSerializer(ProductValidateSerializer):
    pass

