from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Medicine
from .serializer import *


class CreateMedicineView(APIView):
    @swagger_auto_schema(request_body=MedicineSerializer)
    def post(self, request, *args, **kwargs):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteMedicineView(APIView):
    def delete(self, request, pk):
        try:
            medicine = Medicine.objects.get(pk=pk)
            medicine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EditMedicineView(APIView):
    @swagger_auto_schema(
        request_body=MedicineSerializer(partial=True),
        responses={
            status.HTTP_200_OK: MedicineSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad Request',
            status.HTTP_404_NOT_FOUND: 'Not Found',
            status.HTTP_403_FORBIDDEN: 'Forbidden'
        }
    )
    def put(self, request, pk):
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetMedicineView(APIView):
    def get(self, request):
        try:
            medicine = Medicine.objects.all()
            serializer = MedicineSerializer(medicine, many=True)
            return Response(serializer.data)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreatePurchaseRequestView(APIView):
    @swagger_auto_schema(request_body=PurchaseRequestSerializer)
    def post(self, request, *args, **kwargs):
        serializer = PurchaseRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePurchaseRequestView(APIView):
    def delete(self, request, pk):
        try:
            medicine = PurchaseRequest.objects.get(pk=pk)
            medicine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EditPurchaseRequestView(APIView):
    @swagger_auto_schema(
        request_body=PurchaseRequestSerializer(partial=True),
        responses={
            status.HTTP_200_OK: PurchaseRequestSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad Request',
            status.HTTP_404_NOT_FOUND: 'Not Found',
            status.HTTP_403_FORBIDDEN: 'Forbidden'
        }
    )
    def put(self, request, pk):
        try:
            medicine = PurchaseRequest.objects.get(pk=pk)
        except PurchaseRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PurchaseRequestSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPurchaseRequestView(APIView):
    def get(self, request):
        try:
            medicine = PurchaseRequest.objects.all()
            serializer = PurchaseRequestSerializer(medicine, many=True)
            return Response(serializer.data)
        except PurchaseRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateDemandView(APIView):
    @swagger_auto_schema(request_body=DemandSerializer)
    def post(self, request, *args, **kwargs):
        serializer = DemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteDemandView(APIView):
    def delete(self, request, pk):
        try:
            medicine = Demand.objects.get(pk=pk)
            medicine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EditDemandView(APIView):
    @swagger_auto_schema(
        request_body=DemandSerializer(partial=True),
        responses={
            status.HTTP_200_OK: DemandSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad Request',
            status.HTTP_404_NOT_FOUND: 'Not Found',
            status.HTTP_403_FORBIDDEN: 'Forbidden'
        }
    )
    def put(self, request, pk):
        try:
            medicine = Demand.objects.get(pk=pk)
        except Demand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DemandSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDemandView(APIView):
    def get(self, request):
        try:
            medicine = Demand.objects.all()
            serializer = DemandSerializer(medicine, many=True)
            return Response(serializer.data)
        except Demand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateUserView(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)