from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Course

# Test use test database which is initialized empty
# Create your tests here.

class CourseViewTests(TestCase):
	def test_detail_view(self):
		Course.objects.create(title='American History')
		
		response = self.client.get(reverse('courses:detail', args=(1,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'American History')
