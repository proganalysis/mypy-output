import six
from fabricio import docker, kubernetes
from typing import Any, Optional

class Migration(six.text_type):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class DjangoMixin(docker.BaseService):
    @staticmethod
    def _migrate(image: Any, options: Any) -> None: ...
    def migrate(self, tag: Optional[Any] = ..., registry: Optional[Any] = ..., account: Optional[Any] = ...) -> None: ...
    @staticmethod
    def _get_parent_migration(migration: Any, migrations: Any): ...
    def get_revert_migrations(self, current_migrations: Any, backup_migrations: Any): ...
    def migrate_back(self) -> None: ...

class DjangoContainer(docker.Container, DjangoMixin): ...
class DjangoService(docker.Service, DjangoMixin): ...
class DjangoStack(docker.Stack, DjangoMixin): ...
class DjangoKubernetes(kubernetes.Configuration, DjangoMixin): ...
