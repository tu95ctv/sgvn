odoo.define('x_rebate_management.field_edit', function(require) {
"use strict";

var FormController = require('web.FormController');

var session = require('web.session');
var Dialog = require('web.Dialog');

FormController.include({_onBounceEdit: function () 
    {
            if (this.$buttons) { 
                if (!session.is_superuser){
                this._setMode('edit');
                }
                else
                this.$buttons.find('.o_form_button_edit').odooBounce();
            }
        },
        
        })
    return FormController;

});
    