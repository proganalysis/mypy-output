# (generated with --quick)

from typing import Any

config: Any

def create_image_queue_graph(files, pixel_depth, height, width, channels, batch_size, capacity) -> Any: ...
def create_model_graph(height, width, channels, num_labels) -> Any: ...
def get_data(data_directory) -> Any: ...
def main() -> None: ...
def train_model(queue_graph, model_graph, placeholder_list, train_list, log_list) -> None: ...
