from django.views.generic import TemplateView
from typing import Any

class HeartbeatsView(TemplateView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...
