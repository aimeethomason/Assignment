# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:06:41 2021

@author: Aimee Thomason
"""

# The first section of code will import the relevant packages into python as well as
# creating variables and lists.

# Import matplotlib is a comprehensive library for creating static, animated, and 
# interactive visualisations in Python.

import matplotlib

# Matplotlib also has different "backends" which allows it to render its graphics in 
# different ways. The following code will change the backend to render as associated 
# with TkInter. This must be placed before any other matplotlib imports.

matplotlib.use('TkAgg')

# Import random provides access to random functions.
# Import matplotlib.pyplot allows data to be plotted in graphs.
# Import matplotlib.animation allows for a live animation.
# Import time provides access to time functions.
# Import af_assignment provides access to the agents in a random location.
# Import csv module provides access to CSV files.
# Import tkinter provides access to the Tk GUI toolkit.
# Import requests provides access to HTTP library, enabling HTTP requests in Python, 
# reducing complexities behind the interface.
# Import bs4 is a python library for pulling data out of HTML and XML files. This 
# provides idiomatic ways of navigating, searching, and modifying the parse tree, 
# saving the programmer time.

import random
import matplotlib.pyplot
import matplotlib.animation
import time
import af_assignment
import csv
import tkinter
import requests
import bs4

# The following code creates a new variable 'r' which scrapes the HTTP data on 
# the web and downloads the y and x coordinates.

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# To test that the model is initiated with data from the web, the y and x 
# coordinates from the HTTP data are printed.

print(td_ys)
print(td_xs)

# Here, a new variable 'f' is created which will open the CSV 'in.txt' file.

f = open('in.txt', newline=(''))

# A new variable called 'reader' is also created to allow for the CSV file to be 
# read within python.

reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)    

# To create an environment that allows agents to later interact with, an empty 
# list called environment is created.

environment = []

# The following code uses a for-loop that will allow each row to be a new list in
# the environment, with each row containing values.
for row in reader:
    # Here a new list called rowlist is created.
    rowlist = []
    for value in row:       
        # The values in each row of the CSV file are appended to the rowlist.
        rowlist.append(value)        
    # The rowlist is then appended to the environment.
    environment.append(rowlist)
    
# To test that the environment has been appended to the model, the environment can
# be printed.
    
print(environment)

# An empty list called agents is created to allow for coordinates to be added.

agents = []

# A new variable created called "num_of_agents" will control how many agents there
# will be.

num_of_agents = 10

# Another new variable "num_of_iterations" will allow the agent coordinates
# to move an arbitrary number of times.

num_of_iterations = 100

# "neighbourhood" is another variable created. This allows for agents to search
# for close neighbours within the distance attached to this variable.

neighbourhood = 20

# The next section of code will connect the model to the agent framework, allowing
# for each agent to interact with both another agent and its environment.

# A for-loop defined by the num_of_agents is created to allow for a list of agent
# coordinates to be generated.
for i in range(num_of_agents):
    # Both y and x variables are created using the obtained HTTP data from the web.
    # The y and x variables are then multiplied by three to allow the coordinates to
    # match the same extent as the environment.
    y = int((td_ys[i].text)*3)
    x = int((td_xs[i].text)*3)
    # The agents.append function is used to add the first set of coordinates to the list.
    # At this point, the environment list, along with the agents and the y and x
    # coordinates are passed into the agent framework's constructor.
    agents.append(af_assignment.Agent(environment, agents, y, x))

# A single agent 'a' is created to connect the model with the agent framework.

a = af_assignment.Agent(environment,agents, y, x)

# To test the single-agent connection, the x and y coordinates from the agent
# framework are printed.

print(a._y,a._x)

# The following code tests that the coordinates from the agent framework move.

print(a.move)

# Start of the code used to measure the time taken for the code to run during the
# animation.

start = time.time()

# The following code defines and sets two new variables, figure plot and axis.
# These are created to help construct the model within an animation.

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Random.seed is used to create a more deterministic pseudorandom sequence.
# Here, 20 is used for the seed. This ensures that by using the same seed, the 
# same pattern of random numbers will be generated. 

random.seed(20)

# Carry_on is used to create a global variable that can be used inside and outside of
# functions.

carry_on = True

# To allow the agents to randomly move, a function called 'def update' defined by the
# frame number is created.
def update(frame_number):
    # Global carry_on is called within the function, setting true, allowing the animation
    # to continue running.
    global carry_on
    # The following code clears the figure plot.
    fig.clear() 
    # As carry_on is true, random.shuffle is used to randomly shuffle the agents list.
    if carry_on:
        random.shuffle(agents)
        # Here, a for-loop is used, using the for j in range function to specify the number
        # of times the coordinates can move (10 times).
        for j in range(10):
            # Within the for-loop, the number of agents is defined within for i in range.
            # Here, move, eat and share functions obtained from the agent framework, allow
            # the agents to interact with both other agents and the environment.
            for i in range(num_of_agents):
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood) 
            
# The following code will display the environment data, adjusted to match the area the 
# agents are in. Here, Matplotlib.pyplot.ylim/xlim are used to set the y and x limits 
# of the current axes. A title is also created.
        
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.title("An Animation of the Movement of Sheep Around an Environment.")
    matplotlib.pyplot.imshow(environment)

# The following code will plot the agent y and x coordinates on the scatter plot and
# will be highlighted by the colour blue.
   
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color='blue')
        
# A generator function is used to yield a value that allows the function for each step 
# of the animation to be updated. As the global variable remains true, if a is less than 10,
# as well as less than the number of iterations, a is yielded and increased by 1.
		
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        while (a < num_of_iterations) & (carry_on):
            yield a			
            a = a + 1

# The following code uses a run function to allow the animation to run. Here, the 
# stopping condition of the animation is defined by the gen_function.

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# The following code allows for the main window ("root") to be created. Here, the 
# title is set and the matplotlib canvas is laid out within the window, displaying the
# matplotlib figure.

root = tkinter.Tk()
root.wm_title("Model")
root.title("Animation: Agent-Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# The next part of the code builds the menu bar within the main window. This will use
# a command function that allows the user to run the model.

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# The following code defines an exiting function. Here, as the animation ends
# and the window has been closed, the current command will be stopped.

def exiting():
    root.quit()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', exiting) 

# Tkinter.mainloop is used to start running the animation.

tkinter.mainloop() # Wait for interactions.

# The end of the code used to measure the time taken for the code to run during the
# animation.

end = time.time()

         