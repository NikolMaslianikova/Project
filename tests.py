from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Medicine.models import *


class CreateMedicineViewTest(APITestCase):

    def test_create_medicine_success(self):
        url = reverse('create_medicine')
        data = {
            'name': 'Aspirin',
            'description': 'Used to reduce pain and fever.',
            'price': 9.99,
            'count': 100
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Medicine.objects.count(), 1)
        medicine = Medicine.objects.get()
        self.assertEqual(medicine.name, 'Aspirin')
        self.assertEqual(medicine.description, 'Used to reduce pain and fever.')
        self.assertEqual(medicine.price, 9.99)
        self.assertEqual(medicine.count, 100)

    def test_create_medicine_invalid_data(self):
        url = reverse('create_medicine')
        invalid_data = {
            'description': 'Pain reliever',
            'price': 5.99,
            'count': 50
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteMedicineViewTest(APITestCase):
    def setUp(self):
        self.medicine = Medicine.objects.create(
            name='Paracetamol',
            description='Pain reliever and a fever reducer',
            price=15.99,
            count=50
        )

    def test_delete_medicine_success(self):
        url = reverse('delete_medicine', args=[self.medicine.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Medicine.objects.filter(pk=self.medicine.pk).count(), 0)

    def test_delete_medicine_not_found(self):
        url = reverse('delete_medicine', args=[99999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EditMedicineViewTest(APITestCase):
    def setUp(self):
        self.medicine = Medicine.objects.create(
            name='Ibuprofen',
            description='Used to reduce fever and treat pain',
            price=20.00,
            count=30
        )
        self.url = reverse('edit_medicine', args=[self.medicine.pk])

    def test_update_medicine_success(self):
        updated_data = {
            'name': 'Ibuprofen',
            'description': 'Pain reliever and fever reducer',
            'price': 25.00,
            'count': 25
        }
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.medicine.refresh_from_db()
        self.assertEqual(self.medicine.description, 'Pain reliever and fever reducer')
        self.assertEqual(self.medicine.price, 25.00)
        self.assertEqual(self.medicine.count, 25)

    def test_update_medicine_not_found(self):
        url = reverse('edit_medicine', args=[99999])
        response = self.client.put(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_medicine_invalid_data(self):
        invalid_data = {
            'name': '',
        }
        response = self.client.put(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreatePurchaseRequestViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.medicine = Medicine.objects.create(
            name='Cough Syrup',
            description='Used to treat cough',
            price=20.00,
            count=50
        )
        self.url = reverse('create_PurchaseRequest')

    def test_create_purchase_request_success(self):
        self.client.login(username='testuser', password='12345')
        data = {
            'user': self.user.pk,
            'medicine_id': self.medicine.pk
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseRequest.objects.count(), 1)
        purchase_request = PurchaseRequest.objects.get()
        self.assertEqual(purchase_request.user, self.user)
        self.assertEqual(purchase_request.medicine_id, self.medicine)

    def test_create_purchase_request_invalid_data(self):
        self.client.login(username='testuser', password='12345')
        invalid_data = {
            'user': self.user.pk
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeletePurchaseRequestViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        medicine = Medicine.objects.create(name='Ibuprofen', description='Pain reliever', price=5.00, count=100)
        self.purchase_request = PurchaseRequest.objects.create(user=user, medicine_id=medicine)
        self.url = reverse('delete_PurchaseRequest', args=[self.purchase_request.pk])

    def test_delete_purchase_request_success(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseRequest.objects.filter(pk=self.purchase_request.pk).count(), 0)


class EditPurchaseRequestViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        medicine = Medicine.objects.create(name='Paracetamol', description='Fever reducer', price=10.00, count=50)
        self.purchase_request = PurchaseRequest.objects.create(user=user, medicine_id=medicine)
        self.url = reverse('edit_purchaseRequest', args=[self.purchase_request.pk])

    def test_update_purchase_request_success(self):
        updated_data = {
            'user': self.purchase_request.user.pk,
            'medicine_id': self.purchase_request.medicine_id.pk
        }
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_request.refresh_from_db()

    def test_update_purchase_request_not_found(self):
        non_existent_url = reverse('edit_purchaseRequest', args=[99999])
        response = self.client.put(non_existent_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_purchase_request_invalid_data(self):
        invalid_data = {
            'user': None,
        }
        response = self.client.put(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetPurchaseRequestViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        medicine1 = Medicine.objects.create(name='Medicine1', description='Description1', price=10.00, count=40)
        medicine2 = Medicine.objects.create(name='Medicine2', description='Description2', price=15.00, count=50)
        PurchaseRequest.objects.create(user=user, medicine_id=medicine1)
        PurchaseRequest.objects.create(user=user, medicine_id=medicine2)

    def test_get_all_purchase_requests(self):
        url = reverse('get_purchaseRequest')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_no_purchase_requests(self):
        PurchaseRequest.objects.all().delete()
        url = reverse('get_purchaseRequest')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class CreateDemandViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.url = reverse('create_Demand')

    def test_create_demand_success(self):
        data = {
            'user': self.user.pk,
            'medicines': []
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Demand.objects.count(), 1)

    def test_create_demand_invalid_data(self):
        invalid_data = {
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteDemandViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser2', password='12345')
        self.demand = Demand.objects.create(user=user)
        self.url = reverse('delete_Demand', args=[self.demand.pk])

    def test_delete_demand_success(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Demand.objects.filter(pk=self.demand.pk).count(), 0)
