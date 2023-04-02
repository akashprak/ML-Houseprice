from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def getRequirements(file_path:str) -> List[str]:
    
    with open(file_path) as f:
        requirements = f.readlines()
        requirements= [i.replace("\n","") for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='Akash',
    install_requires = getRequirements('requirements.txt'),
    packages=find_packages()
)