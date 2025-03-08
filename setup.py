from setuptools import setup, find_packages

setup(
    name="continuous_distributions",
    version="0.1.0",
    description="A library for visualizing continuous probability distributions",
    author="Rocco Angelella",
    author_email="rocco.angelellafx@gmail.com",
    url="https://github.com/roccoangelella/Probability-Distributions",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3..6",
)
