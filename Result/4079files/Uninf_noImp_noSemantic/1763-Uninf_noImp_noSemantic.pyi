from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help: str = ...
    def handle(self, *args: Any, **options: Any) -> None: ...