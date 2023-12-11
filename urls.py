from django.urls import path
from .views import *

urlpatterns = [
    path('create_medicine/', CreateMedicineView.as_view(), name='create_medicine'),
    path('delete_medicine/<int:pk>/', DeleteMedicineView.as_view(), name='delete_medicine'),
    path('edit_medicine/<int:pk>/', EditMedicineView.as_view(), name='edit_medicine'),
    path('get_medicine/', GetMedicineView.as_view(), name='get_medicine'),

    path('create_purchase/', CreatePurchaseRequestView.as_view(), name='create_PurchaseRequest'),
    path('delete_purchase/<int:pk>/', DeletePurchaseRequestView.as_view(), name='delete_PurchaseRequest'),
    path('edit_purchase/<int:pk>/', EditPurchaseRequestView.as_view(), name='edit_purchaseRequest'),
    path('get_purchase/', GetPurchaseRequestView.as_view(), name='get_purchaseRequest'),

    path('create_demand/', CreateDemandView.as_view(), name='create_Demand'),
    path('delete_demand/<int:pk>/', DeleteDemandView.as_view(), name='delete_Demand'),
    path('edit_demand/<int:pk>/', EditDemandView.as_view(), name='edit_Demand'),
    path('get_demand/', GetDemandView.as_view(), name='get_Demand'),

    path('create_user/', CreateUserView.as_view(), name='create_user'),
]