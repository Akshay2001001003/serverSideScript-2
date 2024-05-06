# Copyright (c) 2024, me and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
@frappe.whitelist()
def getDetails(program_name):
    # details=frappe.get_doc("Details")
    # job=frappe.get_doc("Job_Apply",program_name)
    # detail=form.fields_dict.details.grid.field_map
    # for details in detail:
    #       details.hidden=1
    # if job.role=="Developer":
    #       detail.language.hidden=0
    #       detail.Framework.hidden=0
    #       detail.ide.hidden=0
    #       detail.applied_date.hidden=0
    #       detail.initials.hidden=0
    # elif job.role=="QA":
    #       details.testing_tools.hidden=0
    #       details.bug_tracking_system.hidden=0
    #       details.automation_system.hidden=0
    #       details.test_environment.hidden=0
    #       details.applied_date.hidden=0
    #       details.test_environments.hidden=0
    # else:
        #   details.design_style.hidden=0
        #   details.color_theory_knowledge.hidden=0
        #   details.typogrsphy_skills.hidden=0
        # #   details.ui/ux_experience.hidden=0
        #   details.applied_date.hidden=0
        #   details.initials.hidden=0
    return 1
class JobApply(Document):
	pass
