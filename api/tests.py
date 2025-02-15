from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Project

User = get_user_model()

class ProjectAPITestCase(APITestCase):

    def setUp(self):
        # Create an Admin User
        self.admin_user = User.objects.create_user(username='admin', password='admin123', role='Admin')

        # Create a Member User
        self.member_user = User.objects.create_user(username='member', password='member123', role='Member')

        # Authenticate as Admin (JWT Authentication)
        self.client.force_authenticate(user=self.admin_user)

    def test_admin_can_create_project(self):
        """
        ✅ Admin should be able to create a project.
        """
        data = {'title': 'Test Project', 'description': 'Test Desc'}
        response = self.client.post('/projects/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.first().title, 'Test Project')

    def test_member_cannot_create_project(self):
        """
        ❌ Member should NOT be able to create a project.
        """
        self.client.force_authenticate(user=self.member_user)

        data = {'title': 'Test Project', 'description': 'Test Desc'}
        response = self.client.post('/projects/', data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_project(self):
        """
        ✅ Admin should be able to delete a project.
        """
        project = Project.objects.create(title="Test Project", description="Test Desc", creator=self.admin_user)

        response = self.client.delete(f'/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)

    def test_member_cannot_delete_project(self):
        """
        ❌ Member should NOT be able to delete a project.
        """
        project = Project.objects.create(title="Test Project", description="Test Desc", creator=self.admin_user)

        self.client.force_authenticate(user=self.member_user)
        response = self.client.delete(f'/projects/{project.id}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.count(), 1)
