from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AuthViewsTests(TestCase):
	def test_register_and_login_flow(self):
		User = get_user_model()
		# Register a new user
		resp = self.client.post(reverse('register'), data={'username': 'testuser', 'password1': 'StrongPass123', 'password2': 'StrongPass123'})
		# After register we expect a redirect to inicio
		self.assertEqual(resp.status_code, 302)

		# Now attempt to login with the same credentials
		login = self.client.post(reverse('login'), data={'username': 'testuser', 'password': 'StrongPass123'})
		# login should redirect to inicio
		self.assertEqual(login.status_code, 302)
