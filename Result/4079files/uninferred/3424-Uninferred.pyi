import argparse
from typing import Any

class ArgumentParserError(Exception): ...

class NewArgumentParser(argparse.ArgumentParser):
    def error(self, message: Any) -> None: ...

def parse_args(args: Any): ...
def main(args: list=...) -> Any: ...