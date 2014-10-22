from rest_framework.test import APITestCase

from .models import Food

class FoodTestCase(APITestCase):

    def setUp(self):
        food1 = Food.objects.create(
            name = 'Leftover Lasagna',
            quantity = 2,
            unit = 'pieces'
        )

    def test_get_foods(self):
        response = self.client.get('/food/', format='json')
        self.assertEqual(response.data[0]['name'], u'Leftover Lasagna')
