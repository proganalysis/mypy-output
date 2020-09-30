from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from typing import Any, Optional

class MLEngineHook(GoogleCloudBaseHook):
    _mlengine: Any = ...
    def __init__(self, gcp_conn_id: str = ..., delegate_to: Optional[Any] = ...) -> None: ...
    def normalize_mlengine_job_id(self, job_id: Any): ...
    def get_conn(self): ...
    def create_job(self, project_id: Any, job: Any, use_existing_job_fn: Optional[Any] = ...): ...
    def _get_job(self, project_id: Any, job_id: Any): ...
    def _wait_for_job_done(self, project_id: Any, job_id: Any, interval: int = ...): ...

class MLEngineTrainingOperator(BaseOperator):
    _project_id: Any = ...
    _job_id: Any = ...
    _package_uris: Any = ...
    _training_python_module: Any = ...
    _training_args: Any = ...
    _region: Any = ...
    _scale_tier: Any = ...
    _master_type: Any = ...
    _gcp_conn_id: Any = ...
    _delegate_to: Any = ...
    _mode: Any = ...
    def __init__(self, project_id: Any, job_id: Any, package_uris: Any, training_python_module: Any, training_args: Any, region: Any, scale_tier: Optional[Any] = ..., master_type: Optional[Any] = ..., gcp_conn_id: str = ..., delegate_to: Optional[Any] = ..., mode: str = ..., *args: Any, **kwargs: Any) -> None: ...
    def execute(self, context: Any): ...

class GoogleMLEnginePlugin(AirflowPlugin):
    name: str = ...
    operators: Any = ...
    hooks: Any = ...
    executors: Any = ...
    macros: Any = ...
    admin_views: Any = ...
    flask_blueprints: Any = ...
    menu_links: Any = ...