# coding:utf-8
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class ClientInfoTest(APITestCase):
    def test_client(self):
        url = reverse('client_info')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        pass
