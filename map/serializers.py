from rest_framework import serializers
from .models import TvmRange4326


class TvmRangeSerializers(serializers.ModelSerializer):

    class Meta:

        model = TvmRange4326
        fields = '__all__'
        #exclude = ('perimeter', 'area', 'range_area', 'geom', )
