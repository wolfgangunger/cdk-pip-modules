import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="wunger-cdk",
    version="0.0.2",
    author="Wolfgang Unger",
    author_email="wolfgang.unger@sccbrasil.com",
    description="CDK python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://upload.pypi.org/legacy/",
    packages=["wunger_cdk_constructs"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
