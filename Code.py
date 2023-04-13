#Filled Scattermapbox Trace
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [120, 115, 115, 120], lat = [-31, -31, -35, -35],
    marker = { 'size': 10, 'color': "orange" }))

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 120, 'lat': -30},
        'zoom': 4},
    showlegend = False)

fig.show()


#Multiple Filled Areas with a Scattermapbox trace
import plotly.graph_objects as go
fig = go.Figure(go.Scattermapbox(
    mode = "lines", fill = "toself",
    lon = [120, 115, 115, 120, 120, None, 153, 147, 147, 153, 153, None, 155, 150, 150, 155, 155],
    lat = [-31, -31, -35, -35, -31,    None, -32, -32, -36, -36, -32, None, -25, -25, -29, -29, -25]))
fig.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 120, 'lat': -30}, 'zoom': 4},
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig.show()



