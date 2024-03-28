import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CustomNet",
    version="0.0.1",
    author="Tirthankar Chakraborty",
    author_email="tirthankar06chakraborty@gmail.com",
    description=" A custom ANN implementation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)