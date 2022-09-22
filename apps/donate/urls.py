from django.urls import path, include

from apps.donate.views.donater import DonateCreateView
from apps.donate.views.admin import AdminDonateListView, AdminDonateRetrieveView

urlpatterns = [
    path('donate/create/', DonateCreateView.as_view()),
    path('admin/donate/', include([
        path('list/', AdminDonateListView.as_view()),
        path('<int:pk>/', AdminDonateRetrieveView.as_view()),
    ]))
]
