from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CookAdminTests(TestCase):
    def test_cook_experience_is_displayed(self):
        user_model = get_user_model()
        admin = user_model.objects.create_superuser(username="admin")
        cook = user_model.objects.create_user(
            username="olena", years_of_experience=7
        )
        self.client.force_login(admin)

        response = self.client.get(reverse("admin:kitchen_cook_changelist"))
        self.assertContains(response, cook.username)
        self.assertIn("years_of_experience", response.context["cl"].list_display)

        response = self.client.get(
            reverse("admin:kitchen_cook_change", args=[cook.pk])
        )
        self.assertContains(response, 'name="years_of_experience"')
