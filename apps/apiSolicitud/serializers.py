from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.apiSolicitud.models import School, Request

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    #idSchool = SchoolSerializer()
    #idSchool = serializers.StringRelatedField()

    class Meta:
        model = Request
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.requestId,
            'studentName': instance.studentName,
            'studentSurname': instance.studentSurname,
            'identification': instance.identification,
            'age': instance.age,
            'idSchool': {
                'houseId':instance.idSchool.houseId,
                'houseName': instance.idSchool.houseName
            } 

     } 