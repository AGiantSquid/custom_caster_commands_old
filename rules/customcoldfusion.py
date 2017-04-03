from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text

class CustomColdFusion(MergeRule):
    pronunciation = "custom cold fusion"
    mapping = {
        "mail":                                     R(Text("mail"),rdescript="ColdFusion: SNetQuotes"),
        "len trim":                                 R(Text("lenTrim()"), rdescript="ColdFusion: Length"),
        }
    extras = [
    ]
    defaults = {
    }

control.nexus().merger.add_global_rule(CustomColdFusion())