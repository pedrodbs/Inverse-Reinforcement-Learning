from setuptools import setup, find_packages

setup(name='irl-ow',
      version='1.0',
      description='MDP Environments for Inverse Reinforcement Learning',
      author='Matthew Alger',
      maintainer='Pedro Sequeira',
      maintainer_email='pedrodbs@gmail.com',
      url='https://github.com/pedrodbs/Inverse-Reinforcement-Learning',
      packages=find_packages(),
      scripts=[
      ],
      install_requires=[
          'numpy'
      ],
      zip_safe=True
      )
