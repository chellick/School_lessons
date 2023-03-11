# # import math
# # def function(x1, y1):
# #     return -((x1 ** 2) + (y1 ** 2))
# # 
# # def fitness_particle(particle):
# #     best_p_position = (-math.inf, -math.inf)
# #     for k in range(len(particle)):
# #         if function(particle[k][0], particle[k][1]) > function(best_p_position[0], best_p_position[1]):
# #             best_p_position = particle[k]
# #     return best_p_position
# # 
# # def fitnes_swarm(swarm):  # лучшая позиция точки
# #     best_s_position = -math.inf
# #     for particle in swarm:
# #         for r in particle:
# #             if function(r[0], r[1]) > best_s_position:
# #                 best_s_position = function(r[0], r[1])
# #     return best_s_position
# # 
# # population = [[(1, 2), (3, 4)]]
# # for i in range(len(population)):
# #     print(fitness_particle(population[i]))
# # print(fitnes_swarm(population))
# # 
# 
# import plotly.graph_objects as go
# 
# import numpy as np
# 
# # Generate curve data
# t = np.linspace(-1, 1, 100)
# x = t + t ** 2
# y = t - t ** 2
# xm = np.min(x) - 1.5
# xM = np.max(x) + 1.5
# ym = np.min(y) - 1.5
# yM = np.max(y) + 1.5
# N = 50
# s = np.linspace(-1, 1, N)
# xx = s + s ** 2
# yy = s - s ** 2
# 
# 
# # Create figure
# fig = go.Figure(
#     data=[go.Scatter(x=x, y=y,
#                      mode="lines",
#                      line=dict(width=2, color="blue")),
#           go.Scatter(x=x, y=y,
#                      mode="lines",
#                      line=dict(width=2, color="blue"))],
#     layout=go.Layout(
#         xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
#         yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
#         title_text="Kinematic Generation of a Planar Curve", hovermode="closest",
#         updatemenus=[dict(type="buttons",
#                           buttons=[dict(label="Play",
#                                         method="animate",
#                                         args=[None])])]),
#     frames=[go.Frame(
#         data=[go.Scatter(
#             x=[xx[k]],
#             y=[yy[k]],
#             mode="markers",
#             marker=dict(color="red", size=10))])
# 
#         for k in range(N)]
# )
# 
# fig.show()

import math


a, b = map(int, input().split())
n = 4
k = a + b
C = int(math.factorial(k)) / int((math.factorial(n) * math.factorial(k - n)))
print(int(C))

