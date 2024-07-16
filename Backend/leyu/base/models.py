from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Parent')
    phone = models.CharField(max_length=100, verbose_name="Parent's Phone")
    address = models.CharField(max_length=100, verbose_name='Address')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

class Child(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Child')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    disability = models.CharField(max_length=100, verbose_name='Disability')
    phone = models.CharField(max_length=100, verbose_name="Child's Phone")
    age = models.IntegerField(null=False, blank=False, verbose_name="Child's Age")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Teacher')
    phone = models.CharField(max_length=100, verbose_name="Phone")
    address = models.CharField(max_length=100, verbose_name='Address')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    categories = [
        ('Alphabet', 'Alphabet'),
        ('Numbers', 'Numbers'),
        ('Signs', 'Signs'),
        ('Other', 'Other')
        ]
    name = models.CharField(max_length=50, choices=categories, default='Other')
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    levels = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard')
        ]

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course/', blank=True, null=True)
    duration = models.IntegerField(help_text='Duration in hours or days, etc.')
    difficulty_level = models.CharField(max_length=1, choices=levels, default='E')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class PDF(models.Model):
    course = models.ForeignKey(Course, related_name='pdfs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

class Quiz(models.Model):
    course = models.ForeignKey(Course, related_name='quizzes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # Add fields like questions, options, answers, etc.

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    # Add fields to track progress, scores, etc.

    def __str__(self):
        return f"{self.child.user.username} - {self.course.title}"

class ChildProgress(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    # Add fields to track progress, scores, etc.

    def __str__(self):
        return f"{self.parent.user.username} - {self.enrollment.child.user.username} - {self.enrollment.course.title}"