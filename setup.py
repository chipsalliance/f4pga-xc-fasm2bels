import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fasm2bels",
    version="0.0.1",
    author="SymbiFlow Authors",
    author_email="symbiflow@lists.librecores.org",
    description="fasm2bels libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SymbiFlow/symbiflow-xc-fasm2bels",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "simplejson",
        "pycapnp",
        "intervaltree",
        "parameterized",
        "progressbar2",
        "lxml",
        "prjxray@git+git://github.com/SymbiFlow/prjxray.git#egg=prjxray",
        "fasm@git+git://github.com/SymbiFlow/fasm.git#egg=fasm",
        "rr-graph@git+git://github.com/SymbiFlow/symbiflow-rr-graph.git@fix-for-python-packaging#egg=symbiflow-rr-graph",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)
