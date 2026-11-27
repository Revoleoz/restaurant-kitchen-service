from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


class DishViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cook = get_user_model().objects.create_user(username="olena")
        dish_type = DishType.objects.create(name="Супи")
        cls.dish = Dish.objects.create(
            name="Борщ", price="165.00", dish_type=dish_type
        )
        Dish.objects.create(name="Юшка", price="145.00", dish_type=dish_type)

    def test_dish_list_requires_login(self):
        url = reverse("kitchen:dish-list")
        login_url = reverse("login")

        self.assertRedirects(self.client.get(url), f"{login_url}?next={url}")

    def test_dish_search_filters_by_name(self):
        self.client.force_login(self.cook)

        response = self.client.get(
            reverse("kitchen:dish-list"), {"name": "Борщ"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
        self.assertEqual(list(response.context["dish_list"]), [self.dish])

    def test_cook_can_assign_and_unassign_self(self):
        self.client.force_login(self.cook)
        url = reverse("kitchen:dish-toggle-assignment", args=[self.dish.pk])
        detail_url = reverse("kitchen:dish-detail", args=[self.dish.pk])

        response = self.client.post(url, {"action": "assign"})
        self.assertRedirects(response, detail_url)
        self.assertTrue(self.dish.cooks.filter(pk=self.cook.pk).exists())

        response = self.client.post(url, {"action": "unassign"})
        self.assertRedirects(response, detail_url)
        self.assertFalse(self.dish.cooks.filter(pk=self.cook.pk).exists())
