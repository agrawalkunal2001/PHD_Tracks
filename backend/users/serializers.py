from rest_framework import serializers
from .models import *

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name'] 


class ExaminerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examiner
        fields = '__all__'

class DscCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DSCCommittee
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    supervisor=SupervisorSerializer()
    indian_examiner=ExaminerSerializer()
    foreign_examiner=ExaminerSerializer()
    dsc_committee = DscCommitteeSerializer(many=True)
    class Meta:
        model = User
        exclude = ['password']

class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = UserSerializer()  # Include the user serializer here
    
# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = '__all__'

class Form1ASerializer(serializers.ModelSerializer):
    # education = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = Form1A
        fields = '__all__'


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'

class Form1BSerializer(serializers.ModelSerializer):
    # course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Form1B
        fields = '__all__'

class Form2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form2
        fields = '__all__'

class Form3ASerializer(serializers.ModelSerializer):
    class Meta:
        model = Form3A
        fields = '__all__'

class Form3BSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form3B
        fields = '__all__'

# class CommitteeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Committee
#         fields = '__all__'

class Form3CSerializer(serializers.ModelSerializer):
    # committee = CommitteeSerializer(many=True, read_only=True)

    class Meta:
        model = Form3C
        fields = '__all__'
  

class Form4ASerializer(serializers.ModelSerializer):
    # committee = CommitteeSerializer(many=True, read_only=True)

    class Meta:
        model = Form4A
        fields = '__all__'


class Form4BSerializer(serializers.ModelSerializer):
    # committee = CommitteeSerializer(many=True, read_only=True)

    class Meta:
        model = Form4B
        fields = '__all__'


class Form4CSerializer(serializers.ModelSerializer):
    # indian_examiner = ExaminerSerializer(read_only=True)
    # foreign_examiner = ExaminerSerializer(read_only=True)
    # committee = CommitteeSerializer(many=True, read_only=True)

    class Meta:
        model = Form4C
        fields = '__all__'

class Form4DSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form4D
        fields = '__all__'

class Form4ESerializer(serializers.ModelSerializer):
    class Meta:
        model = Form4E
        fields = '__all__'

class Form5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form5
        fields = '__all__'
        

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'   

class Form6Serializer(serializers.ModelSerializer):
    # comment = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Form6
        fields = '__all__'
 
