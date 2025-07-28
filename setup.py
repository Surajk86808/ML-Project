from setuptools import setup, find_packages
from typing import List 

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list[str]:
    '''
    This function returns a list of requirements from a given file path.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPEN_E_DOT]
    return requirements        
        
setup(
    name='ML-Project',
    version='0.0.1',
    author='Suraj',
    author_email='surajk86808@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
) 