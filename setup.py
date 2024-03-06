from setuptools import setup, find_packages

setup(
    name="py_fao",
    version="0.1.0",
    author="bokushi4",
    author_email="t.hayasaka@cartahd.com",
    description="A simple math library for basic arithmetic operations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
