from setuptools import find_packages, setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='linearalgcalc',
    packages=find_packages(include=['linearalgcalc']),
    version='0.1.1',
    description='A library for linear algebra calculations',
    long_description = long_description,
    long_description_content_type="text/markdown",
    author='Jinha Kim',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)