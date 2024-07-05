"""
Project Setup and Initiator.
"""

from setuptools import setup, find_packages

setup(
    name="vertex_trading_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "vertex-protocol",
        "pandas",
        "numpy",
        "scikit-learn",
    ],
)