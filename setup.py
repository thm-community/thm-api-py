import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thmapi",
    version="0.0.1",
    author="Szymon Borecki",
    author_email="self@szymex.pw",
    description="THM public API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/szymex73/py-thmapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Internet :: WWW/HTTP"
    ],
    python_requires='>=3.6',
)
