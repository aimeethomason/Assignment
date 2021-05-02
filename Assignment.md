# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:06:41 2021

@author: Aimee Thomason
"""

# Import relevant packages from the python library.
# Import matplotlib is a comprehensive library for creating static, animated, and 
# interactive visualizations in Python.

import matplotlib

# The following code will render matplotlib to a Tk canvas.

matplotlib.use('TkAgg')

# Import random provides access to random functions.
# Import operator supplies functions that are equivalent to Python's operators.
# Import matplotlib.pyplot allows data to be plotted in graphs.
# Import matplotlib.animation to make a live animation.
# Import time provides access to time functions.
# Import agent framework module to acess the agents in a random location.
# Import csv module to enable access to csv files.
# Import tkinter provides access to the Tk GUI toolkit.
# Import requests provides access to HTTP library, enabling HTTP requests in Python, 
# reducing complexities behind the interface.
# Import bs4 is a python library for pulling data out of HTML and XML files. This provides
# idiomic ways of navigating, searching, and modifying the parse tree, saving the programmer time.

import random
import operator
import matplotlib.pyplot
import matplotlib.animation
#import time
import af_assignment
import csv
import tkinter
import requests
import bs4

# The following code creates a new variable 'r' which scrapes the http data on 
# the web, downloading and printing the y and x data.

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

# The following code will create a new variable 'f' which will open the CSV 'in.txt' file.

f = open('in.txt', newline=(''))

# A new variable called 'reader' is created which allows the CSV file to be read within
# python.

reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)    

# Create an empty list named Environment.

environment = []

# The following code will create a new list named rowlist, for each row in the read
# csv file. The values in each row of the CSV file can then be appended to the rowlist.
# The rowlist can then be appended to the environment. This will allow each row to be a 
# new list in the environment, with each row filled with values.

for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
    
# Test that the environment has been appended to the model.
    
print(environment)
   

# Test that the self.x and self.y co-ordinates (within the agent framework) move
# randomly

# a.move()
# print(a._y, a._x)

# Start of the code used to measure the time taken for the code to run.
# start = time.time()

# The following code will create a function which returns the Euclidian distance between
# two arbitary pair of agents derived from the agent framework, using Pythagoras' theorem.

# def distance_between(agents_row_a, agents_row_b):
    # return (((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y - agents_row_b._y)**2))**0.5
    
# Create an empty list using agents which coordinates can be added to.

agents = []

# Create a new variable to control how many agents there will be.

num_of_agents = 10

# Create a new variable to move the agent co-ordinates an arbitary number of times.

num_of_iterations = 100

# Create a new variable to allow agents to search for close neighbours within the
# distance attached to this variable.

neighbourhood = 20

# The following code will use a for-loop defined by the num of agents to generate 
# a list of agent coordinates, obtained from a random location within the agent
# framework. To add the first set of coordinates to the list, the agents.append 
# function will be used. At this point, the environment list is passed into the
# agent's cronstructor along with the x and y variables.

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(af_assignment.Agent(environment, agents, y, x))

# Create a single agent that connects the model with the agent framework module.

a = af_assignment.Agent(environment,agents, y, x)

# The following code will create a new variable which defines the figure plot and axis.

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# # Test the single agent connection by printing the x and y coordinates from the agent
# framework.Test the link to the list of agents into each agent.

print(a._y,a._x)

# Test that the co-ordinates from the agent framework move.

print(a.move)

    
# To give the model behaviour, a code within a for-loop can be created to randomly 
# move all agent co-ordinates using the move and eat methods, obtained again from the agent framework. 
# This is achievable with the for I in range function. The for j in range function specifies 
# the number of times the coordinates can move, which is 100. Here, the y co-ordinated will 
# be refered to as agents[i].y and the x co-ordinate will be refered to as agents[i].x.
# Here, x and y coordinates are edited using the move and eat methods obtained from the agent
# framework file.

carry_on = True

def update(frame_number):
     
    global carry_on
    fig.clear() 
    if True:
        
        random.shuffle(agents)
        
        for j in range(10):
            for i in range(num_of_agents):
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood) 
                
        if random.random() < 0.1:
            carry_on = False
            print("stopping condition")
        
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# The following code builds the main window ("root"); sets its title, then creates 
# and lays out a matplotlib canvas embedded within our window and associated with fig,
# our matplotlib figure.

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# This code builds the menu bar within the main window; alongside a command function
# that allows the model to be run.

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# 

tkinter.mainloop() # Wait for interactions.

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

# Randomise the order in which agents are processed each iteration.

         