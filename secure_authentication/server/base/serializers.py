from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Note

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
