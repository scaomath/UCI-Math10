# UCI-Math10
This is the repository for Math 10 Intro to Programming for Data Science
---------------------------------------------------------

**Math 10** is the first dedicated programming class in the Data Science specialization designed mainly for Math majors at University of California Irvine. We will learn some of current de facto algorithms, and verify some theorems in Mathematics behind in data science/machine learning mainly using Python, and the format can be adapted to other popular languages like R and Julia.

### Prerequisites: 
**MATH 2D** Multivariate Calculus
<br><br>
**MATH 3A** Linear Algebra(can be taken concurrently)
<br><br>
**MATH 9** Introduction to Programming for Numerical Analysis
<br><br>
#### Recommended: 
**MATH 130A** Probabilty I
<br><br>
**ICS 31** Introduction to Programming 
<br><br>

----

### Lecture notes (Jupyter notebooks) are available in the Lectures folder.

| Lecture    | Contents |
|:----------|:--------|
|  Lecture 1 | Intro to Jupyter notebooks, expressions, operations, variables |
|  Lecture 2 | Defining your own functions, types (float, bool, int), Lists, IF-ELSE  |
|  Lecture 3 | Numpy arrays I, tuples, slicing |
|  Lecture 4 | Numpy arrays II, WHILE and FOR loops, advanced slicing |
|  Lecture 5 | Matplotlib I, plot the graph of a function |
|  Lecture 6 | More on vectorization, linear algebra routines |
|  Lecture 7 | Matplotlib II, histograms|
|  Lecture 8 | Randomness I; Matplotlib III, scatter plot|
|  Lecture 9 | Randomness II, descriptive statistics, sampling data|
|  Lecture 10 | Randomness III, random walks, Law of large numbers|
|  Lecture 11 | Introduction to class and methods, object-oriented programming |
|  Lecture 12 | Optimization I: Optimizing functions, gradient descent|
|  Lecture 13 | Fitting data I: Linear model, regression, least-square|
|  Lecture 14 | Optimization II: Solving linear regression by gradient descent|
|  Lecture 15 | Fitting data II: Overfitting, interpolation, multivariate linear regression|
|  Lecture 16 | Classification I: Bayesian classification, supervised learning models|
|  Lecture 17 | Classification II: Logistic regression, binary classifier|
|  Lecture 18 | Classification III: Softmax regression, multiclass classifier|
|  Lecture 19 | Optimization III: Stochastic gradient descent|
|  Lecture 20 | Classification IV: K-nearest neighbor|
|  Lecture 21 | Dimension reduction: Singular Value Decomposition (SVD), Principal Component Analysis (PCA)|
|  Lecture 22 | Feedforward Neural Networks I: models, activation functions, regularizations |
|  Lecture 23 | Feedforward Neural Networks II: backpropagation |
|  Lecture 24 | PyTorch, Autograd, and other tools to look at |


### Labs and Homeworks
There are two Labs per week. One is a Lab exercise, aiming to review and sharpen your programming skills. 
The other is a graded Lab assignment, which is like a collaborative programming quiz.
Homework is assigned on a weekly basis, the later ones may look a mini project.
Lab assignments' and Homeworks' solutions are available on [Canvas](https://canvas.eee.uci.edu).


### Textbook
No official textbook but we will use the following as references:
[Scientific Computation: Python Hacking for Math Junkies. Version3, With iPython](https://github.com/biomathman/python-book/) (Math 9 reference book)
<br><br>
[Python Data Science Handbook. Online version](https://jakevdp.github.io/PythonDataScienceHandbook/)


### Software
Python 3 and Jupyter notebook (iPython). Please install [Anaconda](https://www.anaconda.com/download). To start Jupyter notebook, you can either use the Anaconda Navigator GUI, or start Terminal on Mac OS/Linux, Anaconda prompt on Windows: in the directory of `.ipynb` file, run the command `jupyter notebook` to start a notebook in your browser (Chrome recommended). If Jupyter complains that a specific package is missing when you 
run your notebook, then return to the command line, execute `conda install <name of package>`, and re-run the notebook cell. 

## Acknowledgements 
A major portion of the first half of the course is adapted from [Umut Isik's Math 9 in Winter 2017](https://www.math.uci.edu/~isik/teaching/17W_MATH9/index.html) with much more emphases on vectorization and examples are presented in a more data-oriented way. Part of the second half of this course (regressions, classifications, multi-layer neural net, PCA) is adapted from [Stanford Deep Learning Tutorial](http://ufldl.stanford.edu/tutorial/)'s MATLAB codes to vectorized implementations in Numpy from scratch, together with the `scikit-learn`'s counterparts.