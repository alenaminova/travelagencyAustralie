from rest_framework import serializers
from viewer.models import travel_agency_Australie

class travel_agency_AustralieSerializer(serializers.ModelSerializer):

    class Meta:
        model = travel_agency_Australie
        fields = '__all__'