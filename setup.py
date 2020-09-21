#from setuptools import setup
import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()
#packages=setuptools.find_packages(),
setuptools.setup(
      name="paquete_suma_resta",
      version="1.0.0",
      description="ejemplo de setup inicial",
      author="mp",
      author_email="mp@mp.com.ar",
      url="www.sarasa.com.ar",
      packages=["libreria","libreria.libresta"],
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
      ]

)