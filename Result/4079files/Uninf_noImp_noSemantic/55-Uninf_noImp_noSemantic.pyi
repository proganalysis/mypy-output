from ..connector import DBConnector as DBConnector
from typing import Any, Optional

class sqlite3_connection:
    conn: Any = ...
    def __init__(self, sqlite_file: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

def getQueryGeometryName(sqlite_file: Any): ...
def classFactory(): ...

class VLayerRegistry:
    _instance: Any = ...
    @classmethod
    def instance(cls): ...
    layers: Any = ...
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def has(self, k: Any): ...
    def get(self, k: Any): ...
    def __getitem__(self, k: Any): ...
    def set(self, k: Any, l: Any) -> None: ...
    def __setitem__(self, k: Any, l: Any) -> None: ...
    def items(self): ...
    def getLayer(self, l: Any): ...

class VLayerConnector(DBConnector):
    def __init__(self, uri: Any) -> None: ...
    sql: Any = ...
    def _execute(self, cursor: Any, sql: Any): ...
    def _get_cursor(self, name: Optional[Any] = ...) -> None: ...
    def _get_cursor_columns(self, c: Any): ...
    def uri(self): ...
    def getInfo(self): ...
    def getSpatialInfo(self) -> None: ...
    def hasSpatialSupport(self): ...
    def hasRasterSupport(self): ...
    def hasCustomQuerySupport(self): ...
    def hasTableColumnEditingSupport(self): ...
    def fieldTypes(self): ...
    def getSchemas(self) -> None: ...
    def getTables(self, schema: Optional[Any] = ..., add_sys_tables: bool = ...): ...
    def getVectorTables(self, schema: Optional[Any] = ...): ...
    def getRasterTables(self, schema: Optional[Any] = ...): ...
    def getTableRowCount(self, table: Any): ...
    def getTableFields(self, table: Any): ...
    def getTableIndexes(self, table: Any): ...
    def getTableConstraints(self, table: Any) -> None: ...
    def getTableTriggers(self, table: Any): ...
    def deleteTableTrigger(self, trigger: Any, table: Optional[Any] = ...) -> None: ...
    def getTableExtent(self, table: Any, geom: Any): ...
    def getViewDefinition(self, view: Any) -> None: ...
    def getSpatialRefInfo(self, srid: Any): ...
    def isVectorTable(self, table: Any): ...
    def isRasterTable(self, table: Any): ...
    def createTable(self, table: Any, field_defs: Any, pkey: Any): ...
    def deleteTable(self, table: Any): ...
    def emptyTable(self, table: Any): ...
    def renameTable(self, table: Any, new_table: Any): ...
    def moveTable(self, table: Any, new_table: Any, new_schema: Optional[Any] = ...): ...
    def createView(self, view: Any, query: Any): ...
    def deleteView(self, view: Any): ...
    def renameView(self, view: Any, new_name: Any): ...
    def runVacuum(self): ...
    def addTableColumn(self, table: Any, field_def: Any): ...
    def deleteTableColumn(self, table: Any, column: Any) -> None: ...
    def updateTableColumn(self, table: Any, column: Any, new_name: Any, new_data_type: Optional[Any] = ..., new_not_null: Optional[Any] = ..., new_default: Optional[Any] = ..., comment: Optional[Any] = ...) -> None: ...
    def renameTableColumn(self, table: Any, column: Any, new_name: Any): ...
    def setColumnType(self, table: Any, column: Any, data_type: Any): ...
    def setColumnDefault(self, table: Any, column: Any, default: Any): ...
    def setColumnNull(self, table: Any, column: Any, is_null: Any): ...
    def isGeometryColumn(self, table: Any, column: Any): ...
    def addGeometryColumn(self, table: Any, geom_column: str = ..., geom_type: str = ..., srid: int = ..., dim: int = ...): ...
    def deleteGeometryColumn(self, table: Any, geom_column: Any): ...
    def addTableUniqueConstraint(self, table: Any, column: Any): ...
    def deleteTableConstraint(self, table: Any, constraint: Any): ...
    def addTablePrimaryKey(self, table: Any, column: Any): ...
    def createTableIndex(self, table: Any, name: Any, column: Any, unique: bool = ...): ...
    def deleteTableIndex(self, table: Any, name: Any): ...
    def createSpatialIndex(self, table: Any, geom_column: str = ...): ...
    def deleteSpatialIndex(self, table: Any, geom_column: str = ...): ...
    def hasSpatialIndex(self, table: Any, geom_column: str = ...): ...
    def execution_error_types(self): ...
    def connection_error_types(self): ...
    def getSqlDictionary(self): ...
    def getQueryBuilderDictionary(self): ...
