from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required

from .models import Course

# Create your views here.
from django.contrib.auth import authenticate, login

# By default, you need to include auth url as 
# url(r'^accounts/', include('django.contrib.auth.urls'))
# And, create registration/login.html under one of registered app's templates dir
@permission_required('courses.add_course')
def detail(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	return render(request, 'courses/detail.html', {'course': course})