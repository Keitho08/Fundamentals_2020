# Fundamental's of Data Analysis
***
## Fundamental's of Data Analysis - Task's 2020
***
## Galway Mayo Intitute of Technology - HDip Data Analytics 2020-2021
***
### Keith Brazill - G00387845
***

**Project Brief:**

Four tasks will be listed here at different times during the semester. You should complete
all tasks in a single jupyter notebook. This, along with relevant files like a README,
should be in a single git repository synced with a hosting provider like GitHub [1]. That
URL should then be submitted using the link on the Moodle page.
1. October 5th, 2020: Write a Python function called counts that takes a list as
input and returns a dictionary of unique items in the list as keys and the number of
times each item appears as values. So, the input ['A', 'A', 'B', 'C', 'A']
should have output {'A': 3, 'B': 1, 'C': 1} . Your code should not depend
on any module from the standard library1 or otherwise. You should research
the task first and include a description with references of your algorithm in the
notebook.
2. November 2nd, 2020: Write a Python function called dicerolls that simulates
rolling dice. Your function should take two parameters: the number of dice k and
the number of times to roll the dice n. The function should simulate randomly
rolling k dice n times, keeping track of each total face value. It should then return
a dictionary with the number of times each possible total face value occurred. So,
calling the function as diceroll(k=2, n=1000) should return a dictionary like:
{2:19,3:50,4:82,5:112,6:135,7:174,8:133,9:114,10:75,11:70,12:36}
You can use any module from the Python standard library you wish and you should
include a description with references of your algorithm in the notebook.
3. November 16th, 2020: The numpy.random.binomial function can be used to
simulate flipping a coin with a 50/50 chance of heads or tails. Interestingly, if a
coin is flipped many times then the number of heads is well approximated by a
bell-shaped curve. For instance, if we flip a coin 100 times in a row the chance of
getting 50 heads is relatively high, the chances of getting 0 or 100 heads is relatively
low, and the chances of getting any other number of heads decreases as you move
away from 50 in either direction towards 0 or 100. Write some python code that
simulates flipping a coin 100 times. Then run this code 1,000 times, keeping track
of the number of heads in each of the 1,000 simulations. Select an appropriate
plot to depict the resulting list of 1,000 numbers, showing that it roughly follows
a bell-shaped curve. You should explain your work in a Markdown cell above the
code.
4. November 30th, 2020: Simpson’s paradox is a well-known statistical paradox
where a trend evident in a number of groups reverses when the groups are combined
into one big data set. Use numpy to create four data sets, each with an x array
and a corresponding y array, to demonstrate Simpson’s paradox. You might
create your x arrays using numpy.linspace and create the y array for each
x using notation like y = a * x + b where you choose the a and b for each
x , y pair to demonstrate the paradox. You might see the Wikipedia page for
Simpson’s paradox for inspiration.


**Getting started**

In order to run the jupyter notebook in this repository the following is recommended to download and install Python using Anaconda. Anaconda is available at:
https://docs.anaconda.com/anaconda/install/

**Packages used in this project**

The following packages were used in this assignment to carry out the required tasks in the project brief:

* Python https://www.python.org/downloads/
* Numpy http://www.numpy.org/ - The fundamental package for scientific computing with Python.
* Jupyter Notebook https://jupyter.org/ - Project Jupyter exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.
* matplotlib.pyplot https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html - matplotlib.pyplot is a state-based interface to matplotlib. It provides a MATLAB-like way of plotting. pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation.
* seaborn https://seaborn.pydata.org/ - Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
* pandas https://pandas.pydata.org/ - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

**Importing Packages**

The above packages can be imported into Python. Use Import function in the notebook or in ipython to import:

* import numpy as np
* import seaborn as sns
* import matplotlib.pyplot as plt
* import pandas as pd

Jupyter notebook is already imported as standard in python when installed via Anaconda. It can be accessed by typing "jupyter notebook" in the command line which will open up the notebook in your browser.

**Summary of Repository**

The notebook **KeithBrazill_FundamentalsTasks_2020.ipynb** contained in this repository, will carry out the four tasks assigned as part of the module Fundamentals of Data Analysis on the postgraduate diploma in Computer Science with Data Analytics at Galway Mayo Institute of Technology.

The notebook consists of the following:

1. Introduction
2. Task 1 - Counts: A python function that takes a list as input and counts the frequency of each value.
3. Task 2 - Dicerolls: A python function that simulates rolling dice based on the parameters; number of dice and number of rolls.
4. Task 3 - Coin FLips: A numpy binomial function that simulates coin flipping.
5. Task 4 - Simpson Paradox: The simpson paradox is explained using the python numpy package
6. Conclusion

For each of the tasks the brief is provided and then using a combination of code and markdown cells each task is completed and clearly explained throughout. References are provided following each section.


**References** 

*A complete list of all references used in this repository is included below:*

