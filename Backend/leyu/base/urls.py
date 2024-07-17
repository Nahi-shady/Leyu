from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'children', ChildViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'teachers', TeacherViewSet)

router.register(r'category', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'pdfs', PDFViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'child-progress', ChildProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
