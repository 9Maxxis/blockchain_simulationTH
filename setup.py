import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'blockchain_simulationTH',      
  packages = ['blockchain_simulationTH'], 
  version = '0.0.3',  
  license='MIT', 
  description = '(BlockchainTH) Blockchain Simulation by 9Maxxis',
  long_description=DESCRIPTION,
  author = '9Maxxis',                 
  author_email = '',     
  url = 'https://github.com/9Maxxis/blockchain_simulationTH',  
  download_url = 'https://github.com/9Maxxis/blockchain_simulationTH/archive/refs/tags/v0.0.3.zip',  
  keywords = ['blockchain', 'blockchain simulation', '9Maxxis'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
  ],
)