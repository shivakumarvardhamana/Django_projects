from rest_framework import serializers

from base.models import test

class testingser(serializers.ModelSerializer):

    class Meta:
        model=test
        fields ='__all__'
        
