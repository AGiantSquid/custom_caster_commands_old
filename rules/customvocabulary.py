from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text

class CustomVocabulary(MergeRule):
    pronunciation = "custom vocabulary"
    mapping = {
        "Schultz":                                  R(Text(" Shultz "),rdescript="CustomVocabulary: Shultz"),
        "e-mail":                                   R(Text(" email "),rdescript="CustomVocabulary: Email"),
        }
    extras = [
    ]
    defaults = {
    }

control.nexus().merger.add_global_rule(CustomVocabulary())