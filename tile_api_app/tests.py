from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task, Tile

class TaskModelTests(TestCase):
    def test_create_task(self):
        tile = Tile.objects.create(launch_date='2022-03-15', status='live')
        task = Task.objects.create(title='Test Task', order=1, description='Test Description', type='survey', tile=tile)
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.order, 1)
        self.assertEqual(task.description, 'Test Description')
        self.assertEqual(task.type, 'survey')
        self.assertEqual(task.tile, tile)

class TileModelTests(TestCase):
    def test_create_tile(self):
        tile = Tile.objects.create(launch_date='2022-01-01', status='live')
        self.assertEqual(tile.launch_date, '2022-01-01')
        self.assertEqual(tile.status, 'live')


class TaskAPITests(APITestCase):
    def setUp(self):
        self.tile = Tile.objects.create(launch_date='2022-01-01', status='live')
        self.task1 = Task.objects.create(title='Task 1', order=1, description='Description 1', type='survey', tile=self.tile)
        self.task2 = Task.objects.create(title='Task 2', order=2, description='Description 2', type='discussion', tile=self.tile)

    def test_get_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_task_detail(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'Task 3', 'order': 3, 'description': 'Description 3', 'type': 'diary', 'tile': self.tile.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {'title': 'Updated Task'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)

class TileAPITests(APITestCase):
    def setUp(self):
        self.tile1 = Tile.objects.create(launch_date='2022-01-01', status='live')
        self.tile2 = Tile.objects.create(launch_date='2022-02-01', status='pending')
        self.task1 = Task.objects.create(title='Task 1', order=1, description='Description 1', type='survey', tile=self.tile1)
        self.task2 = Task.objects.create(title='Task 2', order=2, description='Description 2', type='discussion', tile=self.tile1)

    def test_get_tile_list(self):
        url = reverse('tile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_tile_detail(self):
        url = reverse('tile-detail', args=[self.tile1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['launch_date'], '2022-01-01')

    def test_create_tile(self):
        url = reverse('tile-list')
        data = {'launch_date': '2022-03-01', 'status': 'live'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tile.objects.count(), 3)

    def test_update_tile(self):
        url = reverse('tile-detail', args=[self.tile1.id])
        data = {'status': 'archived'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tile1.refresh_from_db()
        self.assertEqual(self.tile1.status, 'archived')

    def test_tile_delete(self):
        url = reverse('tile-detail', args=[self.tile1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tile.objects.count(), 1)