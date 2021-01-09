import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdriq2complex", # Replace with your own username
    version="0.0.1",
    author="Eugene Mikhantiev",
    author_email="mikhantiev@gmail.com",
    description="SDRangel *.srdiq data conversion tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mehanik/sdriq2complex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/sdriq2complex'],
    install_requires = [
        'numpy',
    ]
)
