from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from app.models import Plans
"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


class GroupModelView(ModelView):
    datamodel = SQLAInterface(Plans)
    label_columns = {'id': 'Plan_ID', 'name': 'Plan_Name'}
    list_columns = ['id', 'name']
"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()


appbuilder.add_view(GroupModelView, "List Plans", icon="fa-folder-open-o", category="Client Portfolio",
                    category_icon="fa-envelope")