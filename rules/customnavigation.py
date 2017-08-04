from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from caster.lib.dfplus.additions import IntegerRefST

from dragonfly import Text, Repeat
from dragonfly.actions.action_key import Key

class CustomNavigation(MergeRule):
    pronunciation = "custom navigation"
    mapping = {
        "pine chat":                                R(Key("w-1"), rdescript="Maximize Window"), 
        "kanban":                                   R(Key("w-2"), rdescript="Maximize Window"), 
        "get help | git hub":                                   R(Key("w-3"), rdescript="Maximize Window"), 
        "chromium":                                 R(Key("w-4"), rdescript="Maximize Window"), 
        "slime tech":                               R(Key("w-5"), rdescript="Maximize Window"), 
        "file system":                              R(Key("w-6"), rdescript="Maximize Window"), 
        "sequel server":                               R(Key("w-7"), rdescript="Maximize Window"), 
        "(get bash) | git bash":                    R(Key("w-8"), rdescript="Maximize Window"), 
        
        "open new file":                            R(Key("c-n"), rdescript="Maximize Window"), 
        "homer":                                    R(Key("home"), rdescript="Maximize Window"), 
        "ender":                                    R(Key("end"), rdescript="Maximize Window"), 
        "open new file":                            R(Key("c-n"), rdescript="Maximize Window"),
        "toggle tab":                               R(Key("c-tab"), rdescript="Next Tab"),
        "back tab [<n>]":                          R(Key("cs-tab"), rdescript="Previous Tab") * Repeat(extra="n"),
        }
    extras = [
        IntegerRefST("n", 1, 10),
    ]
    defaults = {"n":1}

control.nexus().merger.add_global_rule(CustomNavigation())