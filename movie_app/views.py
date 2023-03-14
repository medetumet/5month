from django.shortcuts import render
from movie_app.models import *
from movie_app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie_app.serializers import *
from rest_framework import status
from .models import Movie, Category, Tag
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

# class TagModelView(ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     pagination_class = PageNumberPagination
#
#
# class CategoryListAPIView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializers_class = CategorySerializer
#     pagination_class = PageNumberPagination
#
# class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class MovieListCreateAPIView(ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers



# Create your views here.
@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':

        directors = Director.objects.all()
        serializer = DirectorSerializers(directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        director = Director.objects.create(**request.data)
        director.save()
        return Response(data=DirectorSerializers(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializers(director, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        director.name = request.data.get("name")
        director.save()
        return Response(data={'message': 'data received!',
                              'movie': DirectorSerializers(director).data})


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        movie = Movie.objects.create(**request.data)
        print(movie)
        movie.save()
        return Response(data=MovieSerializers(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializers(movie, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movie.title = request.data.get("title")
        movie.description = request.data.get("description")
        movie.duration = request.data.get("duration")
        movie.director_id = request.data.get("director_id")
        movie.save()
        return Response(data={'message': 'data received!',
                              'movie': MovieSerializers(movie).data})

@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializers(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        review = Review.objects.create(**request.data)
        review.save()
        return Response(data=ReviewSerializers(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializers(review, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        review.text = request.data.get("text")
        review.movie_id = request.data.get("movie_id")
        review.save()
        return Response(data={'message': 'data received!',
                              'movie': ReviewSerializers(review).data})






