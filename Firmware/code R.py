import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

keyboard.col_pins = (board.P0_29, board.P0_02, board.P0_03, board.P0_04)
keyboard.row_pins = (board.P0_09, board.P0_10, board.P1_13, board.P1_14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Enable Split in SLAVE mode
split = Split(
    split_type=SplitType.BLE,
    split_target_left=False,  # This is the right half
)
keyboard.modules.append(split)

keyboard.keymap = [
    [  # Layer 0
        KC.Y, KC.U, KC.I, KC.O,
        KC.H, KC.J, KC.K, KC.L,
        KC.B, KC.N, KC.M, KC.ENTER,
    ]
]

keyboard.go()
