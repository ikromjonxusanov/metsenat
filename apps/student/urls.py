from django.urls import path, include

from apps.student.views import AdminStudentAddView, AdminStudentListView

urlpatterns = [
    path('admin/student/', include([
        path('add/', AdminStudentAddView.as_view()),
        path('list/', AdminStudentListView.as_view()),
    ]))
]
