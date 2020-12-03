from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from APP.API1.serializers import UserRegistrationSerializer
from APP.API2.models import AdminDetails


class AdminProfileView(RetrieveUpdateDestroyAPIView,ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    # queryset = UserProfile.objects.all()
    # serializer_class = UserRegistrationSerializer
    # lookup_field = 'id'

    def get(self, request,*args,**kwargs):
        try:
            admindetail = AdminDetails.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'message': 'User profile fetching successful',
                'data': [{
                    'first_name': admindetail.first_name,
                    'last_name': admindetail.last_name,
                    'phone_number': admindetail.phone_number,
                    'age': admindetail.age,
                    'gender': admindetail.gender,
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)
