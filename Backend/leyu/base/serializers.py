from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# SERIALIZER USER TYPES
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Parent
        fields = ['id', 'user', 'phone', 'address', 'date_joined', 'last_login']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        parent = Parent.objects.create(user=user, **validated_data)
        return parent

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()

        return instance

class ChildSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    parent = serializers.SlugRelatedField(queryset=Parent.objects.all(), slug_field='user__username')

    class Meta:
        model = Child
        fields = ['user', 'parent', 'disability', 'phone', 'age', 'date_joined', 'last_login']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        parent_username = validated_data.pop('parent')  # Retrieve parent username from validated data
        user = User.objects.create(**user_data)
        
        parent = Parent.objects.get(user__username=parent_username)  # Fetch parent by username
        child = Child.objects.create(user=user, parent=parent, **validated_data)
        return child

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        parent_username = validated_data.pop('parent', None)

        # Update Child fields
        instance.disability = validated_data.get('disability', instance.disability)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.age = validated_data.get('age', instance.age)
        instance.save()

        # Update User fields
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()

        return instance

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'phone', 'address', 'date_joined', 'last_login']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')

        # Update Teacher fields
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        # Update User fields
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()

        return instance



# Serializers for course, vidoes, pdfs, quize and enrollment and childporgress

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'description']

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Use the nested serializer for read operations
    category_name = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )  
    class Meta:
        model = Course
        fields = ['id', 'title', 'image', 'description', 'category', 'category_name', 'duration', 'difficulty_level']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'course', 'title', 'video_url']

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ['id', 'course', 'title', 'pdf_file']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'course', 'title']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'child', 'course', 'enrolled_date', 'completed']

class ChildProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProgress
        fields = ['id', 'parent', 'enrollment']



# Authentication
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class TeacherRegistrationSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'phone', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegistrationSerializer.create(UserRegistrationSerializer(), validated_data=user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

class ChildRegistrationSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()

    class Meta:
        model = Child
        fields = ['user', 'parent', 'disability', 'phone', 'age']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegistrationSerializer.create(UserRegistrationSerializer(), validated_data=user_data)
        child = Child.objects.create(user=user, **validated_data)
        return child

class ParentRegistrationSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()

    class Meta:
        model = Parent
        fields = ['user', 'phone', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegistrationSerializer.create(UserRegistrationSerializer(), validated_data=user_data)
        parent = Parent.objects.create(user=user, **validated_data)
        return parent