from django.urls import path, include

from apps.donate.views.donater import DonateCreateView
from apps.donate.views.admin import AdminDonateListView, AdminDonateRetrieveView, AdminDonateEditView, \
    AdminDonateForStudentAddView, AdminDonateForStudentEditView, AdminDonateForStudentDeleteView

urlpatterns = [
    path('donate/create/', DonateCreateView.as_view()),
    path('admin/donate/', include([
        path('list/', AdminDonateListView.as_view()),
        path('<int:pk>/', AdminDonateRetrieveView.as_view()),
        path('edit/<int:pk>/', AdminDonateEditView.as_view()),
        path('for/student/', include([
            path('add/', AdminDonateForStudentAddView.as_view()),
            path('edit/<int:pk>/', AdminDonateForStudentEditView.as_view()),
            path('delete/<int:pk>/', AdminDonateForStudentDeleteView.as_view()),
        ]))
    ]))
]
