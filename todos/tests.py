from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from .models import Todo


class TodoModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):

        cls.todo = Todo.objects.create(
            title = 'First Todo',
            body = 'Some useful supporting text.',
        )


    def testModelContent(self):
        """
        Performs basic tests on the Todo model.
        """

        self.assertEqual(self.todo.title, 'First Todo')
        self.assertEqual(self.todo.body, 'Some useful supporting text.')
        self.assertEqual(str(self.todo), 'First Todo')


    def testApiListView(self):
        """
        Tests the todo list endpoint.
        """
        
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)


    def testApiDetailView(self):
        """
        Tests the todo detail (single object) endpoint.
        """

        response = self.client.get(reverse('todo_detail', kwargs={'pk': self.todo.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, 'First Todo')