from django.urls import path

from zno2020_results.views import (index,
                                   StudentListView,
                                   InstitutionListView,
                                   ResultListView,
                                   ResultCreateView,
                                   ResultUpdateView,
                                   ResultDeleteView,
                                   StudentCreateView,
                                   StudentUpdateView,
                                   StudentDeleteView,
                                   InstitutionCreateView,
                                   InstitutionUpdateView,
                                   InstitutionDeleteView,
                                   LocationListView,
                                   LocationDeleteView,
                                   LocationCreateView,
                                   LocationUpdateView,
                                   StudentDetailView,
                                   student_search)

urlpatterns = [
    path("", index, name="index"),
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/search/", student_search, name="student-search"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("students/create/", StudentCreateView.as_view(), name="student-create"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),

    path("institutions/", InstitutionListView.as_view(), name="institution-list"),
    path("institutions/create/", InstitutionCreateView.as_view(), name="institution-create"),
    path("institutions/<int:pk>/update/", InstitutionUpdateView.as_view(), name="institution-update"),
    path("institutions/<int:pk>/delete/", InstitutionDeleteView.as_view(), name="institution-delete"),

    path("locations/", LocationListView.as_view(), name="location-list"),
    path("locations/create/", LocationCreateView.as_view(), name="location-create"),
    path("locations/<int:pk>/update/", LocationUpdateView.as_view(), name="location-update"),
    path("locations/<int:pk>/delete/", LocationDeleteView.as_view(), name="location-delete"),

    path("results/", ResultListView.as_view(), name="studentresults-list"),
    path("results/create/", ResultCreateView.as_view(), name="studentresults-create"),
    path("results/<int:pk>/update/", ResultUpdateView.as_view(), name="studentresults-update"),
    path("results/<int:pk>/delete/", ResultDeleteView.as_view(), name="studentresults-delete"),
]

app_name = "zno2020_results"
