from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import CleaningCompany
from .serializers import CleaningCompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def cleaning_companies_list(request):

    if request.method == 'GET':
        company = CleaningCompany.objects.all()
        serializer = CleaningCompanySerializer(company, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CleaningCompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, pk):
    try:
        company = CleaningCompany.objects.get(pk=pk)
    except CleaningCompany.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CleaningCompanySerializer(company)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CleaningCompanySerializer(company, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        company.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
