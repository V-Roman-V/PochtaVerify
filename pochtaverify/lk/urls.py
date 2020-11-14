from django.urls import path

from .views import HomePageView, CreatePackageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('package/', CreatePackageView.as_view(), name='add_package')
]