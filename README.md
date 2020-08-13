Introduction to Machine Learning with Scikit-learn
========================================================


This repository will contain the teaching material and other info associated
with the "Introduction to Machine Learning with scikit-learn" course.

Content
-------
- [Review of basic Machine Learning concepts](https://amueller.github.io/sklearn-one-day/slides/01-introduction.html)
- [Data loading and basic API of scikit-learn](https://amueller.github.io/sklearn-one-day/slides/02-supervised-learning.html)
- [Fundamentals of Data Preprocessing: scaling and categorical data](https://amueller.github.io/sklearn-one-day/slides/03-preprocessing.html)
- [Grid search and cross-validation](https://amueller.github.io/sklearn-one-day/slides/04-cross-validation-grid-search.html)
- [Building workflows with Pipelines](https://amueller.github.io/sklearn-one-day/slides/05-pipelines.html)
- [Evaluation metrics for classification](https://amueller.github.io/sklearn-one-day/slides/06-model-evaluation.html)
- [if time permits: Trees and Random Forests](https://amueller.github.io/sklearn-one-day/slides/bonus-07-trees-and-forests.html)
- [if time permits: Gradient Boosting in-depth](https://amueller.github.io/sklearn-one-day/slides/bonus-08-gradient-boosting.html)

About the workshop
------------------
Machine learning has become an indispensable tool across many areas of research
and commercial applications. From text-to-speech for your phone to detecting
the Higgs boson, machine learning excels at extracting knowledge from large
amounts of data. This workshop will talk through the machine learning process
with the popular Python library scikit-learn.
We will focus on the machine learning workflow and best practices for machine learning with scikit-learn.

Prerequisites
-------------
This workshop assumes familiarity with Jupyter notebooks and basics of pandas, matplotlib and numpy.


Obtaining the Tutorial Material
--------------------------------


If you are familiar with git, it is most convenient if you clone the GitHub repository. This
is highly encouraged as it allows you to easily synchronize any changes to the material.

```
git clone https://github.com/amueller/sklearn-one-day.git
```

If you are not familiar with git, you can download the repository as a .zip file by heading over to the GitHub repository (https://github.com/amueller/sklearn-one-day) in your browser and click the green “Download” button in the upper right.

![](images/download-repo.png)

Please note that I may add and improve the material until shortly before the
tutorial session, and we recommend you to update your copy of the materials one
day before the tutorials. If you have an GitHub account and forked/cloned the
repository via GitHub, you can sync your existing fork with via the following
commands:

```
git pull origin master
```


Installation Notes
------------------

This tutorial will require recent installations of

- [NumPy](http://www.numpy.org)
- [SciPy](http://www.scipy.org)
- [matplotlib](http://matplotlib.org)
- [pillow](https://python-pillow.org)
- [pandas](http://pandas.pydata.org)
- [scikit-learn](http://scikit-learn.org/stable/) (>=0.22.1)
- [IPython](http://ipython.readthedocs.org/en/stable/)
- [Jupyter Notebook](http://jupyter.org)

The last one is important, you should be able to type:

    jupyter notebook

in your terminal window and see the notebook panel load in your web browser.
Try opening and running a notebook from the material to see check that it works.

For users who do not yet have these  packages installed, a relatively
painless way to install all the requirements is to use a Python distribution
such as [Anaconda](https://www.continuum.io/downloads), which includes
the most relevant Python packages for science, math, engineering, and
data analysis; Anaconda can be downloaded and installed for free
including commercial use and redistribution.
The code examples in this tutorial requires Python 3.5 or later.

After obtaining the material, we **strongly recommend** you to open and execute
a Jupyter Notebook `jupter notebook check_env.ipynb` that is located at the
top level of this repository. Inside the repository, you can open the notebook
by executing

```bash
jupyter notebook check_env.ipynb
```

inside this repository. Inside the Notebook, you can run the code cell by
clicking on the "Run Cells" button as illustrated in the figure below:

![](images/check_env-1.png)


Finally, if your environment satisfies the requirements for the tutorials, the executed code cell will produce an output message as shown below:

![](images/check_env-2.png)
