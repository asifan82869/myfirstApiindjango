from rest_framework import serializers
from hrm.models import *

class Userserializer(serializers.ModelSerializer):

	#following two line use when we modify sum thing.
    employee_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    ranking = serializers.FloatField(required=False)
    class Meta:
        model = User
        fields = "__all__"