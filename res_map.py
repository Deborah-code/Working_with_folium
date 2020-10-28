# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:21:13 2020

@author: Debs
"""

import folium, pandas, branca


data = pandas.read_csv('Restaurants.txt')
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])
link = list(data["Link"])

map = folium.Map(location = [6.5244, 3.3792], tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")

#zip function iterates through both list simultaneously
for lt, ln, nm, li in zip(lat, lon, name, link):
    test = folium.Html('<a href = %s target ="_blank">%s</a>' % (li,nm), script = True)
    iframe = branca.element.IFrame(html=test, width=160, height=50)
    popup = folium.Popup(iframe, parse_html=True)
    fg.add_child(folium.Marker(location = [lt, ln], popup = popup,
                            icon = folium.Icon(color= 'red')))

map.add_child(fg)
map.save('Restaurant.html')