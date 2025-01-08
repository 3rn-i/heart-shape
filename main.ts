input.onButtonPressed(Button.A, function () {
    if (is_code_a_running) {
        // Stop the code for A and show the start pattern
        is_code_a_running = false
        basic.clearScreen()
        show_start_pattern()
    } else {
        // Run the code for A
        is_code_a_running = true
        basic.clearScreen()
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
        basic.showIcon(IconNames.SmallHeart)
        basic.showIcon(IconNames.Heart)
        basic.showIcon(IconNames.SmallHeart)
        basic.showIcon(IconNames.Heart)
        basic.pause(1050)
        basic.clearScreen()
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
        basic.pause(2000)
        // After completing the code, reset back to the start pattern
        show_start_pattern()
    }
})
input.onButtonPressed(Button.B, function () {
    if (is_code_b_running) {
        // Stop the code for B and show the start pattern
        is_code_b_running = false
        basic.clearScreen()
        show_start_pattern()
    } else {
        // Run the code for B
        is_code_b_running = true
        basic.clearScreen()
        basic.showString("E")
        basic.pause(200)
        basic.showString("S")
        basic.pause(200)
        basic.showString("T")
        basic.pause(200)
        basic.showString("E")
        basic.pause(200)
        basic.showString("R")
        basic.pause(200)
        // After completing the code, reset back to the start pattern
        show_start_pattern()
    }
})
function show_start_pattern () {
    basic.showLeds(`
        # . # . #
        # . # . #
        # # # # #
        # . # . #
        # . # . #
        `)
}
let is_code_b_running = false
let is_code_a_running = false
show_start_pattern()
