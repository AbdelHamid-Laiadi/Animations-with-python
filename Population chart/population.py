# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:29:10 2023

@author: HAMID
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

df = pd.read_csv('city_populations.csv', usecols=['name', 'group', 'year', 'value'])
dff = df[df['year'].eq(2018)].sort_values(by='value', ascending=True).head(10)
colors = dict(zip(
    ['India','Europe','Asia','Latin America','Middle East','North America','Africa'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50']
))

group_lk = df.set_index('name')['group'].to_dict()
fig, ax = plt.subplots(figsize=(15, 8))

def update(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']], edgecolor='black')
    dx = dff['value'].max() / 200
    ax.set_xlim([0, 40000])
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-0.25, group_lk[name], size=10, color='#444444', ha='right',
                va='baseline')
        ax.text(value+dx, i, f'{value:,.0f}',  size=14, ha='left',  va='center')
    # for beautifying
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='minor', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.1, 'The most populous cities in the world from 1968 to 2018',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    plt.box(False)

ani = animation.FuncAnimation(fig, update, frames=range(1968, 2019))
ani.save('animation_drawing2.gif', writer='imagemagick', fps=20)