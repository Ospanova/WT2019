from rest_framework import serializers
from api.models import Contact, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email')



class ContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Contact
        fields = '__all__' # if want to post all fieds
        

# class ContactSerializer2(serializers.ModelSerializer)
