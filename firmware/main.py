from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.oled import Oled, OledData

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(EncoderHandler())
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = ("GP0", "GP1", "GP2", "GP3", "GP4", "GP5", "GP6", "GP7", "GP8", "GP9", "GP10", "GP11", "GP12")
keyboard.row_pins = ("GP13", "GP14", "GP15", "GP16", "GP17", "GP18")
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

BASE = (
    KC.ESC,   KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
    KC.TAB,   KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ENT,
    KC.LSFT,  KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.RSFT,
    KC.LCTL,  KC.LALT, KC.LGUI, KC.SPC, KC.RGUI, KC.RALT, KC.RCTL
)

FN = (
    KC.GESC,  KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.DEL,
    KC.TRNS,  KC.MPLY, KC.MPRV, KC.MNXT, KC.VOLD, KC.VOLU, KC.BRIU, KC.BRID, KC.MUTE, KC.TRNS, KC.TRNS,
    KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
)

keyboard.keymap = [BASE, FN]

keyboard.keys[KC.F1] = KC.BRID 
keyboard.keys[KC.F2] = KC.BRIU 
keyboard.keys[KC.F3] = KC.MCTL 
keyboard.keys[KC.F4] = KC.SLCK 
keyboard.keys[KC.F5] = KC.DICT  
keyboard.keys[KC.F6] = KC.DND   
keyboard.keys[KC.F7] = KC.MPRV  
keyboard.keys[KC.F8] = KC.MPLY  
keyboard.keys[KC.F9] = KC.MNXT  
keyboard.keys[KC.F10] = KC.MUTE 
keyboard.keys[KC.F11] = KC.VOLD 
keyboard.keys[KC.F12] = KC.VOLU

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (("GP20", "GP21"),)  
encoder_handler.map = ((KC.MNXT, KC.MPRV),)  
keyboard.keymap.append([KC.MPLY])  

oled = Oled()
oled.display(oled_data=OledData())
keyboard.modules.append(oled)

oled_data = OledData()
def update_oled():
    oled_data.update("Media: Playing\nTime: 00:30")

oled.display(oled_data=oled_data)

if __name__ == "__main__":
    keyboard.go()