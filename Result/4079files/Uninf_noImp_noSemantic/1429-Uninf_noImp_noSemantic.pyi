import argparse
import kazoo.exceptions
from typing import Any, Iterable, Iterator

ZK_DEFAULT_CLUSTER_TYPE: str
ZK_TOPOLOGY_DIR: str
LOG_FORMAT: str
log: Any

def parse_args() -> argparse.Namespace: ...
def get_zk_cluster_locations(cluster_type: str) -> Iterator[str]: ...
def get_zk_topology(cluster_type: str, cluster_location: str) -> Iterable[str]: ...
def clean(simulate: bool, zk: kazoo.client.KazooClient) -> int: ...
def main() -> None: ...
