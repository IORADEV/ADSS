from rest_framework import serializers
from geojson_serializer.serializers import geojson_serializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import TvmRange4326, TvmDivision, TvmSection4326


class TvmRangeSerializers(serializers.ModelSerializer):

    class Meta:

        model = TvmRange4326
        fields = ('name', )
        read_only_fields = ['name']


class TmvDivisionSerializers(serializers.ModelSerializer):

    class Meta:

        model = TvmDivision
        fields = ('name', )
        read_only_fields = ['name']


class TmvSectionSerializers(serializers.ModelSerializer):

    class Meta:

        model = TvmSection4326
        fields = ('name', )
        read_only_fields = ['name']
