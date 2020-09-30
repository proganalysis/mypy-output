from jenkins_job_linter.linters import Linter
from typing import Any
from xml.etree import ElementTree

FAILING_SHEBANG_ARGS: Any
PASSING_SHEBANG_ARGS: Any

def _elementtree_from_str(xml_string: str) -> ElementTree.ElementTree: ...

class ShellTest:
    _xml_template: str = ...
    _shell_builder_template: str = ...
    def test_non_project_skipped(self) -> None: ...

class TestCheckShebang(ShellTest):
    def test_project_with_shell(self, expected: Any, shell_string: Any) -> None: ...
    def test_project_with_no_shell_part_skipped(self) -> None: ...
    def test_multiple_shell_parts(self, expected: Any, shebangs: Any) -> None: ...
    def test_allow_default_shebang_false(self) -> None: ...
    def test_required_shell_options(self, expected: Any, required: Any, shell_string: Any) -> None: ...

class TestCheckForEmptyShell(ShellTest):
    def test_linter(self, expected: Any, script: Any) -> None: ...

class TestEnsureTimestamps:
    def test_linter(self, expected: Any, xml_string: Any) -> None: ...

class TestEnsureWorkspaceCleanup:
    def test_linter(self, expected: Any, xml_string: Any) -> None: ...

class TestCheckJobReferences:
    _trigger_builder_template: str = ...
    _config_template: str = ...
    def test_linter(self, expected: Any, configured_projects: Any, object_names: Any) -> None: ...
    def test_completely_empty_projects_node(self) -> None: ...

class TestCheckColumnConfiguration:
    def test_linter(self, expected: Any, xml_string: Any) -> None: ...

class TestCheckEnvInject:
    _template: str = ...
    def test_no_properties_configured(self, expected: Any, required_environment_settings: Any) -> None: ...
    def test_linter(self, expected: Any, properties_content: Any, required_environment_settings: Any) -> None: ...

class TestLinter:
    class LintTestSubclass(Linter):
        description: str = ...
        root_tag: str = ...
        def actual_check(self): ...
    def test_check_and_text_passed_through(self, mocker: Any) -> None: ...
    def test_wrong_root_tag_is_skipped_without_check(self, mocker: Any) -> None: ...
