from caster.lib import control, navigation
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from caster.lib.dfplus.additions import IntegerRefST
from caster.lib import textformat

from dragonfly import Repeat, Function, Dictation
from dragonfly.actions.action_key import Key

_NEXUS = control.nexus()


def format_text_wrapper(cap, space, textnv):
    '''
    allows defaults for Capitalization and spacing
    that override the default capitalization and spacing
    in nav.py
    '''
    textformat.master_format_text(cap, space, textnv)


def wheel_scroll_up(nnavi500):
    navigation.wheel_scroll('up', nnavi500)


def wheel_scroll_down(nnavi500):
    navigation.wheel_scroll('down', nnavi500)


class CustomStuff(MergeRule):
    pronunciation = "custom stuff"
    mapping = {
        "open new file":
            R(Key("c-n"), rdescript="Custom Navigation: Open New File"),
        "Lefty":
            R(Key("home"), rdescript="Custom Navigation: Home Key"),
        "Lexi":
            R(Key("s-home"), rdescript="Custom Navigation: Home Key"),
        "Ricky":
            R(Key("end"), rdescript="Custom Navigation: End Key"),
        "Ricksy":
            R(Key("s-end"), rdescript="Custom Navigation: End Key"),
        "toggle tab":
            R(Key("c-tab"), rdescript="Next Tab"),
        "Ali":
            R(Key("c-a"), rdescript="Select All"),
        "back tab [<n>]":
            R(Key("s-tab"), rdescript="Previous Tab")*Repeat(extra="n"),
        "(windy | Wendy) Max":
            R(Key("w-up"), rdescript="Maximize Window"),
        "(windy | Wendy) lease [<n>]":
            R(Key("w-left"), rdescript="Window Left")*Repeat(extra="n"),
        "(windy | Wendy) ross [<n>]":
            R(Key("w-right"), rdescript="Window Right")*Repeat(extra="n"),
        "mahni lease [<n>]":
            R(Key("sw-left"), rdescript="Monitor Left")*Repeat(extra="n"),
        "manhi ross [<n>]":
            R(Key("sw-right"), rdescript="Monitor Right")*Repeat(extra="n"),
        "workace lease":
            R(Key("cw-left"), rdescript="Workspace Left"),
        "workace ross":
            R(Key("cw-right"), rdescript="Monitor Right"),
        "peach":
            R(Key("c-t"), rdescript="Open New Tab"),
        "snatch":
            R(Key("c-x"), rdescript="Open New Tab"),
        "junk [<nnavi50>]":
            R(Key("backspace/5:%(nnavi50)d"), rspec="clear", rdescript="Backspace"),
        "spunk [<nnavi50>]":
            R(Key("del/5"), rspec="deli", rdescript="Delete")*Repeat(extra="nnavi50"),
        "snipple":
            R(Key("s-home") + Key("del/5"), rspec="clear", rdescript="Backspace"),
        "(sniper | snipper)":
            R(Key("s-end") + Key("del/5"), rspec="clear", rdescript="Backspace"),
        "fish [<nnavi50>]":
            R(Key("c-right"), rspec="fish", rdescript="Jump word to the right")*
            Repeat(extra="nnavi50"),
        "fame [<nnavi50>]":
            R(Key("c-left"), rspec="fame", rdescript="Jump word to the Left")*
            Repeat(extra="nnavi50"),
        "scrish [<nnavi50>]":
            R(Key("cs-right"), rspec="scrish", rdescript="Select word to the right")*
            Repeat(extra="nnavi50"),
        "scram [<nnavi50>]":
            R(Key("cs-left"), rspec="scram", rdescript="Select a word to the left")*
            Repeat(extra="nnavi50"),
        "shreep [<nnavi50>]":
            R(Key("s-up"), rspec="shreeep", rdescript="Select a line up")*
            Repeat(extra="nnavi50"),
        "shroom [<nnavi50>]":
            R(Key("s-down"), rspec="shroom", rdescript="Select a line down")*
            Repeat(extra="nnavi50"),
        "(Kate | Kite) [<nnavi50>]":
            R(Key("c-del"), rspec="clear", rdescript="Backspace")*Repeat(extra="nnavi50"),
        "trough [<nnavi50>]":
            R(Key("c-backspace"), rspec="clear", rdescript="Backspace")*
            Repeat(extra="nnavi50"),
        "totch":
            R(Key("c-w/20"), rdescript="Close Tab"),
        "dizzle [<n>]":
            R(Key("c-z"), rdescript="Undo")*Repeat(extra="n"),
        "rizzle [<n>]":
            R(Key("c-y"), rdescript="Redo")*Repeat(extra="n"),
        'duke':
            R(Function(navigation.left_click, nexus=_NEXUS)*Repeat(2),
              rdescript="Mouse: Double Click"),
        "marco":
            R(Key("c-f"), rdescript="Find"),
        "cram <textnv>":
            R(Function(format_text_wrapper, cpa=3, space=1), rdescript="camelCase"),
        "smash <textnv>":
            R(Function(format_text_wrapper, cap=5, space=1),
              rdescript="lowercasenospaces"),
        "squash <textnv>":
            R(Function(format_text_wrapper, cap=5, space=0),
              rdescript="lowercase with spaces"),
        "snake <textnv>":
            R(Function(format_text_wrapper, cap=5, space=3), rdescript="snake_case"),
        "Yeller <textnv>":
            R(Function(format_text_wrapper, cap=1, space=0), rdescript="UPPERCASE"),
        "spine <textnv>":
            R(Function(format_text_wrapper, cap=0, space=2),
              rdescript="spinal-case-text"),
        "tridal <textnv>":
            R(Function(format_text_wrapper, cap=2, space=0), rdescript="Title Case"),
        "Champ <textnv>":
            R(Function(format_text_wrapper, cap=4, space=0),
              rdescript="Capitalize first word"),
        "format <textnv>":
            R(Function(textformat.prior_text_format), rdescript="Last Text Format"),
        "scrodge [<nnavi50>]":
            R(Function(wheel_scroll_down), rdescript="Wheel Scroll"),
        "scroop [<nnavi50>]":
            R(Function(wheel_scroll_up), rdescript="Wheel Scroll"),
        'chiff | Jeff':
            R(Function(navigation.left_click, nexus=_NEXUS),
              rdescript="Mouse: Left Click"),
    }
    extras = [
        IntegerRefST("n", 1, 10),
        IntegerRefST("nnavi50", 1, 50),
        Dictation("textnv"),
    ]
    defaults = {"n": 1, "nnavi50": 1, "textnv": ""}


control.nexus().merger.add_global_rule(CustomStuff())
