import plotly.express as plotly_total
import plotly.graph_objs as go_objects

plot = plotly_total.pie(labels=['D1','D2','D3'], values=[1.4,12,6])
plot.show()