from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ResultDAO(object):
    data: dict
    # job_id: str
    # hasblock_CAT: bool
    # hasblock_NUM: bool
    # hasblock_TEXT: bool
    # CategoryEncoder: str
    # CategoryEncoder_params: dict
    # DimensionReduction: str
    # DimensionReduction_params: dict
    # FeatureSelection: str
    # FeatureSelection_params: dict
    # MissingValueImputer: str
    # MissingValueImputer_params: dict
    # Model: str
    # Model_params: dict
    # Scaling: str
    # Scaling_params: dict
    # TextDimensionReduction: str
    # TextDimensionReduction_params: dict
    # TextEncoder: str
    # TextEncoder_params: dict
    # TextPreprocessing: str
    # test_metrics: dict
    # train_metrics: dict
    # global_metrics: dict


@dataclass_json
@dataclass
class Response(object):
    results: dict

