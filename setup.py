import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="preconfig-nedelec", # Replace with your own username
    version="1.0",
    author="Francois Nedelec",
    author_email="francois.nedelec@slcu.cam.ac.uk",
    description="A versatile configuration file generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nedelec/preconfig",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)