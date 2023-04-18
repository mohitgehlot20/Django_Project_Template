from rest_framework import serializers
from newapp.models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()


def get_id(self,obj):
    return obj.name


class Meta:
    model=Employee
    fields=["id","name","email","address","phone"]


