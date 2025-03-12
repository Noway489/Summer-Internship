import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

def display_graph(df, canvas):
    # Clear the previous graph
    # if canvas.figure:
    #     canvas.figure.clear()

    # Create a new figure and plot the DataFrame
    fig = plt.figure()

    num = df['num'][0]
    x_col = 'Time'
    if num == 1:
        y_col = 'df 1'
    elif num == 2:
        y_col = 'df 2'
    elif num == 3:
        y_col = 'df 3'
    elif num == 4:
        y_col = 'df 4'
    elif num == 5:
        y_col = 'df 5'
    elif num == 6:
        y_col = 'df 6'
    elif num == 7:
        y_col = 'df 7'
    elif num == 8:
        y_col = 'df 8'
    elif num == 9:
        y_col = 'df 9'
    else:
        y_col = 'df 10'

    x = df[x_col]
    y = df[y_col]

    plt.plot(x, y)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title('Plot of Value vs. Time')

    # Create a FigureCanvasTkAgg object to display the graph in the GUI
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Store the figure reference in the canvas object
    canvas.figure = fig

def component_clicked(event):
    component_id = canvas.find_withtag(tk.CURRENT)[0]
    component_index = list(component_objects.values()).index(component_id)
    component_key = sorted(components_dict.keys(), key=lambda x: components_dict[x]['position'])[component_index]
    dataframe = components_dict[component_key]['dataframe']
    display_graph(dataframe, graph_canvas)

# Create a sample DataFrame
df1 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 1': [0, 10, 20, 30, 40], 'num': [1, 1, 1, 1, 1]})
df2 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 2': [0, 10, 30, 60, 100], 'num': [2, 1, 1, 1, 1]})
df3 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 3': [0, 5, 10, 15, 20], 'num': [3, 1, 1, 1, 1]})
df4 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 4': [0, 5, 10, 15, 20], 'num': [4, 1, 1, 1, 1]})
df5 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 5': [0, 2, 8, 18, 32], 'num': [5, 1, 1, 1, 1]})
df6 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 6': [0, 1, 2, 3, 4], 'num': [6, 1, 1, 1, 1]})
df7 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 7': [0, 8, 16, 24, 32], 'num': [7, 1, 1, 1, 1]})
df8 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 8': [0, 4, 12, 24, 40], 'num': [8, 1, 1, 1, 1]})
df9 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 9': [0, 2, 4, 6, 8], 'num': [9, 1, 1, 1, 1]})
df10 = pd.DataFrame({'Time': [0, 1, 2, 3, 4], 'df 10': [0, 3, 6, 9, 12], 'num': [10, 1, 1, 1, 1]})

# Sample components dictionary
components_dict = {
    "1": {"position": 1, "name": "Component 1", "kind": "Type A", "health": "good", "dataframe":df1},
    "2": {"position": 2, "name": "Component 2", "kind": "Type B", "health": "bad", "dataframe": df2},
    "3": {"position": 3, "name": "Component 3", "kind": "Type C", "health": "good", "dataframe": df3},
    "4": {"position": 4, "name": "Component 4", "kind": "Type D", "health": "good", "dataframe": df4},
}

# Create the main window
window = tk.Tk()
window.title("Component Flowchart")

# Create a canvas for drawing the flowchart
canvas = tk.Canvas(window, width=800, height=400)
canvas.pack()

# Create a dictionary to store the rectangles and text objects
component_objects = {}

# Create a dictionary to store the dataframes
dataframe_dict = {}

# Create the flowchart
x = 100
for component_id, attributes in sorted(components_dict.items(), key=lambda x: x[1]['position']):
    # Set the color based on health
    color = "green" if attributes['health'] == "good" else "red"

    # Draw the rectangle
    rect = canvas.create_rectangle(x-50, 150, x+50, 250, fill=color)
    component_objects[component_id] = rect

    # Add the component name as text
    canvas.create_text(x, 200, text=attributes['name'], fill="white")

    # Bind the click event to the rectangle
    canvas.tag_bind(rect, '<Button-1>', component_clicked)
    x += 200

# Create a frame to hold the graph
graph_frame = tk.Frame(window)
graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a FigureCanvasTkAgg object to display the graph
graph_canvas = FigureCanvasTkAgg(plt.figure())
graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Run the main loop
window.mainloop()
