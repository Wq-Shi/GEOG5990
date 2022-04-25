# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:04:44 2022

@author: SWQ
"""
# import random
import agentframework
import matplotlib.pyplot
import matplotlib.animation 
import csv
import matplotlib
matplotlib.use('TkAgg')
import tkinter

environment = []
f = open('in.csv',newline = '')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    row_1 = []
    for value in row:
        row_1.append(value)
    environment.append(row_1)
# print(environment)
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show() 
f.close()

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

root = tkinter.Tk()
root.wm_title("Model")

carry_on = True

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents)) 

# Move the agents.
def update(frame_number):
    
    fig.clear()   
    global carry_on
    carry_on = True
    for i in range(num_of_agents):
        agents[i].eat()
        agents[i].move()
        agents[i].share_with_neighbours(neighbourhood)
    #Plot
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)
    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition")
    
    for j in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[j].x,agents[j].y)
        # print(agents[i][0],agents[i][1])
    # matplotlib.pyplot.show()

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()


#Just showing menu elements
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model",menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()

# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=100)
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)


# def distance_between(agents_row_a, agents_row_b):
#     return (((agents_row_a.x - agents_row_b.x)**2) +
#     ((agents_row_a.y - agents_row_b.y)**2))**0.5

# matplotlib.pyplot.xlim(0, 299)
# matplotlib.pyplot.ylim(0, 299)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
# matplotlib.pyplot.show()

# for agents_row_a in agents:
#     dis_list = []
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b)
#     dis_list.append(distance)
# print(dis_list)