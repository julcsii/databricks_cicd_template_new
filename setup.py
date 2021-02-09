from setuptools import find_packages, setup
from cicd_template_new import __version__

setup(
    name='cicd_template_new',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='Test',
    author='Julia Hermann'
)
