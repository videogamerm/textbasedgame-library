import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text-based-game-videogamerm",
    version="0.0.1",
    author="Mason Withers",
    author_email="thchessminecraft@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/videogamerm/textbasedgame-library",
    project_urls={
        "Bug Tracker": "https://github.com/videogamerm/textbasedgame-library/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)