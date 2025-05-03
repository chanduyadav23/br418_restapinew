from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class Allmovies(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

@api_view(['GET'])
def apioverview(req):
    api_urls={
        'allmovies':"/Allmovies",
        'addmovie':'/addmovie',
        'updatemovie':'/updatemovie/update/pk',
        'deletemovie':'Deletemovie/delete/pk',
        'search by category':'/serchbycategory/?category=categoryname',
    }
    return Response(api_urls)

class Addmovie(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class Updatamovie(generics.RetrieveUpdateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class Deletemovie(generics.DestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


from django.db.models import Q
from rest_framework import status
@api_view(['GET'])
def serchbycategory(req):
    query_params=req.query_params
    filters=Q()

    if "category" in query_params:
        filters &=Q(category=query_params['category'])
    
    movie=Movie.objects.filter(filters)
    if not movie.exists():
        return Response(
            {'message':'No movie found'},status=status.HTTP_404_NOT_FOUND
        )
    serializer=MovieSerializer(movie,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)