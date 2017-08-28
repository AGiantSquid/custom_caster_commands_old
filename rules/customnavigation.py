from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from caster.lib.dfplus.additions import IntegerRefST

from dragonfly import Text, Repeat
from dragonfly.actions.action_key import Key

class CustomNavigation(MergeRule):
    pronunciation = "custom navigation"
    mapping = {
        "open new file":                            R(Key("c-n"), rdescript="Maximize Window"), 
        "homer":                                    R(Key("home"), rdescript="Maximize Window"), 
        "ender":                                    R(Key("end"), rdescript="Maximize Window"), 
        "open new file":                            R(Key("c-n"), rdescript="Maximize Window"),
        "toggle tab":                               R(Key("c-tab"), rdescript="Next Tab"),
        "back tab [<n>]":                           R(Key("cs-tab"), rdescript="Previous Tab") * Repeat(extra="n"),
        }
    extras = [
        IntegerRefST("n", 1, 10),
    ]
    defaults = {"n":1}

control.nexus().merger.add_global_rule(CustomNavigation())