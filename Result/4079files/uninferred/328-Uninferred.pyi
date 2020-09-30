from common.trace import traceln as traceln
from tasks.DU_ABPTableSkewed_txtBIO_sepSIO import NodeType_BIESO_to_BIO_Shape
from tasks.DU_CRF_Task import DU_CRF_Task
from typing import Any, Optional

class NodeType_BIESO_to_SIOStSmSb_Shape(NodeType_BIESO_to_BIO_Shape):
    bColumnHeader: bool = ...
    dConverter: Any = ...
    def parseDomNodeLabel(self, domnode: Any, defaultCls: Optional[Any] = ...): ...

class DU_ABPTableSkewedRowCutLine(DU_CRF_Task):
    sXmlFilenamePattern: str = ...
    iBlockVisibility: Any = ...
    iLineVisibility: Any = ...
    fCutHeight: Any = ...
    bCutAbove: Any = ...
    lRadAngle: Any = ...
    @classmethod
    def getConfiguredGraphClass(cls): ...
    def __init__(self, sModelName: Any, sModelDir: Any, iBlockVisibility: Optional[Any] = ..., iLineVisibility: Optional[Any] = ..., fCutHeight: Optional[Any] = ..., bCutAbove: Optional[Any] = ..., lRadAngle: Optional[Any] = ..., sComment: Optional[Any] = ..., C: Optional[Any] = ..., tol: Optional[Any] = ..., njobs: Optional[Any] = ..., max_iter: Optional[Any] = ..., inference_cache: Optional[Any] = ...) -> None: ...
