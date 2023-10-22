from rest_framework import serializers
from drop.models import Drop

# Drop Setializers
# class DropSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()

    # class Meta:
    #     model = Drop
    #     fields = ['_ _all__']

class DropSerializer(serializers.ModelSerializer):
    # __all__ = serializers.CharField(source='some_field')J
    class Meta:
        model = Drop
        #fields = ('__all__', )
        fields = ['id', 'name', 'email', 'message', 'created_at']


    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user
