"""Setup script for aws-pricing-calculator-mcp."""

from setuptools import setup, find_packages

setup(
    packages=find_packages(include=["mcp_server", "mcp_server.*", "scripts", "scripts.*"]),
    package_data={
        "mcp_server": ["py.typed"],
    },
)
