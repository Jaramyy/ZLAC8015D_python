# from setuptools import setup

# setup(
#     name = "zlac8015d",
#     version = "0.0.1",
#     author = "Rasheed Kittinanthapanya",
#     author_email = "rasheedo.kit@gmail.com",
#     url='https://github.com/rasheeddo/ZLAC8015D_python', 
#     license='GPLv3',
#     packages=['zlac8015d',],
#     install_requires = [
#         'pymodbus',
#         'numpy'
#     ]
# )

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['zlac8015d'],
    package_dir={'': 'src'}
    # install_requires = [
    #     'pymodbus',
    #     'numpy'
    # ]
)
setup(**d)