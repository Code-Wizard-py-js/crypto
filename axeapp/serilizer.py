from rest_framework import serializers
from .models import Sivan,Forest,Arctic,Mystic,Genesis
class Sivanserial(serializers.ModelSerializer):
    class Meta:
        model=Sivan
        fields='__all__'
class Forestserial(serializers.ModelSerializer):
    class Meta:
        model=Forest
        fields='__all__'

class Arcticserial(serializers.ModelSerializer):
    class Meta:
        model=Arctic
        fields='__all__'

class Mysticserial(serializers.ModelSerializer):
    class Meta:
        model=Mystic
        fields='__all__'

class Genesisserial(serializers.ModelSerializer):
    class Meta:
        model=Genesis
        fields='__all__'

#items data serializer 
class Sivanserial(serializers.ModelSerializer):
    class Meta:
        model=Sivan
        fields='__all__'

class Sivanserial(serializers.ModelSerializer):
    class Meta:
        model=Sivan
        fields='__all__'

