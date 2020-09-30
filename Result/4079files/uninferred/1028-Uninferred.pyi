import tensorflow as tf
from typing import Any, Optional

flags: Any
lt: Any
FLAGS: Any

def bounds_unlabeled(lower: float, upper: float, tensor: tf.Tensor, name: Optional[str]=...) -> tf.Tensor: ...
def bounds(lower: float, upper: float, labeled_tensor: lt.LabeledTensor, name: Optional[str]=...) -> lt.LabeledTensor: ...
def shape_unlabeled(tensor: tf.Tensor, name: Optional[str]=...) -> tf.Tensor: ...
def shape(labeled_tensor: lt.LabeledTensor, name: Optional[str]=...) -> lt.LabeledTensor: ...
def well_defined(): ...
