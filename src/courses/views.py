from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Course
# Base View Class = View


class CourseView(View):
    template_name = "courses/course_detail.html"
    # Create your views here.
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)
    # # to handle forms
    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {})
# class CourseDetailView(View):
#     template_name = "about.html"
#     # Create your views here.
#     def get(self, request, *args, **kwargs):
#         # GET method
#         return render(request, self.template_name, {})
# Create your views here.


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
