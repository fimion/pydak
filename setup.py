from setuptools import setup

setup(
    name='pydak',
    version='0.2',
    packages=['daktronics'],
    install_requires=['pyserial'],
    url='https://github.com/fimion/pydak',
    license='MIT',
    author='Alex Riviere',
    author_email='fimion@gmail.com',
    description='Python Library for Daktronics AllSport 5000 Scoring Controllers'
)
