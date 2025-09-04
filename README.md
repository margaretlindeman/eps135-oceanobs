## EPS/ESE 135
### Observing the Ocean: Measurements and Instrumentation
#### Fall 2025

Materials and code for EPS/ESE 135 data visualization & analysis assignments will be available in this Github repository. The course syllabus and other information can be found on the Canvas page. This page includes some tips for setting up Python and some helpful resources &mdash; if you have different suggestions, or if there are other resources that you find especially helpful, please share them with me and I'll update this page!


#### Setting up Python
If you don't already have Python set up on your machine, I recommend installing the [Anaconda Distribution](www.anaconda.com/download/success). Python is open-source and modular, which means that there are nearly limitless libraries with potentially useful functions that you may wish to explore, but the Anaconda distribution includes most of the most-commonly used packages. (You can also install Miniconda from the same link, which is a smaller download but will require you to download other packages later.) The Anaconda Navigator itself is basically an app that allows you to edit your Python environment via a GUI/graphical user interface and launch various Python applications, including [Jupyter Lab](https://jupyter.org/). We will be using Jupyter Notebooks for coding assignments in this course because they are interactive and also lend themselves to good documentation, which is a key part of data analysis and visualization.

It's good practice to maintain separate Python environments for different projects, which may require different versions of certain libraries or various packages with incompatible dependencies. You can create an environment that includes the packages needed for these assignments from the `environment.yaml` file in this repo by [following the steps here](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) or using the _Import_ button under the _Environments_ tab in Anaconda Navigator.


#### Getting started with Python
If you are new to Python, I strongly recommend this thorough primer from [Project Pythia](https://foundations.projectpythia.org/preamble/how-to-use/), which covers the foundational skills and key Python packages that you are likely to use in earth science data analysis. It's great either to work through systematically or to use as a reference as needed. They also offer more advanced, specialized [cookbooks](https://cookbooks.projectpythia.org/) for certain applications.

#### Python resources
There are many other excellent Python resources around the internet that you may find useful, including:
- [Software Carpentry](https://swcarpentry.github.io/python-novice-inflammation/01-intro.html), which will introduce you to basic coding principles and Python syntax. If you have not done much or any coding previously, this is a nice first stop. (In addition to programming in Python, they have [open-source materials](https://software-carpentry.org/lessons/) on how to use the Unix shell/Terminal and version control with Git, all of which I'd recommend if you're interested in developing those skills further!)
- [ClimateMatch Academy](https://comptools.climatematch.io/tutorials/intro.html), which is an open-source climate-focused data science course with videos and hands-on data examples. These can be worked through in order as a structured course, or you can identify modules that cover methods you're interested in applying to your own work.
- [Jupyter notebook tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- If you have previously worked in Matlab, you may find this [cheat sheat](https://cheatsheets.quantecon.org/) helpful. It provides Python "translations" for some basic Matlab operations and syntaxes. (A key point not covered here: Matlab indexing starts at 1 and Python indexing starts at 0!)

Generative AI chatbots can save you a lot of time with certain types of coding tasks, but the code they generate can contain errors. It's important to develop some basic understanding of how Python works so that you can identify issues and debug code that you get from outside sources.
