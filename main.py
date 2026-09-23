def on_forever():
    basic.show_number(1 + 2)
    basic.pause(100)
    basic.show_number(0)
basic.forever(on_forever)
