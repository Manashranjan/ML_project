from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str)->List[str]: # this functions will return a list
    '''
    This function will return the list of requirements
    '''
    HYPEN_E_DOT="-e ."
    requiremetns = []
    with open(file_path) as file_obj:
        requiremetns=file_obj.readlines()
        requiremetns=[req.replace("\n", "") for req in requiremetns]

        if HYPEN_E_DOT in requiremetns:
            requiremetns.remove(HYPEN_E_DOT)

    return requiremetns
setup(
    name='MLproject',
    version='0.0.1',
    author='Manash',
    author_email='manashn381@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)