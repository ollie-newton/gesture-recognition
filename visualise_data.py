import plotly.express as px

def line_plot(df):

    fig = px.line(df, y='ENV')

    for i in range(100, 10600, 100):
        fig.add_shape(type="line", x0=i, y0=0, x1=i, y1=6, line=dict(color="red", width=1))

    fig.show()

    
