 from django.db import models

 class UserModel(models.Model):
     class UserSerializer(serializers.Model):
     password=models.CharField(max_length=50,min_length=6,write_only=True)
     email=models.EmailField(max_length=100)
     fname=models.CharField(max_length=100)
     fname=models.CharField(max_length=100)
     udep=models.CharField(max_length=50)
     phoneno=models.IntegerField()
     gender=models.CharField(max_length=100)
