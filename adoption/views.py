from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from adoption.serializers import AdoptionSerializer
from .email_service import send_confirmation_email
from .models import Adoption


class AdoptionList(APIView):
    def get(self, request, format=None):
        adoptions = Adoption.objects.all()
        serializer = AdoptionSerializer(adoptions, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AdoptionSerializer(data=request.data)
        if serializer.is_valid():
            adoption = serializer.save()
            send_confirmation_email(adoption)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "message": "There were validation errors",
                "errors": serializer.errors
            }
            , status=HTTP_400_BAD_REQUEST)
