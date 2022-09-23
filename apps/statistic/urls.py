from django.urls import path, include

from apps.statistic.views import AdminMainStatisticsView, AdminDateStatistics

urlpatterns = [
    path('admin/statistics/', include([
        path('', AdminMainStatisticsView.as_view()),
        path('date/', AdminDateStatistics.as_view())
    ]))
]