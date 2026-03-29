from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    
    # FIXED: Replaced semicolon with a colon
    with open(file_path) as file_obj:
        # FIXED: Changed readline() to readlines()
        requirements = file_obj.readlines()
        
        # FIXED: Replaced newline with an empty string "", not a space " "
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kinshuk',
    author_email='ver.kinshuk111@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)