from django.core.management import BaseCommand
from typing import Any

class Command(BaseCommand):
    help: str = ...
    def handle(self, *args: Any, **options: Any) -> None: ...
    def _regenerate_zip(self, imageset: Any) -> None: ...