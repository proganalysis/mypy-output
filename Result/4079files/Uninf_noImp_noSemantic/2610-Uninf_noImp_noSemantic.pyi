from misc.deploy import Application

class Microservice(Application):
    def _check(self) -> None: ...
    def _after_deploy(self) -> None: ...
    def _after_promote(self) -> None: ...
    @staticmethod
    def _do_migrations() -> None: ...
