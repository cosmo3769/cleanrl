from setuptools import setup, find_packages

setup(name='cleanrl',
      version='0.1.0',
      install_requires=['gym', 'stable_baselines', 'tensorboardX'],
      packages=find_packages()
)