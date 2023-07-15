#data must be coverted from an xlsx to a csv file before being fed into this software

import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import pandas as pd
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import base64

# Load the file into a dataframe
df = pd.read_csv('Test.csv', encoding='ISO-8859-1')

# Convert 'start_date' and 'end_date' to datetime format
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# Limit the number of projects to 50
df = df.head(50)

# Create a new figure with increased size
fig, ax = plt.subplots(figsize=(10, len(df)/2))

# Loop over the rows and add a bar to the plot for each project
for i, row in df.iterrows():
    start_date = date2num(row['start_date'])
    end_date = date2num(row['end_date'])
    ax.barh(i, end_date - start_date, left=start_date)

# Set the y-axis labels to be the project names, rotate them and adjust font size
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Project'], rotation=0, fontsize=8)

# Format the x-axis as dates
ax.xaxis_date()

# Tight layout
plt.tight_layout()

# Save the figure to a BytesIO object
img_output = BytesIO()
FigureCanvas(fig).print_png(img_output)

# Get the PNG image data
image_base64 = base64.b64encode(img_output.getvalue()).decode('utf8')


# Chart for second 50 entries

import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import pandas as pd
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import base64

# Load the file into a dataframe
df = pd.read_csv('Test.csv', encoding='ISO-8859-1')

# Convert 'start_date' and 'end_date' to datetime format
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# Select the next 50 projects
df = df.iloc[50:100]

# Create a new figure with increased size
fig, ax = plt.subplots(figsize=(10, len(df)/2))

# Loop over the rows and add a bar to the plot for each project
for i, row in df.iterrows():
    start_date = date2num(row['start_date'])
    end_date = date2num(row['end_date'])
    ax.barh(i-50, end_date - start_date, left=start_date)

# Set the y-axis labels to be the project names, rotate them and adjust font size
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Project'], rotation=0, fontsize=8)

# Format the x-axis as dates
ax.xaxis_date()

# Tight layout
plt.tight_layout()

# Save the figure to a BytesIO object
img_output = BytesIO()
FigureCanvas(fig).print_png(img_output)

# Get the PNG image data
image_base64 = base64.b64encode(img_output.getvalue()).decode('utf8')
