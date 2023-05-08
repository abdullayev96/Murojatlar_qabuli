from django.urls import path
from .views import home
# from .views import TestResultDetail
#
urlpatterns = [
        path('', home)
#     path('test/<int:id_number>/detail', TestResultDetail.as_view(), name="test-result-detail"),
]