from setuptools import setup, find_packages

# import readme
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='anonymization',
    version='0.1.3',
    description='Text anonymization using Faker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alterway/anonymization',
    author='Alter Way R&D',
    author_email='rnd@alterway.fr',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'Faker>=1,<2'
    ],
    extras_require = {
        'spacyAnonymizers':  ['spacy>=2,<3']
    })