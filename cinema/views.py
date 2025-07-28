from rest_framework import viewsets
from cinema import models
from cinema import serializers


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = models.CinemaHall.objects.all()
    serializer_class = serializers.CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieListSerializer
        elif self.action == "retrieve":
            return serializers.MovieRetrieveSerializer
        else:
            return serializers.MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = models.MovieSession.objects.all()
    serializer_class = serializers.MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieSessionListSerializer
        elif self.action == "retrieve":
            return serializers.MovieSessionRetrieveSerializer
        else:
            return serializers.MovieSessionSerializer

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return self.queryset.select_related("movie", "cinema_hall")
        return queryset
