from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text

class Alpine(MergeRule):
    pronunciation = "alpine"
    mapping = {
        "alpine":                                   R(Text(" Alpine "),rdescript="ColdFusion: SNetQuotes"),
        "alpine home air":                          R(Text(" Alpine Home Air "),rdescript="ColdFusion: SNetQuotes"),
        "partner net | partner that":               R(Text(" Partnernet "),rdescript="ColdFusion: SNetQuotes"),
        "easy HVAC":                                R(Text(" EasyHVAC "),rdescript="ColdFusion: SNetQuotes"),
        "as net":					                R(Text("SNet"), rdescript="ColdFusion: SNet"),
        "eric":                                     R(Text(" Erick "),rdescript="ColdFusion: SNetQuotes"),
        "many split":                               R(Text(" mini split "),rdescript="ColdFusion: SNetQuotes"),
        }
    extras = [
    ]
    defaults = {
    }

control.nexus().merger.add_global_rule(Alpine())