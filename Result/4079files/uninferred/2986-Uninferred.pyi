from django.db import migrations
from typing import Any

def load_fixture(apps: Any, schema_editor: Any) -> None: ...

class Migration(migrations.Migration):
    dependencies: Any = ...
    operations: Any = ...