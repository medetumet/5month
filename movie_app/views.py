from django.shortcuts import render
from movie_app.models import *
from movie_app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializers(director, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializers(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializers(review, many=True)
    return Response(data=serializer.data)



@api_view(['Get'])
def director_detail(request, id):
    director = Director.objects.get(id=id)
    data = DirectorSerializers(director).data
    return Response(data=data)

@api_view(['Get'])
def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    data = MovieSerializers(movie).data
    return Response(data=data)

@api_view(['Get'])
def review_detail(request, id):
    review = Review.objects.get(id=id)
    data = ReviewSerializers(review, many = False)
    return Response(data=data)

@api_view(['GET'])
def review_movie(request):
    movie = Movie.objects.all()
    serializers = MovieReviewSerializers(movie, many=True)
    return Response(data=serializers)




