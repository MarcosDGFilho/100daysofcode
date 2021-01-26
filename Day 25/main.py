import turtle

screen = turtle.Screen()
screen.title('Brazil States game')
img = "bg.gif"
screen.addshape(img)
turtle.shape(img)

master_dict = []


def get_mouse_click_coor(x, y):
    print(x, y)
    master_dict.append(f"({x},{y})")


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
