from django.test import TestCase, Client
from .models import Recipe


class TestViews(TestCase):

    def test_get_tags_list(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
