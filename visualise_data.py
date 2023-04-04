import plotly.express as px

def line_plot(df):

    fig = px.line(df, y='ENV')

    for i in range(399, 500, 1):
        fig.add_shape(type="line", x0=i, y0=0, x1=i, y1=8, line=dict(color="red", width=1))

    fig.show()
  
