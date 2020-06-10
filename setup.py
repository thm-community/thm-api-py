import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thmapi",
    version="0.8.0",
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
    python_requires='>=3.8',
    install_requires=[
        "requests",
        "chardet>=3.0.2,<4",
        "idna>=2.5,<3",
        "urllib3>=1.21.1,<1.26,!=1.25.0,!=1.25.1",
        "certifi>=2017.4.17"
    ],
)
