from django.urls import path, include

from apps.student.views import AdminStudentAddView

urlpatterns = [
    path('admin/student/', include([
        path('add/', AdminStudentAddView.as_view())
    ]))
]
