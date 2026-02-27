from setuptools import setup, find_packages

setup(
    name='flask-app-skeleton',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask>=2.3.0',
        'flask-cors>=4.0.0',
        'sqlalchemy>=2.0.0',
        'pyyaml>=6.0.1',
        'python-dotenv>=1.0.0',
    ],
)
