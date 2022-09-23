from django.urls import path, include

from apps.statistic.views import AdminMainStatisticsView

urlpatterns = [
    path('admin/statistics/', include([
        path('', AdminMainStatisticsView.as_view())
    ]))
]