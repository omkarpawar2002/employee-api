from django.urls import path
from .views import EmployeeView, EmployeeDetailView

urlpatterns = [
    path("emp/", EmployeeView.as_view(), name="emp_list"),
    path("emp/<int:pk>/", EmployeeDetailView.as_view(), name="emp_detail"),
]
