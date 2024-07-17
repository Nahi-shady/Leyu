from rest_framework import viewsets, generics
from .models import Parent, Child
from .serializers import *

# CRUD API VIEW FOR PARENTS
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = 'user__username'

# CRUD API VIEW FOR PARENTS
class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    lookup_field = 'user__username'

# CRUD API VIEW FOR TEACHERS
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'user_username'


# API views for course, vidoes, pdfs, quize and enrollment and childporgress
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ChildProgressViewSet(viewsets.ModelViewSet):
    queryset = ChildProgress.objects.all()
    serializer_class = ChildProgressSerializer


# Authentication
class TeacherRegistrationView(generics.CreateAPIView):
    serializer_class = TeacherRegistrationSerializer

class ChildRegistrationView(generics.CreateAPIView):
    serializer_class = ChildRegistrationSerializer

class ParentRegistrationView(generics.CreateAPIView):
    serializer_class = ParentRegistrationSerializer