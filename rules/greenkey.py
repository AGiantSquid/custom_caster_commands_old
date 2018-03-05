from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text

class CustomVocabulary(MergeRule):
    pronunciation = "Green key"
    mapping = {
        "Ashley at Green key":                                  	R(Text("ashley@greenkeytech.com"),rdescript="CustomVocabulary: Shultz"),
        "Green key to":                                  			R(Text("greenkeytech"),rdescript="CustomVocabulary: Shultz"),
        "Green key":                                  				R(Text("GreenKey"),rdescript="CustomVocabulary: Shultz"),
       	
        }
    extras = [
    ]
    defaults = {
    }

control.nexus().merger.add_global_rule(CustomVocabulary())
