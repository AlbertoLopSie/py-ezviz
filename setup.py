import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py-ezviz',
    version="0.1.6.8",
    license='GPL-3.0 License',
    author='Renier Moorcroft',
    author_email='RenierM26@users.github.com',
    description='Pilot your Ezviz cameras',
    long_description="This package is based on pyEzviz, written by BaQs. Pilot your Ezviz cameras with this module. Please view readme on github",
    url='https://github.com/RenierM26/py-Ezviz',
    packages=setuptools.find_packages(),
    setup_requires=[
        'requests',
        'setuptools'
    ],
    install_requires=[
        'requests',
        'pandas'
    ],
    entry_points={
    'console_scripts': ['pyezviz = pyezviz.__main__:main']
    },
    python_requires = '>=3.6'
)
