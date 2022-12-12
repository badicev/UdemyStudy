"""World Geodetic System (WGS 84) to Web Mercator"""
import math
# x: Web Mercator coordinate
# y: Web Mercator coordinate
# longitude: WGS 84 coordinate
# latitude: WGS 84 coordinate


from tkinter import *
from math import pi, log, tan


def wgs84_to_webmercator():
    wgs84_x = float(wgs84_input_x.get())
    wgs84_y = float(wgs84_input_y.get())

    # 31.347
    # 40.189

    mercator_result_x = wgs84_x * (20037508.34 / 180)
    mercator_result_y = log(tan((90 + wgs84_y) * math.pi / 360)) / (math.pi / 180)
    mercator_result_y = mercator_result_y * (20037508.34 / 180)

    mercator_result_label_x.config(text=f"{mercator_result_x}")
    mercator_result_label_y.config(text=f"{mercator_result_y}")


window = Tk()
window.title("WGS 84 to Web Mercator converter")
window.config(padx=20, pady=20)

wgs84_input_x = Entry(width=10)
wgs84_input_x.grid(column=1, row=0)

wgs84_input_y = Entry(width=10)
wgs84_input_y.grid(column=2, row=0)

wgs84_label = Label(text="WGS 84 Coordinates")
wgs84_label.grid(column=3, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

mercator_result_label_x = Label(text="0")
mercator_result_label_x.grid(column=1, row=1)

mercator_result_label_y = Label(text="0")
mercator_result_label_y.grid(column=2, row=1)

mercator_label = Label(text="Web Mercator")
mercator_label.grid(column=3, row=1)

calculate_button = Button(text="Calculate", command=wgs84_to_webmercator)
calculate_button.grid(column=1, row=2)
calculate_button.config(borderwidth=10)

window.mainloop()
