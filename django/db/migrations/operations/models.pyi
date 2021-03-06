from typing import List, Tuple, Set

from django.db.migrations.operations.base import Operation
from django.db.models.fields import Field


class ModelOperation(Operation):
    def __init__(self, name): ...


class CreateModel(ModelOperation):
    def __init__(self, name: str, fields: List[Tuple[str, Field]], options=None, bases=None, managers=None) -> None: ...


class DeleteModel(ModelOperation): ...


class RenameModel(ModelOperation):
    def __init__(self, old_name: str, new_name: str) -> None: ...


class AlterModelTable(ModelOperation): ...


class ModelOptionOperation(ModelOperation): ...


class FieldRelatedOptionOperation(ModelOptionOperation): ...


class AlterUniqueTogether(FieldRelatedOptionOperation):
    def __init__(self, name: str, unique_together: Set[Tuple[str, str]]) -> None: ...


class AlterIndexTogether(FieldRelatedOptionOperation): ...


class AlterOrderWithRespectTo(FieldRelatedOptionOperation): ...


class AlterModelOptions(ModelOptionOperation): ...


class AlterModelManagers(ModelOptionOperation): ...


class IndexOperation(Operation): ...


class AddIndex(IndexOperation): ...


class RemoveIndex(IndexOperation): ...
