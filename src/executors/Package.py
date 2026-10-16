
import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), "../../../../")
)

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from sdks.novavision.src.helper.package import PackageHelper

from components.DetectionCounter.src.models.PackageModel import (
    PackageModel,
    DetectionCounterConfigs,
    DetectionCounterOutputs,
    DetectionCounterResponse,
    CounterExecutor,
    CounterConfigExecutor,
    OutputTotalCount,
)

from components.DetectionCounter.src.utils.counting import (
    count_detections,
)


class DetectionCounter(Component):

    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)

        self.request.model = PackageModel(
            **self.request.data
        )

        self.detections = self.request.get_param(
            "inputDetections"
        )

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):

        results = count_detections(self.detections)

        total_count = results["total"]

        output = OutputTotalCount(
            value=total_count
        )

        outputs = DetectionCounterOutputs(
            outputTotalCount=output
        )

        response = DetectionCounterResponse(
            outputs=outputs
        )

        executor_result = CounterExecutor(
            value=response
        )

        executor_config = CounterConfigExecutor(
            value=executor_result
        )

        package_configs = DetectionCounterConfigs(
            executor=executor_config
        )

        package = PackageHelper(
            packageModel=PackageModel,
            packageConfigs=package_configs
        )

        return package.build_model(self)


if __name__ == "__main__":
    Executor(sys.argv[1]).run()
