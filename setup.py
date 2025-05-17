from setuptools import setup

setup(
    name="projforge",
    version="1.0.0",
    py_modules=["projforge"],
    install_requires=[
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "projforge = projforge:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to scaffold modular Python project folders.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/projforge",  # Update if published
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

