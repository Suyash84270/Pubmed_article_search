
from setuptools import setup, find_packages

setup(
    name="pubmed_module_saikat_sinha_25",  # Replace with your module's name
    version="0.1.0",
    packages=find_packages(),  # Automatically discover packages in the directory
    install_requires=[
        "biopython>=1.79",
        "pandas>=1.3.0"
    ],
    author="Your Name",
    author_email="saikatsinha21@gmail.com",
    description="PubMed article search and analysis toolkit",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Saikatsinha007/PubMed-Article-Search.git",  # Replace with your project's URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your chosen license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
