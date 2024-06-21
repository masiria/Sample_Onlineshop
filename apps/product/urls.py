from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('<slug:product_slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:category_slug>', views.CategoryPageView.as_view(), name='category_page'),
    path('<slug:tag_slug>', views.TagPageView.as_view(), name='tag_page'),
]