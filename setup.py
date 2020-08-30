import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='project_graph',
     version='0.1.7',
     author="Felix Plagge",
     scripts=['project_graph/project_graph'],
     author_email="felix.plagge@gmail.com",
     description="Provides visual performance overview of scripts",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/fior-di-latte/performance_graph",
     packages=['project_graph'],
     install_requires=['gprof2dot', 'path'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Unix based OS",
     ],
 )
