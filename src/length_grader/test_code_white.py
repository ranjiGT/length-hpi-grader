#!/usr/bin/python
# -*- coding: utf-8 -*-

from testbook import testbook
import ipywidgets as widgets
from IPython.display import display, Javascript, clear_output
from ipylab import JupyterFrontEnd



url = 'http://localhost:8888/lab/tree/obs/ssnn_solved.ipynb'
nbfile = url.rsplit('/', 1)[-1]

def grader():
    points = 0.0
    """
    TASK 1: SGD
    """

    def test_a():
        score_a = 0.0

        try:
            with testbook(nbfile, execute=[1, 3, 5,
                          7]) as tb1:
                if tb1.cell_output_text(7) == 'Test passed.':
                    score_a += 1
                    print('Task 1 Passed.')
        except Exception:
            print('Task 1 failed.')

        return score_a

    points_a = test_a()

    def test_b():
        score_b = 0.0

        try:
            with testbook(nbfile, execute=[1, 3, 9, 11,
                          13]) as tb2:
                if tb2.cell_output_text(13) == 'Test passed.':
                    score_b += 1
                    print('Task 2 Passed.')
        except Exception:
            print('Task 2 failed.')

        return score_b

    points_b = test_b()

    def test_c():
        score_c = 0.0

        try:
            with testbook(nbfile, execute=[1, 3, 11, 15,
                          17]) as tb3:
                if tb3.cell_output_text(17) == 'Test passed.':
                    score_c += 1
                    print('Task 3 Passed.')
        except Exception:
            print('Task 3 failed.')

        return score_c

    points_c = test_c()

    def test_d():
        score_d = 0.0

        try:
            with testbook(nbfile, execute=[1, 3, 19,
                          21]) as tb4:
                if tb4.cell_output_text(21) == 'Test passed.':
                    score_d += 1
                    print('Task 4 Passed.')
        except Exception:
            print('Task 4 failed.')
        return score_d

    points_d = test_d()
    
    points = points_a + points_b + points_c + points_d

    return points

grade = grader()

print('Your score is: ',grade)

"""
def submit_score(a):
    return grade
"""

"""
Check score
out = widgets.Output()

def show_score(grade):
    with out:
        display(Javascript(f'window.open("{grade}");'))

ss = widgets.Button(description="Check scores", tooltip='https://www.google.com', button_style = 'success')
ss.on_click(show_score)

with out:
    display(ss)
out

"""


"""
Submit Score
"""

button2 = widgets.Button(
    description ='Fetch score',
    disabled = False,
    button_style = 'info',
    tooltip = 'Submit your score to LMS')
    
display(button2)
#Jupyter.actions.call("jupyter-notebook:save-notebook")
def on_button2_clicked(_):
        app = JupyterFrontEnd()
        app.commands.execute('docmanager:save')
        clear_output()
        print(grade)

button2.on_click(on_button2_clicked)

"""
open link to openHPI
"""

link_view = widgets.Output()

@link_view.capture(clear_output=True)
def callback(url):
    display(Javascript(f'window.open("{url.tooltip}");'))

button = widgets.Button(
    description = "Submit to openHPI", 
    tooltip = 'https://open.hpi.de/courses/mypbt/items/2ZmFtAEWnAAWb44xJJMPzP', 
    button_style = 'success'
)
button.on_click(callback)
display(button, link_view)
