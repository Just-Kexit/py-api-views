from rest_framework import serializers

from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall
)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        field = "__all__"


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        field = "__all__"


class ActorSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        field = "__all__"


class CinemaHallSerializer(serializers.Serializer):
    class Meta:
        model = CinemaHall
        field = "__all__"
