# Python Programming Lectures Notes

This repository contains a curated set of iPython Notebooks of 
introductory materials about programming in Python.

Some (*most*, so far) of these notebooks have been borrowed by the
material provided in the [Introduction to Programming](http://www.introtopython.org) 
course by [Eric Matthes](mailto:ehmatthes@gmail.com)

You can view the `HTML` version of the Notebooks using the **iPython Notebook Viewer** service:
([index page](http://nbviewer.ipython.org/urls/raw.github.com/leriomaggio/python-programming-lectures/master/notebooks/Index.ipynb), 
[course syllabus](http://nbviewer.ipython.org/urls/raw.github.com/leriomaggio/python-programming-lectures/master/notebooks/TOC.ipynb)). 

## Goals ##

Available notebooks are intended to aid both students and teachers in learning and teaching 
Python programming, respectively. 

In more details, the goals of this project are:

- Introduce students as quickly as possible to the basics of Python programming;
- Introduce best practice as early as possible, while remaining accessible to students with no background in programming at all;
- Provide teachers an easy-to-use material about programming in Python to be used in their lectures
  (please see the Section [Teaching Material](#slides) for further details).

## Programming Environment

These notebooks are written primarily in Python 3. 
If the default Python on your system is Python 3, then you will have a simpler time contributing to the project. 
If you only have Python 2, you might want to consider adding Python 3 to your system. 
In this regards, you may find useful to take a look at the *Programming Environment* [notebook]() where you 
could find links and details on how to set up your environment depending on your platform.

## <a name="slides"></a>Teaching Material ##

Provided notebooks can be easily converted in HTML slides by the `nbconvert` command of iPython.
Cells have been already organized into the different types of slides available, namely 
*slides*, *sub-slides*, and *fragments*.
To this end, the content of each cell has been edited and split to fit into the corresponding
type.

To view and modify the details about slides segmentation and organization, you are just required to 
enable the **Slideshow** mode on the *Cell Toolbar* during a running iPython notebook session.

The folder `slides` contains all the converted versions of the notebooks that are ready to be used.

These slides are mainly intended to be used by teachers in their programming classes.

### Converting and Playing notebooks as HTML slides: 

The notebooks ship with a control script (namely, `control_notebook_slides.py`) that can be used 
both to generate and to serve the HTML slides.

In more details, please use the following two commands to:

- Generate the HTML slides: `python control_notebook_slides.py -a convert`
- Start the Presentation: `python control_notebook_slides.py -a serve`

