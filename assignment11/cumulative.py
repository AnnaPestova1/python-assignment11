'''Task 2: A Line Plot with Pandas

Create a file called cumulative.py. The boss wants to see how money is rolling in. You use SQL to access ../db/lesson.db again.
 You create a DataFrame with the order_id and the total_price for each order. 
 This requires joining several tables, GROUP BY, SUM, etc.
Add a "cumulative" column to the DataFrame. This is an interesting use of apply():
def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)
Because axis=1, apply() calls the cumulative function once per row. Do you see why this gives cumulative revenue? One can instead use cumsum() for the cumulative sum:
df['cumulative'] = df['total_price'].cumsum()
Use Pandas plotting to create a line plot of cumulative revenue vs. order_id.
Show the Plot.
'''


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT o.order_id,
    SUM(p.price*l.quantity) AS total_price
    FROM Orders AS o
    JOIN Line_items AS l ON l.order_id = o.order_id
    JOIN Products AS p ON p.product_id = l.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id """
    df=pd.read_sql_query(sql_statement, conn)
    print(df)
    def cumulative(row):
        totals_above = df['total_price'][0:row.name+1]
        return totals_above.sum()

    # df['cumulative'] = df.apply(cumulative, axis=1)
    df['cumulative'] = df['total_price'].cumsum()
    print(df)
    df.plot(x="cumulative", y="order_id", kind="line", title="Money Spent by All Orders")
    plt.show()
