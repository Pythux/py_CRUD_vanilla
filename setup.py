from setuptools import setup

setup(
    name='CRUD_vanilla',
    version='1.0',
    description='database tools to link models to data_access',
    author='Pythux',
    # author_email='',
    packages=[
        'CRUD_vanilla',
        'CRUD_vanilla.connection',
    ],  # same as name
    # install_requires=[],  # external packages as dependencies
)
