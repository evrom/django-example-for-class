from django.test import TestCase, RequestFactory
from django.urls import reverse

from twittr.models import Message
from twittr.views import my_view


class MyViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.resource = reverse('my_view')

    def test_get(self):
        request = self.factory.get(self.resource)
        response = my_view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """
        On a successful post request:
        create new message in the database
        return redirect back to same view
        """
        data = {'message': 'hi'}
        request = self.factory.post(self.resource, data)
        message_count_before = Message.objects.count()
        response = my_view(request)
        message_count_after = Message.objects.count()
        self.assertEqual(message_count_before + 1, message_count_after)
        self.assertEqual(response['location'], self.resource)
