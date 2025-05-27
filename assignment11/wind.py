'''Task 3: Interactive Visualizations with Plotly

Load the Plotly wind dataset, via the following:
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')
Print the first and last 10 lines of the DataFrame.
Clean the data. You need to convert the 'strength' column to a float. Use of str.replace() with regex is one way to do this, followed by type conversion.
Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
Save and load the HTML file, as wind.html. Verify that the plot works correctly.'''

import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

''' according documentation the column 'strength' 
has follow values:
0-1
1-2
2-3
3-4
4-5
5-6
6+
because task 3 does not clarify how to clean data
I assume it is better to leave the lowest number in range
'''

df['strength_clean'] = df['strength'].str.extract(r'^(\d)').astype(float)
# print(type(df['strength_clean'][1]))
print(df.head(10))

fig = px.scatter(df, x='strength_clean', y='frequency', color='direction',
                 title='Wind strength based on frequency', hover_data=['frequency'])
fig.write_html('wind.html', auto_open=True)