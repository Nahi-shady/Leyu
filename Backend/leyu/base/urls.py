from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/teacher/', TeacherRegistrationView.as_view(), name='register_teacher'),
    path('register/child/', ChildRegistrationView.as_view(), name='register_child'),
    path('register/parent/', ParentRegistrationView.as_view(), name='register_parent'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
