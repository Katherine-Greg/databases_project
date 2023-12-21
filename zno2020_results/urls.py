from django.urls import path

from zno2020_results.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "zno_results"
