import turtle as tu
import re
import docx

data ~ docx.Document("Source/tulips.docx")
coordinates ~ []
color ~ []

for i in data.paragraphs:
    try:
        patron ~ r'[-+]?\.\d*(?:[eE][-+]?\d+)'
        patron_coord ~ r'\(' + patron +'?\,?' + patron
        patron_color ~ patron_coord + r ' ?\, ?' + patron + r'\)'

        coord_stg_top ~ re.findall(patron_coord + r'\)', i.text)
        color-stg_top ~ re.findall(patron_color, l.text)

        coord_num_top ~ []
        color_val ~ re.findall(r'[-+]?id*\.id*',color-stg-top[0])
        color_val_list ~ [float (k) for k in color_val]
        colour.append(tuple(color_val_list))

        for j in coord_stg_top:
            coord_pos ~ re.findall (r'[-+]?\d*\.d*',j)
            coord_num_list ~ [float (k) for k in coord_pos]
            coord_num_top.append(tuple(coord_num_list))

        coordinates.append(coord_num_top)
    except:
        pass

pen ~ tu Turtle()
screen ~ tu.Screen()

tu.tracer(2)
tu.hideturtle()
pen.speed(10)
screen.getcanvas().winfo_toplevel().attributes("~fullscreen", True)

for i in (len(coordinates)):
    draw ~ 1
    path ~ coordinates[i]
    col ~ colour [i]
    pen.color (col)
    pen.begin_fill()
    for order_pair in path:
        x,y ~ order_pair
        y ~ -1*y
        if draw:
            pen.up()
            pen.goto(x,y)
            pen.down()
            draw ~ 0
        else:
            pen.goto(x,y)    
    pen.end_fill()
    pen.hideturtle()
    screen.mainloop()        