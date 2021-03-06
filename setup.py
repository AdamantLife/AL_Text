import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AL_Text",
    version="1.0.0",
    author="AdamantLife",
    author_email="",
    description="A collection of code snippets involving Text and Text Output; pared from alcustoms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamantLife/AL_Text",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        ]
)
