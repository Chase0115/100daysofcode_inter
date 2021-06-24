import colorgram

color_list = []
colors = colorgram.extract('img.jpg', 20)
for _ in range(19):
    new_color = colors[_]
    r = new_color.rgb.r
    g = new_color.rgb.g
    b = new_color.rgb.b
    color_tuple = (r, g, b)
    color_list.append(color_tuple)

print(color_list)