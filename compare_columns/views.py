from django.shortcuts import render
from django.views.generic import ListView
from vertical_multi_columns.views import EvenVMCView
from django.views.generic import ListView, TemplateView

from . import indata

class About(TemplateView):

    template_name = "about.html"

class Audrey(ListView):

    def get(self, request):
        """Provide the data to be displayed"""
        raw_api_data = indata.decoded_api_json_data()
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        subset_sorted_api_data = []
        for i in sorted_api_data:
            i_subset = {key: i[key] for key in ['name', 'colour']}
            subset_sorted_api_data.append(i_subset)
        return render(request, "audrey.html", {"mylist": subset_sorted_api_data})

class Susan(EvenVMCView):

    def __init__(self):
        super().__init__(num_columns=3)

    def get_data(self):
        """Provide the data to be displayed"""
        raw_api_data = indata.decoded_api_json_data()
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        return sorted_api_data

    template_name = "susan.html"
    context_object_name = "rows"