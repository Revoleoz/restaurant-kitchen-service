from django.test import TestCase

from kitchen.forms import CookCreationForm


class CookCreationFormTests(TestCase):
    def setUp(self):
        self.data = {
            "username": "olena",
            "first_name": "Олена",
            "last_name": "Коваль",
            "years_of_experience": 7,
            "password1": "Test-kitchen-pass-8426",
            "password2": "Test-kitchen-pass-8426",
        }

    def test_valid_form_saves_cook(self):
        form = CookCreationForm(data=self.data)

        self.assertTrue(form.is_valid(), form.errors)
        cook = form.save()
        self.assertEqual(cook.first_name, "Олена")
        self.assertEqual(cook.years_of_experience, 7)
        self.assertTrue(cook.check_password(self.data["password1"]))

    def test_negative_experience_is_rejected(self):
        self.data["years_of_experience"] = -1
        form = CookCreationForm(data=self.data)

        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)
