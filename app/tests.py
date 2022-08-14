from turtle import title
from unittest import TestResult

from django.test import TestCase

from .models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="First Post")

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.title}"
        self.assertEqual(expected_object_name, "First Post")


# Create your tests here.
