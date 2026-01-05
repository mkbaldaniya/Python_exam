import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns

def plot_bar_chart(data):
    try:
        plt.figure(figsize=(10, 6))
        col = input("Enter the column name for bar chart (e.g., 'book_title'): ")
        head_num = int(input("Enter number of top items to display (e.g., 5): "))
        top_books = data[col].value_counts().head(head_num)
        sns.barplot(
            x=top_books.values, 
            y=top_books.index, 
            hue=top_books.index, 
            palette='coolwarm', 
            legend=False )
        plt.title('Top 5 Most Borrowed Books')
        plt.xlabel('Borrow Count')
        plt.ylabel('Book Title')
        plt.tight_layout()
        plt.savefig('bar_chart.png')
        plt.show()
        print("Bar Chart saved!")
    except Exception as e:
        print(f"Error generating bar chart: {e}")
    
    
def plot_line_graph(data):
    try:
        plt.figure(figsize=(10, 6))
        col = input("Enter the date column name (e.g., 'transaction_date'): ")
        data[col] = pd.to_datetime(data[col], dayfirst=True)
        monthly_data = data.groupby(data[col].dt.month_name()).size()
        months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December']
        monthly_data = monthly_data.reindex(months_order).dropna()
        plt.plot(monthly_data.index, monthly_data.values, marker='o', color='teal', linewidth=2)
        plt.title(f'Monthly Trends for {col}')
        plt.xlabel('Month')
        plt.ylabel('Count')
        plt.legend([col])
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('line_graph.png')
        plt.show()
        print("Line Graph Chart saved!")
    except Exception as e:
        print(f"Error generating line graph: {e}")

def plot_pie_chart(data):
    try:
        plt.figure(figsize=(8, 8))
        col = input("Enter the category column for pie chart (e.g., 'genre'): ")
        head_num = int(input("Enter number of top categories to display (e.g., 8): "))
        genre_data = data[col].value_counts().head(head_num)
        plt.pie(genre_data, labels=genre_data.index, autopct='%1.1f%%', 
                startangle=140, colors=sns.color_palette('pastel')) 
        plt.title(f'Distribution of {col}')
        plt.legend(genre_data.index, title=col, loc='best')
        plt.tight_layout()
        plt.savefig('pie_chart.png')
        plt.show()
        print("Pie Chart saved!")
    except Exception as e:
        print(f"Error generating pie chart: {e}")
    
def plot_heatmap(data):
    try:
        plt.figure(figsize=(12, 6))
        print("For Heatmap, we need two columns (e.g., Day of Week and Month).")
        date_col = input("Enter the date column to extract Day/Month (e.g., 'transaction_date'): ")
        data[date_col] = pd.to_datetime(data[date_col], dayfirst=True)
        data['Temp_Day'] = data[date_col].dt.day_name()
        data['Temp_Month'] = data[date_col].dt.month_name()
        pivot = data.pivot_table(index='Temp_Day', columns='Temp_Month', aggfunc='size', fill_value=0)
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pivot = pivot.reindex(days_order)
        sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu')
        plt.title('Borrowing Activity Heatmap')
        plt.xlabel('Month')
        plt.ylabel('Day of Week')
        plt.tight_layout()
        plt.savefig('heatmap.png')
        plt.show()
        data.drop(['Temp_Day', 'Temp_Month'], axis=1, inplace=True)
        print("Heatmap Chart saved!")
    except Exception as e:
        print(f"Error generating heatmap: {e}")