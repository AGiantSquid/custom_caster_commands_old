from dragonfly.actions.action_base import Repeat
from dragonfly.actions.action_key import Key
from dragonfly.actions.action_text import Text

from caster.lib import control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class CustomPunctuation(MergeRule):
    pronunciation = "custom punctuation"
    mapping = {

        # my custom overrides
        "double quotes":                            R(Key("dquote,dquote,left"), rdescript="Quotation Marks"),
        "Quach it":                                 R(Key("apostrophe,apostrophe,left"), rdescript="Thin Quotation Marks"),
        "equals | equal to":                        R(Text(" = "), rdescript="ColdFusion: Equals"),
        "not equals | not equal to":                R(Text(" != "), rdescript="ColdFusion: Not Equal To"),
        "is equal to":                              R(Text(" == "), rdescript="ColdFusion: Not Equal To"),
        "[is] greater than":                        R(Text(" > "), rdescript="> Comparison"),
        "[is] less than":                           R(Text(" < "), rdescript="< Comparison"),
        "[is] greater [than] [or] equal [to]":      R(Text(" >= "), rdescript=">= Comparison"),
        "[is] less [than] [or] equal [to]":         R(Text(" <= "), rdescript="<= Comparison"),
        "kirksorp":                                 R(Key("lbrace"), rdescript="Left Curly Brace"),
        "kirkos":                                   R(Key("rbrace"), rdescript="Right Curly Brace"),
        "plus":                                     R(Text(" + "), rdescript="ColdFusion: Plus"),
        "minus":                                    R(Text(" - "), rdescript="ColdFusion: Minus"),

        # this is same as the default punctuation
        "sinker":                                   R(Key("semicolon"), rdescript="Semicolon"),
        "prekris":                                  R(Key("lparen, rparen, left"), rdescript="Parentheses"),
        "brax":                                     R(Key("lbracket, rbracket, left"), rdescript="Square Brackets"),
        "curly":                                    R(Key("lbrace, rbrace, left"), rdescript="Curly Braces"),
        "angle":                                    R(Key("langle, rangle, left"), rdescript="Angle Brackets"),
        "(pipe | pipes) (sim | symbol)":            R(Text("|"), rdescript="Pipe Symbol"),
        "pipes and":                                R(Text("|"), rdescript="Pipe Symbol"),
        'skoosh [<npunc>]':                         R(Key("space"), rdescript="Space") * Repeat(extra="npunc"),
        "clamor":                                   R(Text("!"), rdescript="Exclamation Mark"),
        "deckle":                                   R(Text(":"), rdescript="Colon"),
        "starling":                                 R(Key("asterisk"), rdescript="Asterisk"),
        "questo":                                   R(Text("?"), rdescript="Question Mark"),
        "comma":                                    R(Text(","), rdescript="Comma"),
        "carrot":                                   R(Text("^"), rdescript="Carat"),
        "(period | dot)":                           R(Text("."), rdescript="Dot"),
        "at sign":                                  R(Text("@"), rdescript="At Sign"),
        "hash tag | pound sign":                    R(Text("#"), rdescript="Hash Tag"),
        "apostrophe":                               R(Text("'"), rdescript="Apostrophe"),
        "underscore":                               R(Text("_"), rdescript="Underscore"),
        "backslash":                                R(Text("\\"), rdescript="Back Slash"),
        "slash":                                    R(Text("/"), rdescript="Forward Slash"),
        "Dolly":                                    R(Text("$"), rdescript="Dollar Sign"),
        "Percy":                                   R(Key("percent"), rdescript="Percent Sign"),
        'tarp [<npunc>]':                          R(Key("tab"), rdescript="Tab") * Repeat(extra="npunc"),
        'tarsh [<npunc>]':                          R(Key("tab"), rdescript="Tab") * Repeat(extra="npunc"),
        "swipe":                                     R(Text(", "), rdescript="Comma + Space"),
    }

    extras = [
        IntegerRefST("npunc", 0, 10),
    ]
    defaults = {
        "npunc": 1,
    }

control.nexus().merger.add_global_rule(CustomPunctuation())
