# generated by datamodel-codegen:
#   filename:  selectors-latest.json
#   timestamp: 2024-08-05T21:30:57+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel


class Default(RootModel[str]):
    root: str = Field(..., pattern='\\{\\{.*\\}\\}')


class Method(Enum):
    tag = 'tag'
    source = 'source'
    path = 'path'
    file = 'file'
    fqn = 'fqn'
    package = 'package'
    config = 'config'
    test_type = 'test_type'
    test_name = 'test_name'
    state = 'state'
    exposure = 'exposure'
    metric = 'metric'
    result = 'result'
    source_status = 'source_status'
    group = 'group'
    wildcard = 'wildcard'


class IndirectSelection(Enum):
    buildable = 'buildable'
    cautious = 'cautious'
    eager = 'eager'


class JinjaString(RootModel[str]):
    root: str = Field(..., pattern='\\{\\{.*\\}\\}')


class BooleanOrJinjaString(RootModel[Union[JinjaString, bool]]):
    root: Union[JinjaString, bool]


class DefinitionBlock(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    method: Optional[Method] = None
    value: Optional[str] = None
    children: Optional[BooleanOrJinjaString] = None
    parents: Optional[BooleanOrJinjaString] = None
    children_depth: Optional[float] = None
    parents_depth: Optional[float] = None
    childrens_parents: Optional[BooleanOrJinjaString] = None
    indirect_selection: Optional[IndirectSelection] = None


class IntersectionBlock(RootModel[List[DefinitionBlock]]):
    root: List[DefinitionBlock]


class ExcludeBlock(RootModel[List[Union[IntersectionBlock, DefinitionBlock]]]):
    root: List[Union[IntersectionBlock, DefinitionBlock]]


class UnionBlock(
    RootModel[List[Union[IntersectionBlock, DefinitionBlock, ExcludeBlock]]]
):
    root: List[Union[IntersectionBlock, DefinitionBlock, ExcludeBlock]]


class Selector(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Union[Default, bool]] = None
    definition: Optional[Union[DefinitionBlock, str, UnionBlock]] = None


class Selectors(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    selectors: List[Selector] = Field(..., min_length=1)