from restconf_flask.extensions import db, admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask import flash, render_template,send_file
from restconf_flask.restconf_modules.interfaces import InterfaceInfo
from restconf_flask.restconf_modules.configuration import Configuration
import os


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    port = db.Column(db.Integer)


    def __str__(self):
        return f"Device:{self.host})"
    
class DeviceView(ModelView):   
    can_delete = True
    can_create = True
    create_modal = True
    edit_modal = True
    form_columns = ['host','username','password','port']
    column_list = ['host','username','password','port']
    
    
    @action("get_interface_info", "Get Interfaces Information")
    def action_get_interface_info(self, devices):
        for device in devices:
            if device:
                dvc = Device.query.get(device)
                dvc_interfaces = InterfaceInfo(dvc.host, dvc.port, dvc.username, dvc.password)
                interfaces = dvc_interfaces.get_interfaces()
                return self.render('admin/device_interfaces_information.html',device=dvc,interfaces=interfaces)
            
    @action("get_device_configuration","Get Device Configuration")
    def action_get_device_configuration(self, devices):
        for device in devices:
            if device:
                dvc = Device.query.get(device)
                dvc_configuration = Configuration(dvc.host,dvc.port,dvc.username,dvc.password)
                dvc_configuration.get_configuration()
                flash(f"Device Configuartion Saved at: config-files/{dvc.host}-config.json",'success')
                
            else:
                flash(f"Device {dvc.host} Configuration saving Failed",'error')

    @action("display_device_configuration","Display Device Configuration")
    def action_display_device_configuration(self, devices):
        for device in devices:
            if device:
                dvc = Device.query.get(device)
                dvc_configuration = Configuration(dvc.host,dvc.port,dvc.username,dvc.password)
                configuration=dvc_configuration.display_configuration()
                return self.render('admin/device_configuration.html',device=device,configuration=configuration)
            

    








