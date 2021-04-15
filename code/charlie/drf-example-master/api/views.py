from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StudentSerializer, UserSerializer

from users.models import User
from students.models import Student