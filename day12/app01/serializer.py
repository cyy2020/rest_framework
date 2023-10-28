from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    student_id = serializers.CharField()
    student_name = serializers.CharField()
    student_gender = serializers.BooleanField()
    student_class = serializers.PrimaryKeyRelatedField(many=False, queryset=Teacher.objects.all())

    def to_representation(self, instance):
        Class = instance.student_class

        ret = super(StudentSerializer, self).to_representation(instance)
        ret["student_class"] = {
            "id": Class.id,
            "name": Class.name
        }


        return ret
