from django.shortcuts import render
# Create your views here.
# from controls.forms import ControlsForm
from django.views.generic import DetailView

from .models import ControlsModel


class ControlsView(DetailView):
    model = ControlsModel
    template_name = 'controls/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
                      # {"salt_level": 0.5, "vacation_mode": "Off", "days_away": 2, "system_alarm": "Off",
                      #  "system_alarm_time": arrow.now().strftime("%H:%M:%S %m-%d-%Y"),
                      #  "time_of_day": arrow.now().format("h:mm:ss a"), "current_day_of_week": arrow.now().format("dddd"),
                      #  "current_date": arrow.now().format("M/D/YYYY"), "auto_dst": "Off", })

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().post(request, *args, **kwargs)
