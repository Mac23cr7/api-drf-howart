from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.apiSolicitud.models import School, Request
from apps.apiSolicitud.serializers import SchoolSerializer, RequestSerializer

# Create your views here.
""" class SchoolApiView(APIView):

    def get(self, request):
        schools = School.objects.all()
        schools_serializer = SchoolSerializer(schools, many = True)
        return Response(schools_serializer.data) """


""" METHODS FOR SCHOOL MODEL AND SERIALIZER """
@api_view(['GET', 'POST'])
def school_api_view(request):

    if request.method == 'GET':
        schools = School.objects.all()
        schools_serializer = SchoolSerializer(schools, many = True)
        return Response(schools_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        school_serializer = SchoolSerializer(data = request.data)
        if school_serializer.is_valid():
            school_serializer.save()
            return Response({'messages':'School added succesfully'}, status = status.HTTP_201_CREATED)
        return Response(school_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def school_api_detail(request, pk = None):

    school = School.objects.filter(houseId = pk).first()

    if school:

        if request.method == 'GET':
            school_serializer = SchoolSerializer(school)
            return Response(school_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            school_serializer = SchoolSerializer(school, data = request.data)
            if school_serializer.is_valid():
                school_serializer.save()
                return Response({'message':'School updated succesfuly'}, status = status.HTTP_200_OK)
            return Response(school_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            school.delete()
            return Response({'message':'School deleted succesfully'}, status = status.HTTP_200_OK)

    return Response({'message':'Id school not found'}, status = status.HTTP_400_BAD_REQUEST)


    """ METHODS FOR REQUEST MODEL AND SERIALIZER """

@api_view(['GET', 'POST'])
def request_api_view(request):

    if request.method == 'GET':
        requests = Request.objects.all()
        requests_serializer = RequestSerializer(requests, many = True)
        return Response(requests_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        request_serializer = RequestSerializer(data = request.data)
        if request_serializer.is_valid():
            request_serializer.save()
            return Response({'messages':'Request created succesfully'}, status = status.HTTP_201_CREATED)
        return Response(request_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def request_api_detail(request, pk = None):

    requested = Request.objects.filter(requestId = pk).first()

    if requested:

        if request.method == 'GET':
            request_serializer = RequestSerializer(requested)
            return Response(request_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            request_serializer = RequestSerializer(requested, data = request.data)
            if request_serializer.is_valid():
                request_serializer.save()
                return Response({'message':'Request updated succesfuly'}, status = status.HTTP_200_OK)
            return Response(request_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            requested.delete()
            return Response({'message':'Request deleted succesfully'}, status = status.HTTP_200_OK)

    return Response({'message':'Id request not found'}, status = status.HTTP_400_BAD_REQUEST)