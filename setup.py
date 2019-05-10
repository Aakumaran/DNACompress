rom setuptools import setup 
  
# reading long description from file 
with open('DESCRIPTION.txt') as file: 
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = ['numpy','bitarray','keras','scikit','tensorflow'] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: Beta', 
    'Intended Audience :: Developers', 
    'Topic :: BioInformatics', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    ] 
  
# calling the setup function  
setup(name='DNACompress', 
      version='1.0.0', 
      description='FASTA file compression', 
      long_description=long_description, 
      url='https://github.com/ramrathi/DNACompress', 
      author='Ram Rathi', 
      author_email='ryrathi@gmail.com', 
      license='MIT', 
      packages=[], 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='fasta compression dna bioinformatics'
      ) 
