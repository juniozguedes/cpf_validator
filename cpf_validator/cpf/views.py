from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CpfSerializer
from django.http import JsonResponse
from .cpf import is_cpf_valid
from .models import Cpf
import json
import re


class List(APIView):
    def get(self, request, format=None):
        queryset = Cpf.objects.all()
        serializer = CpfSerializer(queryset, many=True)
        return Response(serializer.data)


class Denied(APIView):
    def get(self, request, format=None):
        queryset = Cpf.objects.filter(status='DENY')
        serializer = CpfSerializer(queryset, many=True)
        return Response(serializer.data)


class Detail(APIView):
    def get(self, request, format=None):
        try:
            request.data['number'] = re.sub("[^0-9]", '',
                                            request.data['number'])
            queryset = Cpf.objects.filter(number=request.data['number'])
            serializer = CpfSerializer(queryset, many=True)
            if not is_cpf_valid(request.data['number']):
                return Response("Invalid CPF number")
            else:
                if serializer.data == []:
                    return Response({"Message": "Cpf não encontrado"})
                return Response(serializer.data)
        except Exception as e:
            return Response("Exception", e)

    def delete(self, request, format=None):
        try:
            request.data['number'] = re.sub("[^0-9]", '',
                                            request.data['number'])
            queryset = Cpf.objects.filter(number=request.data['number'])
            serializer = CpfSerializer(queryset, many=True)
            if not is_cpf_valid(request.data['number']):
                return Response("Invalid CPF number")
            else:
                if serializer.data == []:
                    return Response({"Message": "Cpf não encontrado"})
                queryset.delete()
                return Response(serializer.data)
        except Exception as e:
            return Response("Exception", e)


class Create(APIView):
    def post(self, request, format=None):
        request.data['number'] = re.sub("[^0-9]", '', request.data['number'])
        if not is_cpf_valid(request.data['number']):
            return Response("Invalid CPF number", status=404)
        request.data['number'] = re.sub("[^0-9]", '', request.data['number'])

        serializer = CpfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=404)
