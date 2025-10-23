from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardAccessTests(TestCase):
    def test_dashboard_requires_login_and_returns_200_for_authenticated(self):
        # Crear usuario
        u = User.objects.create_user(username='tester', password='secret123')
        # Login
        login = self.client.login(username='tester', password='secret123')
        self.assertTrue(login)
        # Acceder al dashboard
        resp = self.client.get(reverse('dashboard'))
        self.assertEqual(resp.status_code, 200)
        # Comprobar que el nombre de usuario aparece en el contexto/HTML
        self.assertContains(resp, 'tester')
