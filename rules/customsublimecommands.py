from dragonfly import (Grammar, AppContext, Dictation, Key)
from dragonfly.actions.action_key import Key
from dragonfly.actions.action_text import Text

from caster.lib import settings
from caster.lib.ccr.standard import SymbolSpecs
from caster.lib import control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class CustomSublimeCommands(MergeRule):
    pronunciation = "custom sublime commands"
    mapping = {  

        #my custom overrides
        "save file as":                                 R(Key("cs-s"), rdescript="Sublime: Save As"),
        # SymbolSpecs.FUNCTION:                       R(Text("fu\\") + Key("tab"), rdescript="CustomSublime: Function"),
        # SymbolSpecs.IF:                             R(Text("if\\") + Key("tab"), rdescript="ColdFusion: If"),
    }

    extras = [
              Dictation("text"),
              Dictation("mim"),
              IntegerRefST("n", 1, 1000),
              
             ]
    defaults = {"n": 1, "mim":""}

#---------------------------------------------------------------------------

context = AppContext(executable="sublime_text")
grammar = Grammar("Sublime", context=context)

if settings.SETTINGS["apps"]["sublime"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(CustomSublimeCommands())
    else:
        rule = CustomSublimeCommands(name="sublime")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()