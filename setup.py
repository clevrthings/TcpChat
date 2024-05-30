from setuptools import setup, find_packages

setup(
    name="ct-tcpchat",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Clevrthings",
    author_email="info@clevrthings.com",
    description="A simple Python module for creating a TCP chat connection between two computers to send commands or information.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/clevrthings/TcpChat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
