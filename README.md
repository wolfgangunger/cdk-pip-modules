
# cdk pip packages
  
this project shows how to package cdk constructs as pip modules and import and use them in our projects  
  
## install required tools  
pip install setuptools  
pip install twine  
pip install wheel  
  
## .pypirc
you must have a file named .pypirc in your user folder   
content must be some like this :   

[distutils]   
index-servers=pypi  
  
[pypi]   
repository = https://upload.pypi.org/legacy/   
username=change2yourusername  
password=change2yourpassword  
    
  
## project structure  
cdk_pip_modules  
├── LICENSE    
├── wunger_cdk_constructs ( folder with the constructs, content will be packaged as pip module)   
│   ├── __init__.py    
│   ├── cdk classes    
│   ├── ...  
├── stacks (wrapper stacks to test the constructs before creating the pip module)   
├── usage ( stacks that will import and use the final pip modules)  
├── README.md    
├── app.py ( main python file, entry point )    
└── setup.py    

-please create your constructs in the folder wunger_cdk_constructs or your own folder ( my_cdk_constructs)  
-adapt setup.py   
-adapt the app.py   
-build the module and install locally  
-upload to remote repo  
-use the module by cdk stacks in usage folder, see example  
  

## check
python setup.py check
## create package
python setup.py bdist_wheel


python -m pip install dist/wunger_cdk-0.0.2-py3-none-any.whl
install same version new
python -m pip install dist/wunger_cdk-0.0.2-py3-none-any.whl --force


## upload

twine upload -r pypi dist/wunger_cdk-0.0.2-py3-none-any.whl

## use in client project
setup requirements.txt: 
wunger-cdk==0.0.1

pip install -r requirements.txt 
or explicit :
pip install wunger-cdk

import class:
from wunger_cdk.ecr_repo import WUngerEcrConstruct



https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/

https://packaging.python.org/

https://dzone.com/articles/executable-package-pip-install






