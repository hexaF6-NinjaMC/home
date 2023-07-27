import os
clear = lambda:os.system("cls")
clear()

import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    # Draw everything from farthest away to closest.
    draw_sky(canvas, scene_left, scene_top, scene_right, 201) # What everything is set against
    draw_clouds(canvas, 10, scene_top, scene_right, 10, 10, 5) # Layer 1, biggest puffs
    draw_clouds(canvas, 10, scene_top, scene_right, 10, 50, 4) # Layer 2
    draw_clouds(canvas, 10, scene_top, scene_right, 10, 75, 3.5) # Layer 3, smallest puffs

    draw_sea(canvas, scene_left, 201, scene_right, scene_bottom)
    draw_fish(canvas, scene_left, 201, scene_right, scene_bottom, 50, 201, 2, position="background") # Fish are behind vegetation.
    draw_sea_vegetation(canvas, scene_left, 220, scene_right, scene_bottom, 15, 51)
    draw_fish(canvas, scene_left, 201, scene_right, scene_bottom, 150, 201, 4, position="foreground") # Fish are in front of vegetation.

    draw_ground(canvas, scene_left, 385, scene_right, scene_bottom)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_sky (canvas, left, top, right, bottom):
    for i in range(top, bottom):
        canvas.create_line(left, i, right, i, fill="deepSkyBlue")

def draw_clouds(canvas, left, top, right, bottom, distance_from_edge, scale):
    # These variables keep the cloud's shape, but affected relative to the scale (size of the puff).
    x_one = 0
    y_one = 0
    x_two = 30 * scale
    y_two = 5 * scale

    for i in range(left, right, 100):
        for j in range(top, bottom):
                canvas.create_oval(x_one + i + distance_from_edge, y_one + j + distance_from_edge, x_two + i + distance_from_edge, y_two * scale + j + distance_from_edge, fill="gray89", outline="snow2",)

def draw_sea(canvas, left, top, right, bottom):
    for i in range(top, bottom):
        canvas.create_line(left, i, right, i, fill="navyBlue")

def draw_fish(canvas, left, top, right, bottom, distance_from_edge, spacing, scale, position):
    # These variables keep the fish's shape, but affected relative to the scale (size of the fish).
    body_x_one = 0
    body_y_one = 0
    body_x_two = 20 * scale
    body_y_two = 10 * scale
    tail_x_vert = body_x_two + 20
    tail_y_one = body_y_one
    tail_y_two = body_y_two
    tail_x_cent = (body_x_one + body_x_two) / 2
    tail_y_cent = (body_y_one + body_y_two) / 2

    if position == "background":
        # Draw the fish behind the vegetation
        for i in range(left, right, 300):
            for j in range(top, bottom, spacing):
                # Draw the body of the fish
                canvas.create_oval(body_x_one + i + distance_from_edge, body_y_one + j + distance_from_edge, body_x_two + i + distance_from_edge, body_y_two + j + distance_from_edge, fill="orange", outline="orange")
                # Draw the tail of the fish
                canvas.create_polygon(tail_x_cent + i + distance_from_edge, tail_y_cent + j + distance_from_edge, tail_x_vert + i + distance_from_edge, tail_y_one + j + distance_from_edge, tail_x_vert + i + distance_from_edge, tail_y_two + j + distance_from_edge, fill="orange", outline="orange")
    
    if position == "foreground":
        # Draw the fish in front of the vegetation, but bigger
        for i in range(left, right, 400):
            for j in range(top, bottom, spacing):
                # Draw the body of the fish
                canvas.create_oval(body_x_one + i + distance_from_edge, body_y_one + j + distance_from_edge, body_x_two + i + distance_from_edge, body_y_two + j + distance_from_edge, fill="orange", outline="orange")
                # Draw the tail of the fish
                canvas.create_polygon(tail_x_cent + i + distance_from_edge, tail_y_cent + j + distance_from_edge, tail_x_vert + i + distance_from_edge, tail_y_one + j + distance_from_edge, tail_x_vert + i + distance_from_edge, tail_y_two + j + distance_from_edge, fill="orange", outline="orange")

def draw_sea_vegetation(canvas, element_left, element_top, element_right, element_bottom, distance_from_edge, spacing):
    for i in range(element_left, element_right, spacing):
        for j in range(element_top, element_bottom, 15):
            canvas.create_arc(i + distance_from_edge, j + distance_from_edge, i + 10 + distance_from_edge, j + 60 + distance_from_edge, fill="green1", outline="green2", style=tk.ARC, width=2)

def draw_ground(canvas, element_left, element_top, element_right, element_bottom):
    for i in range(element_top, element_bottom):
        canvas.create_line(element_left, i, element_right, i, fill="lightGoldenrod1")

# Call the main function so that
# this program will start executing.
main()