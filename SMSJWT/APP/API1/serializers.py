# # from APP.models import UserModel
# from django.contrib.auth.models import User
# from rest_framework import serializers
#
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=50, min_length=6, write_only=True)
#     email = serializers.EmailField(max_length=100)
#     fname = serializers.CharField(max_length=100)
#     fname = serializers.CharField(max_length=100)
#     udep = serializers.CharField(max_length=50)
#     phoneno = serializers.IntegerField()
#     gender = serializers.CharField(max_length=100)
#
#     class Meta:
#         model = User
#         fields = ['id''email', 'password', 'fname', 'lname', 'phoneno', 'gender']
#         extra_kwargs = {'upassword': {'write_only': True}}
#
#     def validate(self, attrs):
#         uemail=attrs.get('uemail','')
#         if User.objects.filter(uemail=uemail).exists():
#             raise serializers.ValidationError(
#                 {'uemail','Email Already Exists'}
#             )
#         return super().validate(attrs)
#
#
# # class RegSerializer(ModelSerializer):
# #     class Meta:
# #         model=User
# #         fields=('id','username','email','password')
# #         extra_kwargs={'password':{'write_only':True}}
#
#     def create(self, validated_data):
#         user=User.objects.create_user(**validated_data)
#         return user
#
#
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from APP.API2.models import AdminDetails
from APP.API1.models import User


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminDetails
        fields = ('first_name', 'last_name', 'phone_number', 'age', 'gender')


class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        AdminDetails.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone_number=profile_data['phone_number'],
            age=profile_data['age'],
            gender=profile_data['gender']
        )
        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }
