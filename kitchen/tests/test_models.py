from django.test import TestCase

from kitchen.models import DishType


class DishTypeModelTests(TestCase):
    def test_string_representation_is_name(self):
        dish_type = DishType(name="Супи")

        self.assertEqual(str(dish_type), "Супи")
