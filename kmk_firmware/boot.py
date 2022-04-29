

import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

# This is from the base kmk boot.py
supervisor.set_next_stack_limit(4096 + 4096)

# If this key is held during boot, don't run the code which hides the storage and disables serial
# To use another key just count its row and column and use those pins
# You can also use any other pins not already used in the matrix and make a button just for accesing your storage
row = digitalio.DigitalInOut(board.GP0)
col = digitalio.DigitalInOut(board.GP8)

# TODO: If your diode orientation is ROW2COL, then make row the output and col the input
row.switch_to_output(value=True)
col.switch_to_input(pull=digitalio.Pull.DOWN)

if not col.value:
    # storage.disable_usb_drive()
    # Equivalent to usb_cdc.enable(console=False, data=False)
    # usb_cdc.disable()
    # usb_hid.enable(boot_device=1)
    print("Detected Button Press")

row.deinit()
col.deinit()
