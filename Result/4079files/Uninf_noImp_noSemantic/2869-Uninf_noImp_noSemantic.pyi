from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...
