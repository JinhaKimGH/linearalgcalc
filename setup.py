from setuptools import find_packages, setup
setup(
    name='linearalgcalc',
    packages=find_packages(include=['linearalgcalc']),
    version='0.1.0',
    description='A library for linear algebra calculations',
    author='Jinha Kim',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)