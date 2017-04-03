from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text
from dragonfly.actions.action_key import Key

class CustomNavigation(MergeRule):
    pronunciation = "custom navigation"
    mapping = {
        "pine chat":                                R(Key("w-1"), rdescript="Maximize Window"), 
        "kanban":                                   R(Key("w-2"), rdescript="Maximize Window"), 
        "chromium":                                 R(Key("w-4"), rdescript="Maximize Window"), 
        "slime text":                               R(Key("w-5"), rdescript="Maximize Window"), 
        "file system":                              R(Key("w-6"), rdescript="Maximize Window"), 
        "(get bash) | git bash":                    R(Key("w-8"), rdescript="Maximize Window"), 
        "(data grip) | (datagram) | (data group)":  R(Key("w-7"), rdescript="Maximize Window"), 
        
        "open new file":                            R(Key("c-n"), rdescript="Maximize Window"), 
        "homer":                                    R(Key("home"), rdescript="Maximize Window"), 
        "ender":                                    R(Key("end"), rdescript="Maximize Window"), 
        "open new file":                            R(Key("c-n"), rdescript="Maximize Window"),
        }
    extras = [
    ]
    defaults = {
    }

control.nexus().merger.add_global_rule(CustomNavigation())