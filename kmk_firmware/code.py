print("Starting")

import board
import busio 
import time
import random
from digitalio import DigitalInOut, Direction, Pull

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation


from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence,send_string
from kmk.modules.tapdance import TapDance
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode
from kmk.extensions.lock_status import LockStatus

from ledDriver import LEDDriver
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import usb_hid

kbd = Keyboard(usb_hid.devices)

locks = LockStatus()

i2c = busio.I2C(scl=board.GP21,sda=board.GP20)
leds = LEDDriver(10,i2c)
leds.reset()
leds.enable()
for i in range(0,10):
    leds.set_brightness(0.4,i)

for i in range(0,10):
    leds.set_output(i,True)
    time.sleep(0.05)
leds.set_output(0,True)


#Define Keyboard
keyboard = KMKKeyboard()
#Add required modules
tapdance = TapDance()
tapdance.tap_time=250


keyboard.modules.append(tapdance)
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())

keyboard.extensions.append(locks)

trackball = Trackball(i2c, mode=TrackballMode.MOUSE_MODE)
keyboard.modules.append(trackball)


# Keyboard Hardware settings
keyboard.col_pins = (board.GP8,board.GP9,board.GP10,board.GP11,board.GP12)
keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

#Custom Keys
#Send the clear string to clear a terminal
STR_CLEAR = send_string("clear")
KC_CLEAR = simple_key_sequence((KC.ENTER,STR_CLEAR,KC.ENTER))

#Keys requiring Modifiers to be help
KC_PLUS = KC.LSFT(KC.EQUAL)
KC_ASTERISK = KC.LSFT(KC.N8)
KC_COPY = KC.LCTL(KC.C)
KC_PASTE = KC.LCTL(KC.V)
KC_CUT = KC.LCTL(KC.X)

#Tap dance keys
CLEAR_DEL_TD = KC.TD(KC.DELETE,KC_CLEAR)
ENTER_EQUALS_TD = KC.TD(KC.ENTER,KC.EQUAL)
MOUSE_SCROLL_TD = KC.TD(KC.MW_DN,KC.MW_UP)
CPY_CUT_TD = KC.TD(KC_COPY,KC_CUT)
COMMENT_TD = KC.TD(KC.DOT,KC.BSLASH,KC.HASH)

LAYERS = [KC.DF(0), KC.DF(1), KC.DF(2)]

keyboard.keymap = [
    # Numpadlayer
    [
        KC.BSPC,         CLEAR_DEL_TD,    KC.SPACE,            KC_PLUS,             LAYERS[1],
        KC.N7,           KC.N8,           KC.N9,               KC.MINUS,            KC.LBRACKET,
        KC.N4,           KC.N5,           KC.N6,               KC_ASTERISK,         KC.RBRACKET,
        KC.N1,           KC.N2,           KC.N3,               KC.SLSH,             KC.COMMA,
        KC.N0,           COMMENT_TD,      KC.LEFT_PAREN,       KC.RIGHT_PAREN,      ENTER_EQUALS_TD, 
    ],

    # Mouselayer
    [
        KC.MB_LMB,      KC.MB_MMB,        KC.MB_RMB,           MOUSE_SCROLL_TD,     KC.TD(LAYERS[2],LAYERS[0]),
        KC.MS_LT,       KC.MS_DN,         KC.MS_UP,            KC.MS_RT,            KC.LSFT,
        CPY_CUT_TD,     KC.PGUP,          KC.UP,               KC.PGDOWN,           KC_PASTE,
        KC.NOP,         KC.LEFT,          KC.DOWN,             KC.RIGHT,            KC.NOP,
        KC.NOP,         KC.NOP,           KC.NOP,              KC.NOP,              KC.ENTER,
    ],

    [
        KC.MUTE,        KC.NOP,           KC.NOP,               KC.NOP,             KC.TD(LAYERS[0],LAYERS[1]),
	KC.VOLD,	KC.NOP,		  KC.NOP,		KC.NOP,		    KC.NOP,	
	KC.VOLU,	KC.NOP,		  KC.NOP,		KC.NOP,		    KC.NOP,	
	KC.MPLY,	KC.NOP,		  KC.NOP,		KC.NOP,		    KC.NOP,	
	KC.CAPS,	KC.NOP,		  KC.NOP,		KC.NOP,		    KC.NOP,	
    ],
]


def change_layer(key, keyboard, *args):
    current_layer = keyboard.active_layers[0]
    leds.set_output(current_layer,True)

    r = random.getrandbits(8)
    g = random.getrandbits(8)
    b = random.getrandbits(8)
    w = random.getrandbits(8)

    trackball.set_rgbw(r,g,b,w)



KC.CAPS.after_press_handler(get_caps_stat)

if __name__ == '__main__':
    keyboard.go()
