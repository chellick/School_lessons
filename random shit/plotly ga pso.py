import plotly.express as px
import plotly.io as pio

a = ['Mod. GA', 'GA', 'Mod. PSO', 'PSO']
b = [160000.0 , 153840.86554106677, 156990.63850500656, 145189.04029656053]
fig = px.bar(x = a, y = b)



fig.show()
