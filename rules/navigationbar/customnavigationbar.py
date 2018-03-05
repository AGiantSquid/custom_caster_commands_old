from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text
from dragonfly.actions.action_key import Key

class CustomNavigationBar(MergeRule):
    pronunciation = "custom navigation bar"
    mapping = {
        "chromium":                                 R(Key("w-1"), rdescript="Maximize Window"), 
        "Firefox":                                  R(Key("w-2"), rdescript="Maximize Window"), 
        "slime tech":                               R(Key("w-3"), rdescript="Maximize Window"), 
        "file system":                              R(Key("w-4"), rdescript="Maximize Window"), 
        "(get bash) | git bash":                    R(Key("w-5"), rdescript="Maximize Window"), 
        "Saponify":                                 R(Key("w-9"), rdescript="Maximize Window"),         
    }
    extras = []
    defaults = {}

control.nexus().merger.add_global_rule(CustomNavigationBar())