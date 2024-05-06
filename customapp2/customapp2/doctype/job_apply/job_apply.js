// Copyright (c) 2024, me and contributors
// For license information, please see license.txt
frappe.ui.form.on("Job Apply", {
    refresh: function(frm){
        // selected_role=frm.doc.role;
        detail=frm.fields_dict.details.grid.fields_map;
        detail.language.hidden=1;
        detail.framework.hidden=1;
        detail.ide.hidden=1;
        detail.applied_date.hidden=1;
        detail.initials.hidden=1;
        detail.testing_tools.hidden=1;
        detail.bug_tracking_system.hidden=1;
        detail.automation_experience.hidden=1;
        detail.test_environment.hidden=1;
        detail.applied_date.hidden=1;
        detail.test_environment.hidden=1;
        detail.design_style.hidden=1;
        detail.color_theory_knowledge.hidden=1;
        detail.typography_skills.hidden=1;
        detail.uiux_experience.hidden=1;
        detail.applied_date.hidden=1;
        detail.initials.hidden=1;
    },
    role: function(frm) {
        selected_role=frm.doc.role;
        detail=frm.fields_dict.details.grid.fields_map;
        detail.language.hidden=1;
        detail.framework.hidden=1;
        detail.ide.hidden=1;
        detail.applied_date.hidden=1;
        detail.initials.hidden=1;
        detail.testing_tools.hidden=1;
        detail.bug_tracking_system.hidden=1;
        detail.automation_experience.hidden=1;
        detail.test_environment.hidden=1;
        detail.applied_date.hidden=1;
        detail.test_environment.hidden=1;
        detail.design_style.hidden=1;
        detail.color_theory_knowledge.hidden=1;
        detail.typography_skills.hidden=1;
        detail.uiux_experience.hidden=1;
        detail.applied_date.hidden=1;
        detail.initials.hidden=1;
        if(selected_role==="Developer"){
                   detail.language.hidden=0;
                   detail.framework.hidden=0;
                   detail.ide.hidden=0;
                   detail.applied_date.hidden=0;
                   detail.initials.hidden=0;
        }
        else if(selected_role==="QA"){
            detail.testing_tools.hidden=0;
           detail.bug_tracking_system.hidden=0;
           detail.automation_experience.hidden=1;
           detail.test_environment.hidden=0;
           detail.applied_date.hidden=0;
           detail.test_environment.hidden=0;
        }
        else{
            detail.design_style.hidden=0;
            detail.color_theory_knowledge.hidden=0;
            detail.typography_skills.hidden=0;
            detail.uiux_experience.hidden=0;
            detail.applied_date.hidden=0;
            detail.initials.hidden=0;
        }
    }
});
frappe.ui.form.on("Details",{
language: function(frm,cdt,cdn){
    // console.log(locals[cdt][cdn]);
    if(locals[cdt][cdn].language==='Python'){
        locals[cdt][cdn].framework="django";
    }
    else if(locals[cdt][cdn].language==="Javascript"){
        locals[cdt][cdn].framework='React Native';
    }
    else{
        locals[cdt][cdn].framework='Laravel';
    }
    frm.refresh_field("details")
},
  ide:function(frm,cdt,cdn){
      locals[cdt][cdn].applied_date=frappe.datetime.nowdate();
      locals[cdt][cdn].initials=frappe.user.full_name;
    frm.refresh_field("details");
    console.log(locals[cdt][cdn]);
  },
  design_style:function(frm,cdt,cdn) {
    if(locals[cdt][cdn].ide){
        locals[cdt][cdn].applied_date=frappe.datetime.nowdate();
        locals[cdt][cdn].initials=frappe.user.full_name;
      }
      frm.refresh_field("details")
      console.log(locals[cdt][cdn]);
  },
  test_environment:function(frm,cdt,cdn){
    locals[cdt][cdn].applied_date=frappe.datetime.nowdate();
    locals[cdt][cdn].initials=frappe.user.full_name;
    frm.refresh_field("details");
    console.log(locals[cdt][cdn]);
  }
});