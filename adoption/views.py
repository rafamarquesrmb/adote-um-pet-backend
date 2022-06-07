from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from adoption.serializers import AdoptionSerializer
from .email_service import send_confirmation_email

class AdoptionList(APIView):
    def post(self, request, format=None):
        serializer = AdoptionSerializer(data=request.data)
        if serializer.is_valid():
            adoption = serializer.save()
            send_confirmation_email(adoption)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Something was wrong"
            }
            , status=HTTP_400_BAD_REQUEST)
