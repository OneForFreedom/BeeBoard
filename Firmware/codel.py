import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

from kmk.modules.layers import Layers
from kmk.modules.ble import BLE
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

keyboard.col_pins = (board.P0_29, board.P0_02, board.P0_03, board.P0_04)  # Change these
keyboard.row_pins = (board.P0_09, board.P0_10, board.P1_13, board.P1_14)  # Change these
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

# Enable BLE
ble = BLE(name="NiceMaster")  # Can change name
keyboard.modules.append(ble)

# Enable Split
split = Split(
    split_type=SplitType.BLE,  # THIS IS THE MAGIC
    split_target_left=True,  # True = this is the left half
)
keyboard.modules.append(split)

keyboard.keymap = [
    [  # Layer 0
        KC.ESC, KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D, KC.F,
        KC.Z, KC.X, KC.C, KC.V,
    ]
]

keyboard.go()
