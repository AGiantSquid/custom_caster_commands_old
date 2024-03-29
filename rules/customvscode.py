from dragonfly import (Grammar, AppContext, Dictation, Key, Pause)
from dragonfly.actions.action_key import Key
from dragonfly.actions.action_text import Text

from caster.lib import settings
from caster.lib import control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class CustomVSCode(MergeRule):
    pronunciation = "custom sublime commands"
    mapping = {
        # my custom overrides
        "save file as":
            R(Key("cs-s"), rdescript="Sublime: Save As"),
        "grab it":
            R(Key("c-d"), rdescript="Sublime: Ctrl + d"),
        "skip it":
            R(Key("c-k,c-d"), rdescript="Sublime: Ctrl + d, k"),
        "uppercase":
            R(Key("csa-u"), rdescript="Sublime: uppercase"),
        "lowercase":
            R(Key("csa-l"), rdescript="Sublime: uppercase"),
        "cue jeep":
            R(Key("a-up"), rdescript="Sublime: uppercase"),
        "cue doom":
            R(Key("a-down"), rdescript="Sublime: uppercase"),
        "execute":
            R(Key("s-enter"), rdescript="Sublime: Ctrl + b"),
        "[go to] group [<n2>]":
            R(Key("c-%(n2)s"), rdescript="Sublime: Go to Group #"),
        "spring <n>":
            R(Key("c-g") + Pause("10") + Text("%(n)s") + Key("enter"),
              rdescript="Sublime: Go to Line #"),
        "crew [<text>]":
            R(Key("c-i") + Pause("10") + Text("%(text)s") + Pause("10") + Key("enter") +
              Key("escape"),
              rdescript="Sublime: Get Next"),
        "trail [<text>]":
            R(Key("c-u") + Pause("10") + Text("%(text)s") + Pause("10") + Key("enter") +
              Key("escape"),
              rdescript="Sublime: Get Next"),
        "expand|fill quotes":
            R(Key("cs-space"), rdescript="Atom: Expand Selection to Quotes"),
        # SymbolSpecs.FUNCTION:                       R(Text("fu\\") + Key("tab"), rdescript="CustomSublime: Function"),
        # SymbolSpecs.IF:                             R(Text("if\\") + Key("tab"), rdescript="ColdFusion: If"),
        # my custom overrides
        "double quotes":
            R(Key("dquote"), rdescript="Quotation Marks"),
        "Quach it":
            R(Key("apostrophe"), rdescript="Thin Quotation Marks"),
        "(cellaring | sell rang) <n> <n3>":
            R(
                Key("c-g") + Pause("5") + Text("%(n)s") + Key("enter") + Pause("5") +
                Key("c-k") + Key("c-space") + Pause("5") + Key("c-g") + Pause("10") +
                Text("%(n3)s") + Key("enter") + Key("end") + Key("c-k") + Key("c-a")),
    }

    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("n", 1, 1000),
        IntegerRefST("n2", 1, 9),
        IntegerRefST("n3", 1, 999),
    ]
    defaults = {"n": 1, "mim": "", "text": ""}


#---------------------------------------------------------------------------

context = AppContext(executable="code")
grammar = Grammar("Visual Studio Code", context=context)

if settings.SETTINGS["apps"]["visualstudiocode"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(CustomVSCode())
    else:
        rule = CustomVSCode(name="sublime")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
