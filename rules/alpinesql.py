from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text

class AlpineSQL(MergeRule):
    pronunciation = "alpine sequel"
    mapping = {
        "as net quote":     			 	        R(Text("SNetQuote"),rdescript="AlpineSQL: SNetQuote"),
        "as net quotes":	       		            R(Text("SNetQuotes"),rdescript="AlpineSQL: SNetQuotes"),
        "table as net quotes":                      R(Text("tblSNetQuotes"),rdescript="AlpineSQL: tblSNetQuotes"),
        "table emails":                             R(Text("tblEmails"),rdescript="AlpineSQL: tblEmails"),
        "table contractors new":                    R(Text("tblContractorsNew"),rdescript="AlpineSQL: tblContractorsNew"),
        "table contractors extra data":             R(Text("tblContractorsExtraData"),rdescript="AlpineSQL: tblContractorsExtraData"),
        "table order performance pay":              R(Text("tblOrderPerformancePay"),rdescript="AlpineSQL: tblOrderPerformancePay"),
        "table as net quotes":                      R(Text("tblSNetQuotes"),rdescript="AlpineSQL: tblSNetQuotes"),
        "view contractors":                         R(Text("v_Contractors"),rdescript="AlpineSQL: v_Contractors"),
        "contractor ID":                            R(Text("contractorID"),rdescript="AlpineSQL: contractorID"),
        "user ID":                                  R(Text("userID"),rdescript="AlpineSQL: userID"),
        "company name":                             R(Text("companyName"),rdescript="AlpineSQL: companyName"),

        }
    extras = [
    ]
    defaults = {
    }

control.nexus().merger.add_global_rule(AlpineSQL())