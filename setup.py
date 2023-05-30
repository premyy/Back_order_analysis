from setuptools import setup, find_packages


#now i'm creatting a function for taking the package from requirements.txt
extention='-e .'
def get_requirement(filename:str)->list[str]:
    #this function returns the package list
    requirement=[]
    with open(filename) as file_obj:
        requirement=file_obj.readlines()
        requirement=[i.replace('\n', '') for i in requirement]


        if extention in requirement:
            requirement.remove(extention)

        
    return requirement



setup(
    name='backorder_analysis',
    version='0.0.1',
    author='Bhoori Singh',
    author_email='Bhoorisingh955716@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)