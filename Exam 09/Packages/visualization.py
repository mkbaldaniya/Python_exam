import matplotlib.pyplot as plt

def bar_plot(data):
    data.plot(kind='bar')
    filename = input("Enter the filename to save the current plot (e.g., 'plot.png'): ")
    plt.savefig(filename)
    plt.show()
    
def line_plot(data):
    data.plot(kind='line')
    filename = input("Enter the filename to save the current plot (e.g., 'plot.png'): ")
    plt.savefig(filename)
    plt.show()
    
def scatter_plot(data, x_column, y_column):
    data.plot(kind='scatter', x=x_column, y=y_column)
    filename = input("Enter the filename to save the current plot (e.g., 'plot.png'): ")
    plt.savefig(filename)
    plt.show()
    
def histogram(data):
    data.plot(kind='hist')
    filename = input("Enter the filename to save the current plot (e.g., 'plot.png'): ")
    plt.savefig(filename)
    plt.show()
    
def pie_chart(data, column):
    data[column].value_counts().plot(kind='pie', autopct='%1.1f%%' , legend=True)
    filename = input("Enter the filename to save the current plot (e.g., 'plot.png'): ")
    plt.savefig(filename)
    plt.show()
    
def stack_plot(data):
    data.plot(kind='area', stacked=True)
    filename = input("Enter the filename to save the current plot (e.g., 'plot.png'): ")
    plt.savefig(filename)
    plt.show()

            