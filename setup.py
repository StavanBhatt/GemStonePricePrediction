from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements_txt(file_path: str) -> List[str]:
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name='RegressionProject',
    version='0.0.1',
    author='Stavan Bhatt',
    author_email='bhattstavan20@gmail.com',
    # install_requires=[i.strip() for i in open('requirements.txt').readlines() if i.strip() not in ['-e .', '']],
    install_requires=get_requirements_txt('requirements.txt'),
    packages=find_packages()
)