from setuptools import setup, find_packages

setup(name='anonymization',
    version='0.1',
    description='Text anonymization using Faker',
    url='https://github.com/gillesdami/anonymization',
    author='Damien Gilles',
    author_email='damien.gilles.pro@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'Faker>=1,<2'
    ],
    extras_require = {
        'spacyAnonymizers':  ['spacy>=2,<3']
    })