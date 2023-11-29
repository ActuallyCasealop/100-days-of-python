import colorgram

color = colorgram.extract('Day 18 - Turtle & the Graphical User Interface (GUI)\damien_hirst_color_pallet.webp',20)

color_pallet = []
for i in color:
    color_pallet.append(i.rgb)

n_color_pallet = []
for i in color_pallet:
    temp_color = (i.r,i.g,i.b)
    n_color_pallet.append(temp_color)

print(n_color_pallet)
