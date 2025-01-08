# Variable to track if the code for A and B is running
is_code_a_running = False
is_code_b_running = False

def show_start_pattern():
    basic.show_leds("""
        # . # . #
        # . # . #
        # # # # #
        # . # . #
        # . # . #
    """)

def on_button_pressed_a():
    global is_code_a_running
    if is_code_a_running:
        # Stop the code for A and show the start pattern
        is_code_a_running = False
        basic.clear_screen()
        show_start_pattern()
    else:
        # Run the code for A
        is_code_a_running = True
        basic.clear_screen()
        led.plot(1, 0)
        basic.pause(200)
        led.plot(2, 0)
        basic.pause(200)
        led.plot(3, 0)
        basic.pause(200)
        led.plot(2, 1)
        basic.pause(200)
        led.plot(2, 2)
        basic.pause(200)
        led.plot(2, 3)
        basic.pause(200)
        led.plot(2, 4)
        basic.pause(200)
        led.plot(3, 4)
        basic.pause(200)
        led.plot(1, 4)
        basic.pause(1050)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.show_icon(IconNames.HEART)
        basic.pause(1050)
        basic.clear_screen()
        led.plot(0, 0)
        basic.pause(200)
        led.plot(0, 1)
        basic.pause(200)
        led.plot(0, 2)
        basic.pause(200)
        led.plot(0, 3)
        basic.pause(200)
        led.plot(0, 4)
        basic.pause(200)
        led.plot(4, 0)
        basic.pause(200)
        led.plot(4, 1)
        basic.pause(200)
        led.plot(4, 2)
        basic.pause(200)
        led.plot(4, 3)
        basic.pause(200)
        led.plot(4, 4)
        basic.pause(200)
        led.plot(0, 4)
        basic.pause(200)
        led.plot(3, 4)
        basic.pause(200)
        led.plot(1, 4)
        basic.pause(200)
        led.plot(2, 4)
        basic.pause(200)
        # After completing the code, reset back to the start pattern
        show_start_pattern()

def on_button_pressed_b():
    global is_code_b_running
    if is_code_b_running:
        # Stop the code for B and show the start pattern
        is_code_b_running = False
        basic.clear_screen()
        show_start_pattern()
    else:
        # Run the code for B
        is_code_b_running = True
        basic.clear_screen()
        basic.show_string("E")
        basic.pause(500)
        basic.show_string("S")
        basic.pause(500)
        basic.show_string("T")
        basic.pause(500)
        basic.show_string("E")
        basic.pause(500)
        basic.show_string("R")
        basic.pause(500)
        # After completing the code, reset back to the start pattern
        show_start_pattern()

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

show_start_pattern()  # Show the starting pattern initially
