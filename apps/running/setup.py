from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in running/__init__.py
from running import __version__ as version

setup(
	name="running",
	version=version,
	description="Warehouse Runner Application",
	author="PackJC",
	author_email="johnnypack@classiccookie.local",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