1. Stack Overflow. 2020. Using A Dictionary To Count The Items In A List. [online] Available at: https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list [Accessed 4 December 2020].
2. Stack Overflow. 2020. Using A Dictionary To Count The Items In A List. [online] Available at: https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list [Accessed 4 December 2020].
3. GeeksforGeeks. 2020. Python | Get A List As Input From User - Geeksforgeeks. [online] Available at: https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/ [Accessed 4 December 2020].
4. Stack Overflow. 2020. How Can I Count The Occurrences Of A List Item?. [online] Available at: https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item [Accessed 4 December 2020].
5. Docs.python.org. 2020. 5. Data Structures — Python 3.9.1Rc1 Documentation. [online] Available at: https://docs.python.org/3/tutorial/datastructures.html#dictionaries [Accessed 4 December 2020].
6. Docs.python.org. 2020. Built-In Types — Python 3.9.1Rc1 Documentation. [online] Available at: https://docs.python.org/3/library/stdtypes.html#typesmapping [Accessed 4 December 2020].
7. Docs.python.org. 2020. Built-In Types — Python 3.9.1Rc1 Documentation. [online] Available at: https://docs.python.org/3/library/stdtypes.html#typesmapping [Accessed 4 December 2020].
8. Codegrepper.com. 2020. Return Occurences In List Python Code Example. [online] Available at: https://www.codegrepper.com/code-examples/python/return+occurences+in+list+python [Accessed 4 December 2020].
9. W3schools.com. 2020. Python Random Choices() Method. [online] Available at: <https://www.w3schools.com/python/ref_random_choices.asp> [Accessed 4 December 2020].
10. Docs.scipy.org. 2020. Numpy.Random.Choice — Numpy V1.10 Manual. [online] Available at: <https://docs.scipy.org/doc//numpy-1.10.4/reference/generated/numpy.random.choice.html> [Accessed 4 December 2020].
11. Stack Overflow. 2020. Rolling Two Dice And Tabulating Outcomes. [online] Available at: <https://stackoverflow.com/questions/23598952/rolling-two-dice-and-tabulating-outcomes?rq=1> [Accessed 4 December 2020].
12. Stack Overflow. 2020. Rolling Two Dice And Returning Count. [online] Available at: <https://stackoverflow.com/questions/49881078/rolling-two-dice-and-returning-count?rq=1> [Accessed 4 December 2020].
13. PythonForBeginners.com. 2020. Python Game : Rolling The Dice - Pythonforbeginners.Com. [online] Available at: <https://www.pythonforbeginners.com/code-snippets-source-code/game-rolling-the-dice> [Accessed 4 December 2020].
14. Stack Overflow. 2020. Dice Rolling Simulator In Python. [online] Available at: <https://stackoverflow.com/questions/44008489/dice-rolling-simulator-in-python> [Accessed 4 December 2020].
15. Data Science Unlimited. 2020. Step By Step: Coding A Dice Roll Simulator In Python | Examples For Beginners. [online] Available at: <https://datascienceunlimited.tech/step-by-step-coding-a-dice-roll-simulator-in-python/> [Accessed 4 December 2020].
16. Medium. 2020. How To Simulate A Dice Roll And Guess The Result In Python. [online] Available at: <https://medium.com/an-amygdala/how-to-simulate-a-dice-roll-and-guess-the-result-in-python-9785079af6f3> [Accessed 4 December 2020].
17. Docs.scipy.org. 2020. Numpy.Random.Choice — Numpy V1.10 Manual. [online] Available at: <https://docs.scipy.org/doc//numpy-1.10.4/reference/generated/numpy.random.choice.html> [Accessed 4 December 2020].
18. Pynative.com. 2020. Python-Range-Function/. [online] Available at: <https://pynative.com/python-range-function/> [Accessed 4 December 2020].
19. GeeksforGeeks. 2020. Count Numbers In Range Such That Digits In It And It's Product With Q Are Unequal - Geeksforgeeks. [online] Available at: <https://www.geeksforgeeks.org/count-numbers-in-range-such-that-digits-in-it-and-its-product-with-q-are-unequal/> [Accessed 4 December 2020].
20. W3schools.com. 2020. Introduction To Random Numbers In Numpy. [online] Available at: https://www.w3schools.com/python/numpy_random.asp [Accessed 19 November 2020].
21. W3schools.com. 2020. Binomial Distribution. [online] Available at: https://www.w3schools.com/python/numpy_random_binomial.asp [Accessed 19 November 2020].
22. Python-ds.com. 2020. Python Binomial Distribution. [online] Available at: http://www.python-ds.com/python-binomial-distribution [Accessed 19 November 2020].
23. Zach, V., 2020. How To Use The Binomial Distribution In Python - Statology. [online] Statology. Available at: https://www.statology.org/binomial-distribution-python/ [Accessed 19 November 2020].
24. Numpy.org. 2020. Numpy.Unique — Numpy V1.19 Manual. [online] Available at: <https://numpy.org/doc/stable/reference/generated/numpy.unique.html> [Accessed 5 December 2020].
25. Stack Overflow. 2020. Convert Two Lists Into A Dictionary. [online] Available at: <https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary> [Accessed 5 December 2020].
26. Stack Overflow. 2020. How To Count The Occurrence Of Certain Item In An Ndarray?. [online] Available at: <https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray> [Accessed 5 December 2020].
27. Brazill, K., 2020. Keitho08/Programming_For_Data-Analysis_Assignement1_2020. [online] GitHub. Available at: <https://github.com/Keitho08/Programming_for_Data-Analysis_Assignement1_2020> [Accessed 5 December 2020].
28. En.wikipedia.org. 2020. Inverted Bell Curve. [online] Available at: <https://en.wikipedia.org/wiki/Inverted_bell_curve#:~:text=In%20statistics%2C%20an%20inverted%20bell,falling%20off%20on%20both%20sides.> [Accessed 5 December 2020].
29. Brazill, K., 2020. Keitho08/Programming_For_Data-Analysis_Assignement1_2020. [online] GitHub. Available at: <https://github.com/Keitho08/Programming_for_Data-Analysis_Assignement1_2020> [Accessed 5 December 2020].
30. McLoughlin, I., 2020. Ianmcloughlin/Jupyter-Teaching-Notebooks. [online] GitHub. Available at: <https://github.com/ianmcloughlin/jupyter-teaching-notebooks/blob/master/fitting-lines.ipynb> [Accessed 7 December 2020].
31. GitHub. 2020. Willkoehrsen/Data-Analysis. [online] Available at: <https://github.com/WillKoehrsen/Data-Analysis/blob/master/statistics/Simpson's%20Paradox.ipynb> [Accessed 7 December 2020].
32. GitHub. 2020. Camdavidsonpilon/Simpsons-Paradox. [online] Available at: <https://github.com/CamDavidsonPilon/simpsons-paradox/blob/master/detect_paradox.py> [Accessed 7 December 2020].
33. Medium. 2020. Solving Simpson’S Paradox. [online] Available at: <https://towardsdatascience.com/solving-simpsons-paradox-e85433c68d03> [Accessed 7 December 2020].
34. Medium. 2020. Simpson’S Paradox: How To Prove Opposite Arguments With The Same Data. [online] Available at: <https://towardsdatascience.com/simpsons-paradox-how-to-prove-two-opposite-arguments-using-one-dataset-1c9c917f5ff9#:~:text=Simpson's%20Paradox%20occurs%20when%20trends,when%20the%20data%20are%20aggregated.&text=Since%20men%20tend%20to%20approve,combined%20and%20hence%20a%20paradox.> [Accessed 7 December 2020].
35. Medium. 2020. What Is Simpson’S Paradox?. [online] Available at: <https://towardsdatascience.com/what-is-simpsons-paradox-4a53cd4e9ee2> [Accessed 7 December 2020].
36. Pearl, J., 2020. Understanding Simpson’S Paradox. [online] Ftp.cs.ucla.edu. Available at: <https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf> [Accessed 7 December 2020].
37. paulvanderlaken.com. 2020. Simpson’S Paradox: Two HR Examples With R Code.. [online] Available at: <https://paulvanderlaken.com/2017/09/27/simpsons-paradox-two-hr-examples-with-r-code/> [Accessed 7 December 2020].
38. Pandas.pydata.org. 2020. Pandas.Dataframe.Loc — Pandas 1.1.4 Documentation. [online] Available at: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html> [Accessed 7 December 2020].
39. Seaborn.pydata.org. 2020. Seaborn.Regplot — Seaborn 0.11.0 Documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.regplot.html> [Accessed 7 December 2020].
40. Docs.scipy.org. 2020. Numpy.Random.Randint — Numpy V1.15 Manual. [online] Available at: <https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.randint.html> [Accessed 7 December 2020].
41. Stack Overflow. 2020. Different Colors For Points And Line In Seaborn Regplot. [online] Available at: <https://stackoverflow.com/questions/48145924/different-colors-for-points-and-line-in-seaborn-regplot/48146987> [Accessed 7 December 2020].
42. Docs.scipy.org. 2020. Numpy.Random.Randn — Numpy V1.15 Manual. [online] Available at: <https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html> [Accessed 7 December 2020].
43. Seaborn.pydata.org. 2020. Visualizing Regression Models — Seaborn 0.11.0 Documentation. [online] Available at: <https://seaborn.pydata.org/tutorial/regression.html> [Accessed 7 December 2020].
44. Numpy.org. 2020. Numpy.Concatenate — Numpy V1.19 Manual. [online] Available at: <https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html> [Accessed 7 December 2020].
45. Numpy.org. 2020. Numpy.Polyfit — Numpy V1.19 Manual. [online] Available at: <https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html> [Accessed 7 December 2020].

***
# End
