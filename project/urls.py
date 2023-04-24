from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.ItemListCreateAPIView.as_view()),
    path('manufacturer/', views.ManufacturerListCreateAPIView.as_view()),
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('item/<int:item_id>', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('manufacturer/<int:manufacturer_id>', views.ManufacturerRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category_id>', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
]