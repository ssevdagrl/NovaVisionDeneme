
from typing import List, Literal
from pydantic import Field

from sdks.novavision.src.base.model import (
    Package,
    Input,
    Output,
    Inputs,
    Outputs,
    Request,
    Response,
    Config,
    Configs,
    Detection
)


class InputDetections(Input):
    name: Literal["inputDetections"] = "inputDetections"
    value: List[Detection]
    type: Literal["list"] = "list"

    class Config:
        title = "YOLO Detections"


class OutputTotalCount(Output):
    name: Literal["outputTotalCount"] = "outputTotalCount"
    value: int = Field(ge=0)
    type: Literal["number"] = "number"

    class Config:
        title = "Total Object Count"


class DetectionCounterInputs(Inputs):
    inputDetections: InputDetections


class DetectionCounterOutputs(Outputs):
    outputTotalCount: OutputTotalCount


class DetectionCounterRequest(Request):
    inputs: DetectionCounterInputs


class DetectionCounterResponse(Response):
    outputs: DetectionCounterOutputs


class CounterExecutor(Config):
    name: Literal["DetectionCounter"] = "DetectionCounter"
    value: DetectionCounterRequest | DetectionCounterResponse
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class CounterConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: CounterExecutor
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"


class DetectionCounterConfigs(Configs):
    executor: CounterConfigExecutor


class PackageModel(Package):
    configs: DetectionCounterConfigs
    type: Literal["component"] = "component"
    name: Literal["DetectionCounter"] = "DetectionCounter"

    class Config:
        title = "Detection Counter"
