from config import Config
from flask import Flask, redirect, url_for, render_template
from restconf_flask.extensions import db,admin
from restconf_flask.models.device import Device,DeviceView

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    
    admin.add_view(DeviceView(Device,db.session,name='Add Devices',endpoint='add-devices'))

    admin.init_app(app)

    
    @app.route('/')
    def index():
        return redirect(url_for('admin.index'))
    
    
    return app

       