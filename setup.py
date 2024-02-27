from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.1",
    author="rajesh",
    author_email="rajesh.koredla25@gmail.com",
    description="A Python package for US visa-related tasks",
    url="https://github.com/rajeshkoredla/USVisaApprovalPrediction",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
