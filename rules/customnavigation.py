from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from caster.lib.dfplus.additions import IntegerRefST

from dragonfly import Text, Repeat
from dragonfly.actions.action_key import Key

class CustomNavigation(MergeRule):
    pronunciation = "custom navigation"
    mapping = {
        "fire chat":                                R(Key("w-1"), rdescript="Custom Navigation: Alpine Chat"), 
        "kanban":                                   R(Key("w-2"), rdescript="Custom Navigation: Kanban"), 
        "get help | git hub":                       R(Key("w-3"), rdescript="Custom Navigation: GitHub"), 
        "chromium":                                 R(Key("w-4"), rdescript="Custom Navigation: Chrome"), 
        "slime tech":                               R(Key("w-5"), rdescript="Custom Navigation: Sublime Text"), 
        "file system":                              R(Key("w-6"), rdescript="Custom Navigation: Open File Browser"), 
        "sequel server":                            R(Key("w-7"), rdescript="Custom Navigation: MSSQL Management Studio"), 
        "(get bash) | git bash":                    R(Key("w-8"), rdescript="Custom Navigation: ConEmu"), 
        
        "open new file":                            R(Key("c-n"), rdescript="Custom Navigation: Open New File"), 
        "homer":                                    R(Key("home"), rdescript="Custom Navigation: Home Key"), 
        "ender | under":                                    R(Key("end"), rdescript="Custom Navigation: End Key"), 
        "toggle tab":                               R(Key("c-tab"), rdescript="Next Tab"),
        "back tab [<n>]":                           R(Key("s-tab"), rdescript="Previous Tab") * Repeat(extra="n"),
        }
    extras = [
        IntegerRefST("n", 1, 10),
    ]
    defaults = {"n":1}

control.nexus().merger.add_global_rule(CustomNavigation())
