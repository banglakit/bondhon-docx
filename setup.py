from distutils.core import setup

setup(name='Bondhon DOCX',
      version='1.0',
      description='Encoding conversion library for the Bengali (বাংলা) script.',
      author='The BanglaKit Project',
      author_email='remember@banglakit.com',
      url='https://github.com/banglakit/bondhon_docx-docx',
      packages=['bondhon_docx'],
      install_requires=['python-docx'],
      scripts=['bin/convert-bangla'],
      )
