from setuptools import setup, find_packages


setup(name='aiomysql',
      version="0.0.22",
      description=('MySQL driver for asyncio.'),
      platforms=['POSIX'],
      author="Nikolay Novik",
      author_email="nickolainovik@gmail.com",
      url='https://github.com/aio-libs/aiomysql',
      download_url='https://pypi.python.org/pypi/aiomysql',
      license='MIT',
      packages=find_packages(),
      include_package_data=True)
