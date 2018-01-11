from django.shortcuts import render

# Create your views here.
from django.views import View


class ControlsView(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'controls.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
