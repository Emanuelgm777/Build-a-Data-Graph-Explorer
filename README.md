# Build a Data Graph Explorer

## Author: Emanuel Gonzalez

### Description

This repository contains the code for the **Data Graph Explorer**, a Python-based tool designed to help users explore data through interactive graphs and visualizations. The tool allows users to upload a CSV file from different sources, such as local files, URLs, or predefined URLs in the code. The user can then visualize and analyze the data through scatter plots, line graphs, and other interactive visualizations.

### Features

1. **Data Loading**: 
   - Upload CSV file from local storage.
   - Fetch CSV from a URL provided by the user.
   - Use a predefined URL in the code to load a CSV.
   
2. **Data Visualization**:
   - Scatter Plot and Line Graph generation.
   - Dynamic selection of data columns for X and Y axes.
   - Interactive input for column selection and graph type.

3. **Data Exploration**:
   - Print headings and first two rows of the loaded dataset.
   - Convert selected columns to NumPy arrays for further manipulation.
   - Ability to customize the graph type (scatter plot or line graph).

4. **Interactivity**:
   - Interactive widgets to help the user select columns and graph types.
   - Customizable features for data exploration, visualization, and graph manipulation.

### Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Requests
- Ipywidgets (for interactivity in Google Colab)

### Installation

To install the necessary libraries, run the following command:

```bash
pip install pandas numpy matplotlib requests ipywidgets
Usage
Run the Python Script:

After cloning this repository, you can run the script in a Python environment (such as Google Colab or locally).

Follow the interactive prompts to load a CSV, select columns for visualization, and choose the graph type.

Google Colab Usage:

If running in Google Colab, simply upload your CSV file or provide a URL to load the data.

Use the provided interactive widgets to explore and visualize the data dynamically.

Example Usage
Load Data: Select how to load the CSV data:

Upload a file from your local system.

Input a URL to load a CSV file from the web.

Use a predefined URL hardcoded in the code.

Data Exploration:

After the data is loaded, the first two rows and the column headers will be printed.

You can choose any columns to visualize in a scatter plot or line graph.

Visualization:

Choose the graph type (scatter plot or line graph).

Customize the X and Y axes by selecting columns from the dataset.

Example Output
A scatter plot or line graph will be displayed, showing the selected data from the CSV file.

The graph will help visualize trends, patterns, and outliers in the dataset.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author: Emanuel Gonzalez
