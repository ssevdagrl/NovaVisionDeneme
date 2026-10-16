
from setuptools import setup, find_packages

setup(
    name="DetectionCounter",
    version="0.1.0",
    author="Sevda",
    description="YOLO object detection counting package for NovaVision",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "pydantic"
    ],
)
