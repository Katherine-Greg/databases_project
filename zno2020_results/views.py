from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from zno2020_results.forms import ResultCreationForm, StudentCreationForm, InstitutionCreationForm, LocationCreationForm
from zno2020_results.models import Student, Institution, StudentResults, Location


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    page_name = "index"
    num_students = Student.objects.count()
    num_instituts = Institution.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "page_name": page_name,
        "num_students": num_students,
        "num_instituts": num_instituts,
        "num_visits": num_visits + 1,
    }

    return render(request, "zno2020_results/index.html", context=context)


def student_search(request: HttpRequest) -> HttpResponse:
    birth_year = request.GET.get("birth_year")
    sex = request.GET.get("sex")
    type = request.GET.get("type")
    location = request.GET.get("location")
    institution = request.GET.get("institution")

    filtered_students = Student.objects.all()
    if birth_year:
        filtered_students = filtered_students.filter(birth_year=birth_year)
    if sex:
        filtered_students = filtered_students.filter(sex=sex)
    if type:
        filtered_students = filtered_students.filter(type=type)
    if location:
        filtered_students = filtered_students.filter(location=location)
    if institution:
        filtered_students = filtered_students.filter(institution=institution)

    return render(request, "zno2020_results/student_search.html", {"students": filtered_students})


class StudentListView(generic.ListView):
    model = Student
    queryset = Student.objects.all()
    paginate_by = 8


class StudentDetailView(generic.DetailView):
    model = Student


class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentCreationForm
    success_url = reverse_lazy("zno2020_results:student-list")


class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("zno2020_results:student-list")


class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = "zno2020_results/student_confirm_delete.html"
    success_url = reverse_lazy("zno2020_results:student-list")


class InstitutionListView(generic.ListView):
    model = Institution
    queryset = Institution.objects.all()
    paginate_by = 8


class InstitutionCreateView(generic.CreateView):
    model = Institution
    form_class = InstitutionCreationForm
    success_url = reverse_lazy("zno2020_results:institution-list")


class InstitutionUpdateView(generic.UpdateView):
    model = Institution
    fields = "__all__"
    success_url = reverse_lazy("zno2020_results:institution-list")


class InstitutionDeleteView(generic.DeleteView):
    model = Institution
    template_name = "zno2020_results/institution_confirm_delete.html"
    success_url = reverse_lazy("zno2020_results:institution-list")


class LocationListView(generic.ListView):
    model = Location
    queryset = Location.objects.all()
    paginate_by = 8


class LocationCreateView(generic.CreateView):
    model = Location
    form_class = LocationCreationForm
    success_url = reverse_lazy("zno2020_results:location-list")


class LocationUpdateView(generic.UpdateView):
    model = Location
    fields = "__all__"
    success_url = reverse_lazy("zno2020_results:location-list")


class LocationDeleteView(generic.DeleteView):
    model = Location
    template_name = "zno2020_results/location_confirm_delete.html"
    success_url = reverse_lazy("zno2020_results:location-list")


class ResultListView(generic.ListView):
    model = StudentResults
    queryset = StudentResults.objects.all()
    paginate_by = 8


class ResultCreateView(generic.CreateView):
    model = StudentResults
    form_class = ResultCreationForm
    success_url = reverse_lazy("zno2020_results:studentresults-list")


class ResultUpdateView(generic.UpdateView):
    model = StudentResults
    fields = "__all__"
    success_url = reverse_lazy("zno2020_results:studentresults-list")


class ResultDeleteView(generic.DeleteView):
    model = StudentResults
    template_name = "zno2020_results/studentresults_confirm_delete.html"
    success_url = reverse_lazy("zno2020_results:studentresults-list")
