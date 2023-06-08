from django.urls import include, path

from .views import OrderListView

app_name = "tasks"

urlpatterns = [
    path("", OrderListView.as_view(), name="list"),
]
