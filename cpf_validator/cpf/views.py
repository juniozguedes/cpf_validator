from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CpfSerializer
from django.http import JsonResponse
from .cpf import isCpfValid
from .models import Cpf
from . import validators
import json

class DeniedCpfViewSet(APIView):
    def get(self, request, format=None):
        queryset = Cpf.objects.filter(status='DENY')
        serializer = CpfSerializer(queryset, many=True)
        return Response(serializer.data)

class CpfDetail(APIView):
    def get(self, request, format=None):
        try:
            req = json.loads(request.body.decode("utf-8"))
            queryset = Cpf.objects.filter(number=request.data['number'])
            serializer = CpfSerializer(queryset, many=True)
            validation = validators.validate_api(req)
            if not validation["success"]:
               return Response({validation["details"]:res["errors"] })
            if not isCpfValid(request.data['number']):
              return Response("Invalid CPF number")
            else:
                if serializer.data == []:
                    return Response({"Message": "Cpf não encontrado"})
                return Response(serializer.data)
        except Exception as e:
            return Response({"Exception": e})
    
    def post(self, request, format=None):
        req = json.loads(request.body.decode("utf-8"))
        validation = validators.validate_creation(req)
        if not validation["success"]:
            return Response({validation["details"]:validation["errors"] }, validation["status"])
        if not isCpfValid(request.data['number']):
            return Response("Invalid CPF number", status=404)

        serializer = CpfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, validation["status"])
        return Response(serializer.errors, validation["status"])