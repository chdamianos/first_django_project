from django.shortcuts import render
from django.views import View
# Base View Class = View
class CourseView(View):
    template_name = "about.html"
    # Create your views here.
    def get(self, request, *args, **kwargs):
        # GET method
        return render(request, self.template_name, {})   
    # # to handle forms
    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {}) 
# Create your views here.
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})