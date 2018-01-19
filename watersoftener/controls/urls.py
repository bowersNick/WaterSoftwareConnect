from django.urls import path

from controls.views import ControlsView

urlpatterns = [
    path('', ControlsView.as_view(), name="controls"),
]