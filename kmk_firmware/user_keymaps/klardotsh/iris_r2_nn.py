from kb import KMKKeyboard

from kmk.consts import UnicodeMode
from kmk.handlers.sequences import compile_unicode_string_sequences as cuss
from kmk.handlers.sequences import send_string
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()
layers_ext = Layers()
keyboard.debug_enabled = False
split = Split(split_type=SplitType.UART, debug_enabled=keyboard.debug_enabled)
keyboard.modules = [layers_ext, split]

keyboard.unicode_mode = UnicodeMode.LINUX
keyboard.tap_time = 750

emoticons = cuss({
    # Emojis
    'BEER': r'πΊ',
    'BEER_TOAST': r'π»',
    'FACE_CUTE_SMILE': r'π',
    'FACE_HEART_EYES': r'π',
    'FACE_JOY': r'π',
    'FACE_SWEAT_SMILE': r'π',
    'FACE_THINKING': r'π€',
    'FIRE': r'π₯',
    'FLAG_CA': r'π¨π¦',
    'FLAG_US': r'πΊπΈ',
    'HAND_CLAP': r'π',
    'HAND_HORNS': r'π€',
    'HAND_OK': r'π',
    'HAND_THUMB_DOWN': r'π',
    'HAND_THUMB_UP': r'π',
    'HAND_WAVE': r'π',
    'HEART': r'β€οΈ',
    'MAPLE_LEAF': r'π',
    'POOP': r'π©',
    'TADA': r'π',
    'SHRUG_EMOJI': r'π€·',

    # Emoticons, but fancier
    'ANGRY_TABLE_FLIP': r'(γΰ² ηΰ² )γε½‘β»ββ»',
    'CELEBRATORY_GLITTER': r'+ο½‘:.οΎγ½(Β΄βο½‘)οΎοΎ.:ο½‘+οΎοΎ+ο½‘:.οΎγ½(*Β΄β)οΎοΎ.:ο½‘+οΎ',
    'SHRUGGIE': r'Β―\_(γ)_/Β―',
    'TABLE_FLIP': r'(β―Β°β‘Β°οΌβ―οΈ΅ β»ββ»',
})

_______ = KC.TRNS
xxxxxxx = KC.NO

keyboard.keymap = [
    [
        KC.GESC, KC.N1,   KC.N2,   KC.N3,  KC.N4, KC.N5,                     KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
        KC.TAB,  KC.QUOT, KC.COMM, KC.DOT, KC.P,  KC.Y,                      KC.F,  KC.G,  KC.C,  KC.R,  KC.L,  KC.SLSH,
        KC.LGUI, KC.A,    KC.O,    KC.E,   KC.U,  KC.I,                      KC.D,  KC.H,  KC.T,  KC.N,  KC.S,  KC.ENTER,
        KC.LCTL, KC.SCLN, KC.Q,    KC.J,   KC.K,  KC.X,  KC.MO(2), KC.MO(1), KC.B,  KC.M,  KC.W,  KC.V,  KC.Z,  KC.LALT,
                                    KC.LEFT, KC.RGHT,    KC.LSFT,  KC.SPC,     KC.UP, KC.DOWN,
    ],
    [
        _______, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                   KC.F10, KC.F11, KC.F12, xxxxxxx, xxxxxxx, _______,
        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                   KC.F7,  KC.F8,  KC.F9,  xxxxxxx, xxxxxxx, KC.EQUAL,
        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.INS,                    KC.F4,  KC.F5,  KC.F6,  xxxxxxx, xxxxxxx, xxxxxxx,
        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.NO,   _______, KC.F1,  KC.F2,  KC.F3,  xxxxxxx, xxxxxxx, _______,
                                      KC.HOME, KC.END,        _______, xxxxxxx,    KC.PGUP, KC.PGDN,
    ],
    [
        KC.MUTE, xxxxxxx, xxxxxxx,  xxxxxxx, xxxxxxx, xxxxxxx,                   xxxxxxx, xxxxxxx, xxxxxxx, KC.LBRC,  KC.RBRC, KC.DEL,
        xxxxxxx, xxxxxxx, xxxxxxx,  xxxxxxx, xxxxxxx, xxxxxxx,                   xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,  xxxxxxx, KC.BSLS,
        KC.RGUI, xxxxxxx, xxxxxxx,  xxxxxxx, xxxxxxx, xxxxxxx,                   xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,  xxxxxxx, KC.MINS,
        xxxxxxx, xxxxxxx, xxxxxxx,  xxxxxxx, xxxxxxx, xxxxxxx, _______, KC.VOLU, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,  xxxxxxx, KC.RALT,
                                      KC.HOME, KC.END,         _______, KC.VOLD,    KC.PGUP, KC.PGDN,
    ],
]

if __name__ == '__main__':
    keyboard.go()
