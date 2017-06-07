from flask_appbuilder import ModelView, IndexView, BaseView, expose, has_access


class MyIndexView(IndexView):
    index_template = 'mybaseindex.html'

    @expose('/')
    def index(self):
        self.update_redirect()
        region = 'United Kindgom'
        country = 'UK'
        return self.render_template(self.index_template, region=region, appbuilder=self.appbuilder)
