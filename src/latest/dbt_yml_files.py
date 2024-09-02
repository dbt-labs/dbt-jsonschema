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
    description: Optional[str] = ""
    data_type: Optional[str] = ""


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
    description: Optional[str] = ""
    type: Optional[str] = ""


class Access(Enum):
    private = "private"
    protected = "protected"
    public = "public"


class Defaults(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    agg_time_dimension: Optional[str] = ""


class Format(Enum):
    csv = "csv"
    dict = "dict"
    sql = "sql"


class UnitTestExpectDict(BaseModel):
    format: Literal["dict"] = Field("dict")
    rows: List[Dict[str, Any]] = Field(
        ...,
        description="When `format` is `dict`, each item should be a dictionary containing a key-value pair for each column and its value, e.g. `{id: 1, code: 'ABC'}`",
    )

class UnitTestGivenDict(UnitTestExpectDict):
    model_config = ConfigDict(
        extra="forbid",
    )
    input: str = Field("ref('')", description="The Relation whose input you want to mock")

class UnitTestExpectCSV(BaseModel):
    format: Literal["csv"] = Field("csv")
    rows: Optional[str] = Field(
        "",
        description="When `format` is csv or sql, a string containing comma-separated headers and values. Alternatively specify the `fixture` property. Use the pipe character | to create a multi-line string in YAML.",
    )
    fixture: Optional[str] = Field(
        "",
        description="Specify the name of a fixture instead of providing `rows`. Does not need to be wrapped in ref.",
    )

class UnitTestGivenCSV(UnitTestExpectCSV):
    model_config = ConfigDict(
        extra="forbid",
    )
    input: str = Field("ref('')", description="The Relation whose input you want to mock")


class UnitTestExpectSQL(BaseModel):
    format: Literal["sql"] = Field("sql")
    rows: Optional[str] = Field(
        "",
        description="When `format` is csv or sql, a string containing comma-separated headers and values. Alternatively specify the `fixture` property. Use the pipe character | to create a multi-line string in YAML.",
    )
    fixture: Optional[str] = Field(
        "",
        description="Specify the name of a fixture instead of providing `rows`. Does not need to be wrapped in ref.",
    )

class UnitTestGivenSQL(UnitTestExpectSQL):
    model_config = ConfigDict(
        extra="forbid",
    )
    input: str = Field("ref('')", description="The Relation whose input you want to mock")


Expect = Union[UnitTestExpectDict, UnitTestExpectCSV, UnitTestExpectSQL]
Given = Union[UnitTestGivenDict, UnitTestGivenCSV, UnitTestGivenSQL]


class Overrides(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    env_vars: Optional[Dict[str, Any]] = {"ENV_VAR_NAME": "value"}
    macros: Optional[Dict[str, Any]] = Field(
        None, examples=[{"is_incremental": "true"}]
    )
    vars: Optional[Dict[str, Any]] = {"var_name": "value"}


class AggregationTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    percentile: Optional[float] = ""
    use_approximate_percentile: Optional[bool] = ""
    use_discrete_percentile: Optional[bool] = ""


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
    entity: Optional[str] = ""
    expr: Optional[str] = Field("", description="The field that denotes the entity. Defaults to name if unspecified")


class ExportAs(Enum):
    table = "table"
    view = "view"
    cache = "cache"


class ExportConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    alias: Optional[str] = ""
    export_as: Optional[ExportAs] = ""
    schema_: Optional[str] = Field("", alias="schema")


class Export(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    config: Optional[ExportConfig] = Field(title="Export Config")


class Period(Enum):
    minute = "minute"
    hour = "hour"
    day = "day"


class GroupName(RootModel[str]):
    root: str


class JinjaString(RootModel[str]):
    root: str = Field(..., pattern="\\{\\{.+\\}\\}")


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
    name: Optional[str] = ""
    fill_nulls_with: Optional[Union[str, int]] = 0
    filter: Optional[str] = ""
    join_to_timespine: Optional[bool] = Field(True, description="Indicates if the aggregated measure should be joined to the time spine table to fill in missing dates")


class MetricInputSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Optional[str] = ""
    alias: Optional[str] = ""
    filter: Optional[str] = ""
    offset_window: Optional[str] = ""


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
    name: str = Field("", description="The name of the time dimension (that has already been defined in the data source) that the measure should not be aggregated over.")
    window_choice: WindowChoice = Field(WindowChoice.min, description="`min` and `max` reflect the beginning and end of the time period respectively.")
    window_groupings: Optional[List[str]] = Field([], description="Provide the entities that you would like to group by.")


class NumberOrJinjaString(RootModel[Union[JinjaString, float]]):
    root: Union[JinjaString, float]


class RatioMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    denominator: Optional[MetricInputSchema] = ""
    filter: Optional[str] = ""
    numerator: Optional[MetricInputSchema] = ""


class SimpleMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    measure: Optional[MetricInputMeasure] = ""


class StringOrArrayOfStrings(RootModel[Union[str, ArrayOfStrings]]):
    root: Union[str, ArrayOfStrings]


class Severity(Enum):
    warn = "warn"
    error = "error"


class ValidityParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_end: Optional[bool] = ""
    is_start: Optional[bool] = ""


class Config(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tags: Optional[StringOrArrayOfStrings] = ""


class Analysis(BaseModel):
    name: str
    description: Optional[str] = ""
    columns: Optional[List[Column]] = ""
    config: Optional[Config] = ""
    docs: Optional[DocsConfig] = ""
    group: Optional[GroupName] = ""


class Exposure(BaseModel):
    name: str
    description: Optional[str] = ""
    type: Type
    depends_on: List[str]
    label: Optional[str] = ""
    maturity: Optional[Maturity] = Maturity.medium
    meta: Optional[Dict[str, Any]] = ""
    owner: Owner
    tags: Optional[StringOrArrayOfStrings] = ""
    url: Optional[str] = ""


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
    description: Optional[str] = ""
    arguments: Optional[List[Argument]] = ""
    docs: Optional[DocsConfig] = ""


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
    description: Optional[str] = ""
    filter: Optional[str] = ""
    group: Optional[GroupName] = ""
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
    dimensions: Optional[ArrayOfStrings] = ""
    metrics: Optional[ArrayOfStrings] = ""
    where: Optional[ArrayOfStrings] = ""


class SavedQuery(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: str
    exports: Optional[List[Export]] = ""
    label: str
    query_params: QueryParams


class UnitTestConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    meta: Optional[Dict[str, Any]] = ""
    tags: Optional[StringOrArrayOfStrings] = ""


class UnitTest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = ""
    config: Optional[UnitTestConfig] = Field(None, title="Unit Test Config")
    expect: Expect
    given: Optional[List[Given]] = [UnitTestGivenDict(input="", rows=[{"col1": "value1", "col2": "value2"}])]
    model: str = Field(
        ...,
        description="The name of the model whose behaviour you are testing. Does not need to be wrapped in a ref.",
        examples=["my_model"],
    )
    overrides: Optional[Overrides] = ""


class BooleanOrJinjaString(RootModel[Union[JinjaString, bool]]):
    root: Union[JinjaString, bool]


class Constraint(BaseModel):
    name: Optional[str] = ""
    type: str
    columns: Optional[StringOrArrayOfStrings] = ""
    expression: Optional[str] = ""
    warn_unenforced: Optional[BooleanOrJinjaString] = ""
    warn_unsupported: Optional[BooleanOrJinjaString] = ""


class Constraints(RootModel[List[Constraint]]):
    root: List[Constraint]


class ConversionTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    base_measure: MetricInputMeasure
    calculation: Optional[Calculation] = Calculation.conversion_rate
    constant_properties: Optional[List[ConstantProperty]] = ""
    conversion_measure: MetricInputMeasure
    entity: str = Field(..., description="The entity to calculate over")
    window: Optional[str] = ""


class ConversionMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    conversion_type_params: Optional[ConversionTypeParams] = ""


class CumulativeMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    grain_to_date: Optional[GrainToDate] = GrainToDate.month
    measure: Optional[MetricInputMeasure] = ""
    window: Optional[str] = ""


class DerivedMetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expr: Optional[str] = ""
    metrics: Optional[List[MetricInputSchema]] = ""


class DimensionTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    time_granularity: TimeGranularity
    validity_params: Optional[ValidityParams] = ""


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
    exclude: Optional[StringOrArrayOfStrings] = ""
    include: Optional[StringOrArrayOfStrings] = ""


class Measure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        regex_engine="python-re",
    )
    name: str = Field(..., pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$")
    description: Optional[str] = ""
    agg: Agg
    agg_params: Optional[AggregationTypeParams] = ""
    agg_time_dimension: Optional[str] = Field(
        None, pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$"
    )
    create_metric: Optional[bool] = True
    create_metric_display_name: Optional[str] = ""
    expr: Optional[Union[str, int, bool]] = ""
    label: Optional[str] = ""
    non_additive_dimension: Optional[NonAdditiveDimension] = Field(NonAdditiveDimension(), description="Specify dimensions that the measure should not be aggregated over.")


class Contract(BaseModel):
    enforced: Optional[BooleanOrJinjaString] = True


class ModelConfigs(BaseModel):
    auto_refresh: Optional[BooleanOrJinjaString] = True
    backup: Optional[BooleanOrJinjaString] = True
    contract: Optional[Contract] = Field(Contract(enforced=True))
    file_format: Optional[str] = ""
    grant_access_to: Optional[List[AuthorizedView]] = Field(
        None,
        description="Configuration, specific to BigQuery adapter, used to setup authorized views.",
        title="Authorized views",
    )
    grants: Optional[Grants] = {"select": ["reporter_role", "bi_user"]}
    hours_to_expiration: Optional[float] = Field(
        1,
        description="Configuration specific to BigQuery adapter used to set an expiration delay (in hours) to a table.",
    )
    kms_key_name: Optional[str] = Field(
        "",
        description="Configuration of the KMS key name, specific to BigQuery adapter.",
        pattern="projects/[a-zA-Z0-9_-]*/locations/[a-zA-Z0-9_-]*/keyRings/.*/cryptoKeys/.*",
    )
    labels: Optional[Dict[str, str]] = Field(
        {"key": "value"},
        description="Configuration specific to BigQuery adapter used to add labels and tags to tables/views created by dbt.",
        title="Label configs",
    )
    location: Optional[str] = ""
    materialized: Optional[str] = ""
    on_configuration_change: Optional[OnConfigurationChange] = ""
    on_schema_change: Optional[OnSchemaChange] = ""
    snowflake_warehouse: Optional[str] = ""
    sql_header: Optional[str] = ""
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
    enabled: Optional[BooleanOrJinjaString] = False
    error_if: Optional[str] = ""
    fail_calc: Optional[str] = ""
    limit: Optional[float] = 20
    schema_: Optional[str] = Field(
        None, alias="schema", description="Only relevant when `store_failures` is true"
    )
    severity: Optional[Union[JinjaString, Severity]] = Severity.warn
    store_failures: Optional[BooleanOrJinjaString] = True
    tags: Optional[StringOrArrayOfStrings] = ""
    warn_if: Optional[str] = ""


class SnapshotConfig(BaseModel):
    alias: Optional[str] = ""
    check_cols: Optional[StringOrArrayOfStrings] = ""
    enabled: Optional[BooleanOrJinjaString] = False
    grants: Optional[Grants] = {"select": ["reporter_role", "bi_user"]}
    persist_docs: Optional[PersistDocsConfig] = ""
    post_hook: Optional[ArrayOfStrings] = Field("", alias="post-hook")
    pre_hook: Optional[ArrayOfStrings] = Field("", alias="pre-hook")
    quote_columns: Optional[BooleanOrJinjaString] = ""
    strategy: Optional[str] = ""
    tags: Optional[StringOrArrayOfStrings] = ""
    target_database: Optional[str] = ""
    target_schema: Optional[str] = ""
    unique_key: Optional[StringOrArrayOfStrings] = ""
    updated_at: Optional[str] = ""


class Quoting(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[BooleanOrJinjaString] = ""
    identifier: Optional[BooleanOrJinjaString] = ""
    schema_: Optional[BooleanOrJinjaString] = Field("", alias="schema")


class Relationships(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Optional[str] = ""
    config: Optional[TestConfigs] = ""
    field: str = Field(
        ..., description="The foreign key column", title="Relationships: Field"
    )
    to: str = Field(
        ..., examples=["ref('parent_model')", "source('parent_schema', 'parent_table')"]
    )
    where: Optional[str] = ""


class RelationshipsTest(BaseModel):
    relationships: Optional[Relationships] = ""


class AcceptedValues(BaseModel):
    name: Optional[str] = ""
    config: Optional[TestConfigs] = ""
    quote: Optional[bool] = ""
    values: List[str]
    where: Optional[str] = ""


class AcceptedValuesTest(BaseModel):
    accepted_values: Optional[AcceptedValues] = AcceptedValues(values=[])


class NotNull(BaseModel):
    name: Optional[str] = ""
    config: Optional[TestConfigs] = ""
    where: Optional[str] = ""


class NotNullTest(BaseModel):
    not_null: Optional[NotNull] = ""


class Unique(BaseModel):
    name: Optional[str] = ""
    config: Optional[TestConfigs] = ""
    where: Optional[str] = ""


class UniqueTest(BaseModel):
    unique: Optional[Unique] = ""


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
    description: Optional[str] = ""
    expr: Optional[Union[str, bool]] = ""
    is_partition: Optional[bool] = True


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
    column_types: Optional[Dict[str, Any]] = ""
    copy_grants: Optional[BooleanOrJinjaString] = True
    data_tests: Optional[List[DataTests]] = ""
    database: Optional[str] = ""
    enabled: Optional[BooleanOrJinjaString] = False
    grants: Optional[Grants] = {"select": ["reporter_role", "bi_user"]}
    quote_columns: Optional[BooleanOrJinjaString] = ""
    schema_: Optional[str] = Field(None, alias="schema")


class SemanticModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        regex_engine="python-re",
    )
    name: str = Field(..., pattern="(?!.*__).*^[a-z][a-z0-9_]*[a-z0-9]$")
    description: Optional[str] = ""
    defaults: Optional[Defaults] = ""
    dimensions: Optional[List[Dimension]] = ""
    entities: Optional[List[Entity]] = ""
    measures: Optional[List[Measure]] = ""
    model: str
    primary_entity: Optional[str] = ""


class ColumnProperties(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = ""
    constraints: Optional[Constraints] = ""
    data_tests: Optional[List[DataTests]] = ""
    data_type: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = ""
    policy_tags: Optional[List[str]] = Field(
        None,
        description="Configurations, specific to BigQuery adapter, used to set policy tags on specific columns, enabling column-level security. Only relevant when `persist_docs.columns` is true.",
        title="Policy tags",
    )
    quote: Optional[BooleanOrJinjaString] = ""
    tags: Optional[StringOrArrayOfStrings] = ""
    tests: Optional[List[DataTests]] = ""


class Version(BaseModel):
    columns: Optional[List[Union[IncludeExclude, ColumnProperties]]] = {}
    config: Optional[ModelConfigs] = {}
    v: float = 1


class Model(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = ""
    access: Optional[Access] = Access.private
    columns: Optional[List[ColumnProperties]] = ""
    config: Optional[ModelConfigs] = ""
    constraints: Optional[Constraints] = ""
    data_tests: Optional[List[DataTests]] = ""
    deprecation_date: Optional[str] = ""
    docs: Optional[DocsConfig] = ""
    group: Optional[GroupName] = ""
    latest_version: Optional[float] = ""
    meta: Optional[Dict[str, Any]] = ""
    tests: Optional[List[DataTests]] = ""
    versions: Optional[List[Version]] = ""


class Seed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = ""
    columns: Optional[List[ColumnProperties]] = ""
    config: Optional[SeedConfig] = Field("", title="Seed Config")
    docs: Optional[DocsConfig] = ""
    group: Optional[GroupName] = ""
    tests: Optional[List[DataTests]] = ""


class Snapshot(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    description: Optional[str] = ""
    columns: Optional[List[ColumnProperties]] = ""
    config: Optional[SnapshotConfig] = Field("", title="Snapshot Config")
    data_tests: Optional[List[DataTests]] = ""
    docs: Optional[DocsConfig] = ""
    group: Optional[GroupName] = ""
    meta: Optional[Dict[str, Any]] = ""
    tests: Optional[List[DataTests]] = ""


class Table(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str = Field(
        ...,
        description="How you will identify the table in {{ source() }} calls. Unless `identifier` is also set, this will be the name of the table in the database.",
        title="Name",
    )
    description: Optional[str] = ""
    columns: Optional[List[ColumnProperties]] = ""
    external: Optional[Dict[str, Any]] = ""
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
    loader: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = ""
    quoting: Optional[Quoting] = ""
    tags: Optional[StringOrArrayOfStrings] = ""
    tests: Optional[List[DataTests]] = ""


class Source(BaseModel):
    name: str = Field(
        ...,
        description="How you will identify the schema in {{ source() }} calls. Unless `schema` is also set, this will be the name of the schema in the database.",
    )
    description: Optional[str] = ""
    config: Optional[Dict[str, Any]] = ""
    data_tests: Optional[List[DataTests]] = ""
    database: Optional[str] = ""
    freshness: Optional[FreshnessDefinition] = Field(FreshnessDefinition(), json_schema_extra={"$comment": "truly_nullable"})
    loaded_at_field: Optional[str] = ""
    loader: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = ""
    overrides: Optional[str] = Field(
        None,
        description="The name of another package installed in your project. If that package has a source with the same name as this one, its properties will be applied on top of the base properties of the overridden source. https://docs.getdbt.com/reference/resource-properties/overrides",
        title="Package to Override",
    )
    quoting: Optional[Quoting] = ""
    schema_: Optional[str] = Field(
        None,
        alias="schema",
        description="The schema name as stored in the database. Only needed if you want to use a different `name` than what exists in the database (otherwise `name` is used by default)",
    )
    tables: Optional[List[Table]] = ""
    tags: Optional[StringOrArrayOfStrings] = ""
    tests: Optional[List[DataTests]] = ""


class DbtYmlFiles(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    version: Literal[2] = 2
    analyses: Optional[List[Analysis]] = ""
    exposures: Optional[List[Exposure]] = ""
    groups: Optional[List[Group]] = ""
    macros: Optional[List[Macro]] = ""
    metrics: Optional[List[Metric]] = ""
    models: Optional[List[Model]] = ""
    saved_queries: Optional[List[SavedQuery]] = ""
    seeds: Optional[List[Seed]] = ""
    semantic_models: Optional[List[SemanticModel]] = ""
    snapshots: Optional[List[Snapshot]] = ""
    sources: Optional[List[Source]] = ""
    unit_tests: Optional[List[UnitTest]] = ""