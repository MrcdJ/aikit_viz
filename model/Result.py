from dataclasses import dataclass


@dataclass
class Result(object):
    data: dict

    # job_id: str
    # hasblock_CAT: bool
    # hasblock_NUM: bool
    # hasblock_TEXT: bool
    #
    # data: dict
    #
    # # CategoryEncoder: str
    # # CategoryEncoder_params: dict
    # # DimensionReduction: str
    # # DimensionReduction_params: dict
    # # FeatureSelection: str
    # # FeatureSelection_params: dict
    # # MissingValueImputer: str
    # # MissingValueImputer_params: dict
    # # Model: str
    # # Model_params: dict
    # # Scaling: str
    # # Scaling_params: dict
    # # TextDimensionReduction: str
    # # TextDimensionReduction_params: dict
    # # TextEncoder: str
    # # TextEncoder_params: dict
    # # TextPreprocessing: str
    # #
    # # other_params: dict
    #
    # test_metrics: dict
    # train_metrics: dict
    # valid_metrics: dict


@dataclass
class Results(object):
    results: dict

