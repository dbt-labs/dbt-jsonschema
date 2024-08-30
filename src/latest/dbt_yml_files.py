# generated by datamodel-codegen:
#   filename:  dbt_yml_files-latest.json
#   timestamp: 2024-07-25T00:00:09+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel


class Column(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    data_type: Optional[str] = None


class Type(Enum):
    dashboard = "dashboard"
    notebook = "notebook"
    analysis = "analysis"
    ml = "ml"
    application = "application"


class Maturity(Enum):
    high = "high"
    medium = "medium"
    low = "low"


class Argument(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    type: Optional[str] = None


class Access(Enum):
    private = "private"
    protected = "protected"
    public = "public"


class Defaults(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    agg_time_dimension: Optional[str] = None


class Format(Enum):
    csv = "csv"
    dict = "dict"
    sql = "sql"


class ExpectDict(BaseModel):
    format: Literal["dict"] = Field("dict")
    rows: List[Dict[str, Any]] = Field(
        ...,
        description="When `format` is `dict`, each item should be a dictionary containing a key-value pair for each column and its value, e.g. `{id: 1, code: 'ABC'}`",
    )


class ExpectCSV(BaseModel):
    format: Literal["csv"] = Field("csv")
    rows: Optional[str] = Field(
        None,
        description="When `format` is csv or sql, a string containing comma-separated headers and values. Alternatively provide a fixture. Use the pipe character | to create a multi-line string in YAML.",
    )
    fixture: Optional[str] = Field(
        None,
        description="Specify the name of a fixture instead of providing `rows`.",
    )


class ExpectSQL(BaseModel):
    format: Literal["sql"] = Field("sql")
    rows: Optional[str] = Field(
        None,
        description="When `format` is csv or sql, a string containing comma-separated headers and values. Alternatively provide a fixture. Use the pipe character | to create a multi-line string in YAML.",
    )
    fixture: Optional[str] = Field(
        None,
        description="Specify the name of a fixture instead of providing `rows`.",
    )


Expect = Union[ExpectDict, ExpectCSV, ExpectSQL]


class GivenItem(BaseModel):
    fixture: Optional[str] = Field(
        None,
        description="Only relevant when format is csv. Specify the name of a fixture instead of providing `rows`.",
    )
    format: Optional[Format] = Field(
        None, description="Defaults to `dict` when not specified"
    )
    input: Optional[str] = Field(
        None,
        description="The relation whose inputs you need to mock. Enclose in ref or source without curly braces",
        examples=[
            "ref('model_b')",
            "ref('upstream_project', 'model_b')",
            "source('schema', 'table')",
        ],
    )
    additionalProperties: Optional[Any] = None


class Overrides(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    env_vars: Optional[Dict[str, Any]] = None
    macros: Optional[Dict[str, Any]] = Field(
        None, examples=[{"is_incremental": "true"}]
    )
    vars: Optional[Dict[str, Any]] = None


class AggregationTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    percentile: Optional[float] = None
    use_approximate_percentile: Optional[bool] = None
    use_discrete_percentile: Optional[bool] = None


class ArrayOfStrings(RootModel[List[str]]):
    root: List[str]


class Calculation(Enum):
    conversions = "conversions"
    conversion_rate = "conversion_rate"
    CONVERSIONS = "CONVERSIONS"
    CONVERSION_RATE = "CONVERSION_RATE"


class ConstantProperty(BaseModel):
    base_property: str = Field(..., description="DIMENSION or ENTITY")
    conversion_property: str = Field(..., description="DIMENSION or ENTITY")


class GrainToDate(Enum):
    day = "day"
    week = "week"
    month = "month"
    quarter = "quarter"
    year = "year"


class TimeGranularity(Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"
    day = "day"
    week = "week"
    month = "month"
    quarter = "quarter"
    year = "year"


class DocsConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    node_color: Optional[str] = Field(
        None,
        description="The color of the node on the DAG in the documentation. It must be an Hex code or a valid CSS color name.",
        pattern="^(#[a-fA-F0-9]{3}|#[a-fA-F0-9]{6}|[^#][a-zA-Z]*)$",
    )
    show: Optional[bool] = True


class EntityType(Enum):
    PRIMARY = "PRIMARY"
    UNIQUE = "UNIQUE"
    FOREIGN = "FOREIGN"
    NATURAL = "NATURAL"
    primary = "primary"
    unique = "unique"
    foreign = "foreign"
    natural = "natural"


class Entity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        regex_engine="python-re",
    )
    name: str = Field(..., pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$")
    type: EntityType = Field(..., title="Entity Type")
    entity: Optional[str] = None
    expr: Optional[Union[str, bool]] = None


class ExportAs(Enum):
    table = "table"
    view = "view"
    cache = "cache"


class ExportConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    alias: Optional[str] = None
    export_as: Optional[ExportAs] = None
    schema_: Optional[str] = Field(None, alias="schema")


class Export(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    config: Optional[ExportConfig] = Field(None, title="Export Config")


class Period(Enum):
    minute = "minute"
    hour = "hour"
    day = "day"


class GroupName(RootModel[str]):
    root: str


class JinjaString(RootModel[str]):
    root: str = Field(..., pattern="\\{\\{.*\\}\\}")


class Agg(Enum):
    SUM = "SUM"
    MIN = "MIN"
    MAX = "MAX"
    AVG = "AVG"
    COUNT_DISTINCT = "COUNT_DISTINCT"
    SUM_BOOLEAN = "SUM_BOOLEAN"
    COUNT = "COUNT"
    PERCENTILE = "PERCENTILE"
    MEDIAN = "MEDIAN"
    sum = "sum"
    min = "min"
    max = "max"
    avg = "avg"
    count_distinct = "count_distinct"
    sum_boolean = "sum_boolean"
    count = "count"
    percentile = "percentile"
    median = "median"


class MetricInputMeasure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Optional[str] = None
    fill_nulls_with: Optional[Union[str, int]] = None
    filter: Optional[str] = None
    join_to_timespine: Optional[bool] = None


class MetricInputSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Optional[str] = None
    alias: Optional[str] = None
    filter: Optional[str] = None
    offset_window: Optional[str] = None


class AuthorizedView(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: str
    project: str


class OnConfigurationChange(Enum):
    apply = "apply"
    continue_ = "continue"
    fail = "fail"


class OnSchemaChange(Enum):
    append_new_columns = "append_new_columns"
    fail = "fail"
    ignore = "ignore"
    sync_all_columns = "sync_all_columns"


class OwnerWithEmail(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    email: str


class OwnerWithName(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str


Owner = Union[OwnerWithEmail, OwnerWithName]


class WindowChoice(Enum):
    MIN = "MIN"
    MAX = "MAX"
    min = "min"
    max = "max"


class NonAdditiveDimension(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    window_choice: Optional[WindowChoice] = None
    window_groupings: Optional[List[str]] = None


class NumberOrJinjaString(RootModel[Union[JinjaString, float]]):
    root: Union[JinjaString, float]


class RatioMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    denominator: Optional[MetricInputSchema] = None
    filter: Optional[str] = None
    numerator: Optional[MetricInputSchema] = None


class SimpleMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    measure: Optional[MetricInputMeasure] = None


class StringOrArrayOfStrings(RootModel[Union[str, ArrayOfStrings]]):
    root: Union[str, ArrayOfStrings]


class Severity(Enum):
    warn = "warn"
    error = "error"


class ValidityParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_end: Optional[bool] = None
    is_start: Optional[bool] = None


class Config(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tags: Optional[StringOrArrayOfStrings] = None


class Analyse(BaseModel):
    name: str
    description: Optional[str] = None
    columns: Optional[List[Column]] = None
    config: Optional[Config] = None
    docs: Optional[DocsConfig] = None
    group: Optional[GroupName] = None


class Exposure(BaseModel):
    name: str
    description: Optional[str] = None
    type: Type
    depends_on: List[str]
    label: Optional[str] = None
    maturity: Optional[Maturity] = None
    meta: Optional[Dict[str, Any]] = None
    owner: Owner
    tags: Optional[StringOrArrayOfStrings] = None
    url: Optional[str] = None


class Group(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    owner: Owner


class Macro(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    arguments: Optional[List[Argument]] = None
    docs: Optional[DocsConfig] = None


class SimpleMetricType(Enum):
    SIMPLE = "SIMPLE"
    simple = "simple"


class DerivedMetricType(Enum):
    DERIVED = "DERIVED"
    derived = "derived"


class CumulativeMetricType(Enum):
    CUMULATIVE = "CUMULATIVE"
    cumulative = "cumulative"


class ConversionMetricType(Enum):
    CONVERSION = "CONVERSION"
    conversion = "conversion"


class RatioMetricType(Enum):
    RATIO = "RATIO"
    ratio = "ratio"


class MetricBase(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        regex_engine="python-re",
    )
    name: str = Field(..., pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$")
    description: Optional[str] = None
    filter: Optional[str] = None
    group: Optional[GroupName] = None
    label: str


class SimpleMetric(MetricBase):
    type: SimpleMetricType
    type_params: SimpleMetricTypeParams


class DerivedMetric(MetricBase):
    type: DerivedMetricType
    type_params: DerivedMetricTypeParams


class CumulativeMetric(MetricBase):
    type: CumulativeMetricType
    type_params: CumulativeMetricTypeParams


class ConversionMetric(MetricBase):
    type: ConversionMetricType
    type_params: ConversionMetricTypeParams


class RatioMetric(MetricBase):
    type: RatioMetricType
    type_params: RatioMetricTypeParams


Metric = Union[
    SimpleMetric, DerivedMetric, CumulativeMetric, ConversionMetric, RatioMetric
]


class QueryParams(BaseModel):
    dimensions: Optional[ArrayOfStrings] = None
    metrics: Optional[ArrayOfStrings] = None
    where: Optional[ArrayOfStrings] = None
    additionalProperties: Optional[Any] = None


class SavedQuery(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: str
    exports: Optional[List[Export]] = None
    label: str
    query_params: QueryParams


class UnitTestConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    meta: Optional[Dict[str, Any]] = None
    tags: Optional[StringOrArrayOfStrings] = None


class UnitTest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    config: Optional[UnitTestConfig] = Field(None, title="Unit Test Config")
    expect: Expect
    given: Optional[List[GivenItem]] = None
    model: str = Field(
        ...,
        description="The name of the model whose behaviour you are testing. Does not need to be wrapped in a ref.",
        examples=["my_model"],
    )
    overrides: Optional[Overrides] = None
    additionalProperties: Optional[Any] = None


class BooleanOrJinjaString(RootModel[Union[JinjaString, bool]]):
    root: Union[JinjaString, bool]


class Constraint(BaseModel):
    name: Optional[str] = None
    type: str
    columns: Optional[StringOrArrayOfStrings] = None
    expression: Optional[str] = None
    warn_unenforced: Optional[BooleanOrJinjaString] = None
    warn_unsupported: Optional[BooleanOrJinjaString] = None


class Constraints(RootModel[List[Constraint]]):
    root: List[Constraint]


class ConversionTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    base_measure: MetricInputMeasure
    calculation: Optional[Calculation] = Calculation.conversion_rate
    constant_properties: Optional[List[ConstantProperty]] = None
    conversion_measure: MetricInputMeasure
    entity: str = Field(..., description="The entity to calculate over")
    window: Optional[str] = None


class ConversionMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    conversion_type_params: Optional[ConversionTypeParams] = None


class CumulativeMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    grain_to_date: Optional[GrainToDate] = None
    measure: Optional[MetricInputMeasure] = None
    window: Optional[str] = None


class DerivedMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expr: Optional[str] = None
    metrics: Optional[List[MetricInputSchema]] = None


class DimensionTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    time_granularity: TimeGranularity
    validity_params: Optional[ValidityParams] = None


class FreshnessRules(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    count: NumberOrJinjaString
    period: Period


class Grants(RootModel[Dict[str, StringOrArrayOfStrings]]):
    root: Dict[str, StringOrArrayOfStrings] = Field(
        ...,
        description="grant config. each key is a database permission and the value is the grantee of that permission",
    )


class IncludeExclude(BaseModel):
    exclude: Optional[StringOrArrayOfStrings] = None
    include: Optional[StringOrArrayOfStrings] = None


class Measure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        regex_engine="python-re",
    )
    name: str = Field(..., pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$")
    description: Optional[str] = None
    agg: Agg
    agg_params: Optional[AggregationTypeParams] = None
    agg_time_dimension: Optional[str] = Field(
        None, pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$"
    )
    create_metric: Optional[bool] = None
    create_metric_display_name: Optional[str] = None
    expr: Optional[Union[str, int, bool]] = None
    label: Optional[str] = None
    non_additive_dimension: Optional[NonAdditiveDimension] = None


class Contract(BaseModel):
    enforced: Optional[BooleanOrJinjaString] = None


class ModelConfigs(BaseModel):
    auto_refresh: Optional[BooleanOrJinjaString] = None
    backup: Optional[BooleanOrJinjaString] = None
    contract: Optional[Contract] = None
    file_format: Optional[str] = None
    grant_access_to: Optional[List[AuthorizedView]] = Field(
        None,
        description="Configuration, specific to BigQuery adapter, used to setup authorized views.",
        title="Authorized views",
    )
    grants: Optional[Grants] = None
    hours_to_expiration: Optional[float] = Field(
        None,
        description="Configuration specific to BigQuery adapter used to set an expiration delay (in hours) to a table.",
    )
    kms_key_name: Optional[str] = Field(
        None,
        description="Configuration of the KMS key name, specific to BigQuery adapter.",
        pattern="projects/[a-zA-Z0-9_-]*/locations/[a-zA-Z0-9_-]*/keyRings/.*/cryptoKeys/.*",
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description="Configuration specific to BigQuery adapter used to add labels and tags to tables/views created by dbt.",
        title="Label configs",
    )
    location: Optional[str] = None
    materialized: Optional[str] = None
    on_configuration_change: Optional[OnConfigurationChange] = None
    on_schema_change: Optional[OnSchemaChange] = None
    snowflake_warehouse: Optional[str] = None
    sql_header: Optional[str] = None
    target_lag: Optional[str] = Field(
        None, pattern="^(?:downstream|\\d+\\s*(?:seconds|minutes|hours|days))$"
    )


class PersistDocsConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    columns: Optional[BooleanOrJinjaString] = Field(
        default_factory=lambda: BooleanOrJinjaString.model_validate(True)
    )
    relation: Optional[BooleanOrJinjaString] = Field(
        default_factory=lambda: BooleanOrJinjaString.model_validate(True)
    )


class TestConfigs(BaseModel):
    alias: Optional[str] = Field(
        None, description="Only relevant when `store_failures` is true"
    )
    database: Optional[str] = Field(
        None, description="Only relevant when `store_failures` is true"
    )
    enabled: Optional[BooleanOrJinjaString] = None
    error_if: Optional[str] = None
    fail_calc: Optional[str] = None
    limit: Optional[float] = None
    schema_: Optional[str] = Field(
        None, alias="schema", description="Only relevant when `store_failures` is true"
    )
    severity: Optional[Union[JinjaString, Severity]] = None
    store_failures: Optional[BooleanOrJinjaString] = None
    tags: Optional[StringOrArrayOfStrings] = None
    warn_if: Optional[str] = None


class SnapshotConfig(BaseModel):
    alias: Optional[str] = None
    check_cols: Optional[StringOrArrayOfStrings] = None
    enabled: Optional[BooleanOrJinjaString] = None
    grants: Optional[Grants] = None
    persist_docs: Optional[PersistDocsConfig] = None
    post_hook: Optional[ArrayOfStrings] = Field(None, alias="post-hook")
    pre_hook: Optional[ArrayOfStrings] = Field(None, alias="pre-hook")
    quote_columns: Optional[BooleanOrJinjaString] = None
    strategy: Optional[str] = None
    tags: Optional[StringOrArrayOfStrings] = None
    target_database: Optional[str] = None
    target_schema: Optional[str] = None
    unique_key: Optional[StringOrArrayOfStrings] = None
    updated_at: Optional[str] = None


class Quoting(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[BooleanOrJinjaString] = None
    identifier: Optional[BooleanOrJinjaString] = None
    schema_: Optional[BooleanOrJinjaString] = Field(None, alias="schema")


class Relationships(BaseModel):
    name: Optional[str] = None
    config: Optional[TestConfigs] = None
    field: str = Field(
        ..., description="The foreign key column", title="Relationships: Field"
    )
    to: str = Field(
        ..., examples=["ref('parent_model')", "source('parent_schema', 'parent_table')"]
    )
    where: Optional[str] = None


class RelationshipsTest(BaseModel):
    relationships: Optional[Relationships] = None


class AcceptedValues(BaseModel):
    name: Optional[str] = None
    config: Optional[TestConfigs] = None
    quote: Optional[bool] = None
    values: List[str]
    where: Optional[str] = None


class AcceptedValuesTest(BaseModel):
    accepted_values: Optional[AcceptedValues] = None


class NotNull(BaseModel):
    name: Optional[str] = None
    config: Optional[TestConfigs] = None
    where: Optional[str] = None


class NotNullTest(BaseModel):
    not_null: Optional[NotNull] = None


class Unique(BaseModel):
    name: Optional[str] = None
    config: Optional[TestConfigs] = None
    where: Optional[str] = None


class UniqueTest(BaseModel):
    unique: Optional[Unique] = None


class DataTests(
    RootModel[
        Union[str, RelationshipsTest, AcceptedValuesTest, NotNullTest, UniqueTest]
    ]
):
    root: Union[str, RelationshipsTest, AcceptedValuesTest, NotNullTest, UniqueTest]


class DimensionBase(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        regex_engine="python-re",
    )
    name: str = Field(..., pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$")
    description: Optional[str] = None
    expr: Optional[Union[str, bool]] = None
    is_partition: Optional[bool] = None


class TimeDimensionType(Enum):
    TIME = "TIME"
    time = "time"


class CategoricalDimensionType(Enum):
    CATEGORICAL = "CATEGORICAL"
    categorical = "categorical"


class CategoricalDimension(DimensionBase):
    type: CategoricalDimensionType


class TimeDimension(DimensionBase):
    type: TimeDimensionType
    type_params: DimensionTypeParams


class Dimension(RootModel[Union[CategoricalDimension, TimeDimension]]):
    root: Union[CategoricalDimension, TimeDimension]


class FreshnessDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    warn_after: Optional[FreshnessRules] = FreshnessRules(count=1, period=Period.hour)
    error_after: Optional[FreshnessRules] = FreshnessRules(count=1, period=Period.day)
    filter: Optional[str] = ""

class SeedConfig(BaseModel):
    column_types: Optional[Dict[str, Any]] = None
    copy_grants: Optional[BooleanOrJinjaString] = None
    data_tests: Optional[List[DataTests]] = None
    database: Optional[str] = None
    enabled: Optional[BooleanOrJinjaString] = None
    grants: Optional[Grants] = None
    quote_columns: Optional[BooleanOrJinjaString] = None
    schema_: Optional[str] = Field(None, alias="schema")


class SemanticModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        regex_engine="python-re",
    )
    name: str = Field(..., pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$")
    description: Optional[str] = None
    defaults: Optional[Defaults] = None
    dimensions: Optional[List[Dimension]] = None
    entities: Optional[List[Entity]] = None
    measures: Optional[List[Measure]] = None
    model: str
    primary_entity: Optional[str] = None


class ColumnProperties(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    constraints: Optional[Constraints] = None
    data_tests: Optional[List[DataTests]] = None
    data_type: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    policy_tags: Optional[List[str]] = Field(
        None,
        description="Configurations, specific to BigQuery adapter, used to set policy tags on specific columns, enabling column-level security. Only relevant when `persist_docs.columns` is true.",
        title="Policy tags",
    )
    quote: Optional[BooleanOrJinjaString] = None
    tags: Optional[StringOrArrayOfStrings] = None
    tests: Optional[List[DataTests]] = None


class Version(BaseModel):
    columns: Optional[List[Union[IncludeExclude, ColumnProperties]]] = None
    config: Optional[ModelConfigs] = None
    v: float


class Model(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    access: Optional[Access] = None
    columns: Optional[List[ColumnProperties]] = None
    config: Optional[ModelConfigs] = None
    constraints: Optional[Constraints] = None
    data_tests: Optional[List[DataTests]] = None
    deprecation_date: Optional[str] = None
    docs: Optional[DocsConfig] = None
    group: Optional[GroupName] = None
    latest_version: Optional[float] = None
    meta: Optional[Dict[str, Any]] = None
    tests: Optional[List[DataTests]] = None
    versions: Optional[List[Version]] = None


class Seed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    columns: Optional[List[ColumnProperties]] = None
    config: Optional[SeedConfig] = Field(None, title="Seed Config")
    docs: Optional[DocsConfig] = None
    group: Optional[GroupName] = None
    tests: Optional[List[DataTests]] = None


class Snapshot(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = None
    columns: Optional[List[ColumnProperties]] = None
    config: Optional[SnapshotConfig] = Field(None, title="Snapshot Config")
    data_tests: Optional[List[DataTests]] = None
    docs: Optional[DocsConfig] = None
    group: Optional[GroupName] = None
    meta: Optional[Dict[str, Any]] = None
    tests: Optional[List[DataTests]] = None


class Table(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str = Field(
        ...,
        description="How you will identify the table in {{ source() }} calls. Unless `identifier` is also set, this will be the name of the table in the database.",
        title="Name",
    )
    description: Optional[str] = None
    columns: Optional[List[ColumnProperties]] = None
    external: Optional[Dict[str, Any]] = None
    freshness: Optional[FreshnessDefinition] = Field(FreshnessDefinition(), json_schema_extra={"$comment": "truly_nullable"})
    identifier: Optional[str] = Field(
        None,
        description="The table name as stored in the database. Only needed if you want to give the source a different name than what exists in the database (otherwise `name` is used by default)",
        title="Identifier",
    )
    loaded_at_field: Optional[str] = Field(
        None,
        description="Which column to check during data freshness tests. Only needed if the table has a different loaded_at_field to the one defined on the source overall.",
    )
    loader: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    quoting: Optional[Quoting] = None
    tags: Optional[StringOrArrayOfStrings] = None
    tests: Optional[List[DataTests]] = None


class Source(BaseModel):
    name: str = Field(
        ...,
        description="How you will identify the schema in {{ source() }} calls. Unless `schema` is also set, this will be the name of the schema in the database.",
    )
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    data_tests: Optional[List[DataTests]] = None
    database: Optional[str] = None
    freshness: Optional[FreshnessDefinition] = Field(FreshnessDefinition(), json_schema_extra={"$comment": "truly_nullable"})
    loaded_at_field: Optional[str] = None
    loader: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    overrides: Optional[str] = Field(
        None,
        description="The name of another package installed in your project. If that package has a source with the same name as this one, its properties will be applied on top of the base properties of the overridden source. https://docs.getdbt.com/reference/resource-properties/overrides",
        title="Package to Override",
    )
    quoting: Optional[Quoting] = None
    schema_: Optional[str] = Field(
        None,
        alias="schema",
        description="The schema name as stored in the database. Only needed if you want to use a different `name` than what exists in the database (otherwise `name` is used by default)",
    )
    tables: Optional[List[Table]] = None
    tags: Optional[StringOrArrayOfStrings] = None
    tests: Optional[List[DataTests]] = None


class DbtYmlFiles(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    version: Literal[2] = 2
    analyses: Optional[List[Analyse]] = None
    exposures: Optional[List[Exposure]] = None
    groups: Optional[List[Group]] = None
    macros: Optional[List[Macro]] = None
    metrics: Optional[List[Metric]] = None
    models: Optional[List[Model]] = None
    saved_queries: Optional[List[SavedQuery]] = None
    seeds: Optional[List[Seed]] = None
    semantic_models: Optional[List[SemanticModel]] = None
    snapshots: Optional[List[Snapshot]] = None
    sources: Optional[List[Source]] = None
    unit_tests: Optional[List[UnitTest]] = None
