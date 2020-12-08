import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

long_description = "something or other"

setuptools.setup(
    name="fooinc",
    version="0.0.1",
    author="Brendan Cox",
    author_email="brendan.cox@vertexone.net",
    description="A sample backend application for packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justnoise/foo_inc",
    # packages=setuptools.find_packages(),
    packages=setuptools.find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
