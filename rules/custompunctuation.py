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
        "double quotes":
            R(Key("dquote"), rdescript="Quotation Marks"),
        "Quach it":
            R(Key("apostrophe"), rdescript="Thin Quotation Marks"),
        "equals | equal to":
            R(Text("="), rdescript="Equals"),
        "equeft":
            R(Text(" = "), rdescript="Equals"),
        "Schrock it | shrocket":
            R(Text(" => "), rdescript="Equals"),
        "not equals | not equal to":
            R(Text(" != "), rdescript="Not Equal To"),
        "is equal to":
            R(Text(" == "), rdescript="Not Equal To"),
        "[is] greater than":
            R(Text(" > "), rdescript="> Comparison"),
        "[is] less than":
            R(Text(" < "), rdescript="< Comparison"),
        "[is] greater [than] [or] equal [to]":
            R(Text(" >= "), rdescript=">= Comparison"),
        "[is] less [than] [or] equal [to]":
            R(Text(" <= "), rdescript="<= Comparison"),
        "deplush":
            R(Text(" + "), rdescript="Plus with padding"),
        "plus":
            R(Text("+"), rdescript="Plus"),
        "pluqual | Luke while":
            R(Text(" += "), rdescript="Plus Equals"),
        "deminus":
            R(Text(" - "), rdescript="Minus with padding"),
        "minus":
            R(Text("-"), rdescript="Minus"),
        "minqual | min call":
            R(Text(" -= "), rdescript="Minus Equals"),
        "min twice | mintwice":
            R(Text("--"), rdescript="Minus Twice"),

        # this is same as the default punctuation
        "sinker":
            R(Key("semicolon"), rdescript="Semicolon"),
        "prekris":
            R(Key("lparen"), rdescript="Parentheses"),
        "prekorp":
            R(Key("lparen"), rdescript="Parentheses"),
        "prekos":
            R(Key("rparen"), rdescript="Parentheses"),
        "brax":
            R(Key("lbracket"), rdescript="Square Brackets"),
        "brackorp":
            R(Key("lbracket"), rdescript="Left Square Bracket"),
        "brackos":
            R(Key("rbracket"), rdescript="Right Square Bracket"),
        "curly":
            R(Key("lbrace"), rdescript="Curly Braces"),
        "kirksorp":
            R(Key("lbrace"), rdescript="Left Curly Brace"),
        "kirkos":
            R(Key("rbrace"), rdescript="Right Curly Brace"),
        "angle":
            R(Key("langle"), rdescript="Left Angle Bracket"),
        "wrangle":
            R(Key("rangle"), rdescript="Right Angle Bracket"),
        "(pipe | pipes) (sim | symbol)":
            R(Text("|"), rdescript="Pipe Symbol"),
        "pipes and":
            R(Text("|"), rdescript="Pipe Symbol"),
        'skoosh [<npunc>]':
            R(Key("space"), rdescript="Space")*Repeat(extra="npunc"),
        "clamor":
            R(Text("!"), rdescript="Exclamation Mark"),
        "deckle":
            R(Text(":"), rdescript="Colon"),
        "starling":
            R(Key("asterisk"), rdescript="Asterisk"),
        "questo":
            R(Text("?"), rdescript="Question Mark"),
        "comma":
            R(Text(","), rdescript="Comma"),
        "carrot":
            R(Text("^"), rdescript="Carat"),
        "(period | dot)":
            R(Text("."), rdescript="Dot"),
        "at sign":
            R(Text("@"), rdescript="At Sign"),
        "hash tag | pound sign | pounder":
            R(Text("#"), rdescript="Hash Tag"),
        "apostrophe":
            R(Text("'"), rdescript="Apostrophe"),
        "tinker":
            R(Text("`"), rdescript='back tick'),
        "crunder":
            R(Text("_"), rdescript="Underscore"),
        "shawls":
            R(Text("\\"), rdescript="Back Slash"),
        "slash":
            R(Text("/"), rdescript="Forward Slash"),
        "Dolly":
            R(Text("$"), rdescript="Dollar Sign"),
        "Percy":
            R(Key("percent"), rdescript="Percent Sign"),
        'tarp [<npunc>]':
            R(Key("tab"), rdescript="Tab") * Repeat(extra="npunc"),
        'tarsh [<npunc>]':
            R(Key("tab"), rdescript="Tab") * Repeat(extra="npunc"),
        'shaber [<npunc>]':
            R(Key("c-rbracket"), rdescript="Tab") * Repeat(extra="npunc"),
        'shable [<npunc>]':
            R(Key("c-lbracket"), rdescript="Tab") * Repeat(extra="npunc"),
        "swipe":
            R(Text(", "), rdescript="Comma + Space"),
    }

    extras = [
        IntegerRefST("npunc", 0, 10),
    ]
    defaults = {
        "npunc": 1,
    }


control.nexus().merger.add_global_rule(CustomPunctuation())
