from django.urls import path, include

from apps.core.views import AdminOTMListAndCreateView, AdminOTMRetrieveEditAndDeleteView

urlpatterns = [
    path('admin/otm/', include([
        path('', AdminOTMListAndCreateView.as_view()),
        path('<int:pk>/', AdminOTMRetrieveEditAndDeleteView.as_view()),
    ]))
]