from setuptools import find_packages, setup

def get_requirements(file):
    with open(file,"r") as f:
        package_list = f.readlines()
        package_list = [package.replace("\n","") for package in package_list]
        if "-e ." in package_list:
            package_list.remove("-e .")
        return package_list

setup(name = "MLProject",
      version = "0.0.1",
      author="Kalyan",
      packages=find_packages(),
      install_requirements = get_requirements("requirements.txt"))
      
      
      