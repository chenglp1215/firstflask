# coding=utf-8
from flask_admin.form import SecureForm
from flask_admin import BaseView as BaseAdminView, expose
from flask_admin.contrib.sqla import ModelView
from flask import url_for, request, redirect
from app import db, admin
from . import models


class BaseView(BaseAdminView):
    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('main.index'))


class BaseModelView(ModelView, BaseView):
    page_size = 50
    # 增加csrf_token
    form_base_class = SecureForm

    def __init__(self, model):
        self.model = model
        super(BaseModelView, self).__init__(self.model, db.session, name=model.__tableplay__, endpoint='love/%s' % model.__tablename__, category="love")


class EachDayTextAdmin(BaseModelView):
    can_view_details = True
    pass


class EachDayArticleAdmin(BaseModelView):
    # column list 参数
    details_template = 'admin/article_detail.html'
    can_view_details = True
    column_editable_list = ['title']
    column_exclude_list = ['article',]
    column_searchable_list = ['title', 'article']
    column_filters = ['title', 'create_time']
    # from 表单参数
    # form_choices = {
    #     'title': [
    #         ('MR', 'Mr'),
    #         ('MRS', 'Mrs'),
    #         ('MS', 'Ms'),
    #         ('DR', 'Dr'),
    #         ('PROF', 'Prof.')
    #     ]
    # }

    form_args = {
        'title': {
            'label': u'标题',
        },
        'article': {
            'label': u'文章',
        },
        'confs': {
            'label': u'每日关联'
        },
        'create_time': {
            'label': u'创建时间',
        },
        'show_counts': {
            'label': u'展示次数',
        },
    }
    # 不生效
    # form_widget_args = {
    #     'article': {
    #         'row': 10,
    #         'style': 'color: black'
    #     }
    # }


class EachDayConfAdmin(BaseModelView):
    can_export = True
    form_ajax_refs = {
        'text': {
            'fields': ['text',],
            'page_size': 10
        },
        'music': {
            'fields': ['id', 'music_title',],
            'page_size': 10
        },
        'article': {
            'fields': ['id', 'title', ],
            'page_size': 10
        }
    }


class EachDayMusicAdmin(BaseModelView):
    create_template = 'admin/music_create.html'
    @expose('/new/', methods=['GET', 'POST'])
    def create_view(self):
        return super(EachDayMusicAdmin, self).create_view()


class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/test_index.html')

admin.add_view(AnalyticsView(name='Analytics', endpoint='love/analytics', category='love'))

admin.add_view(EachDayTextAdmin(models.EachDayText))
admin.add_view(EachDayMusicAdmin(models.EachDayMusic))
admin.add_view(EachDayArticleAdmin(models.EachDayArticle))
admin.add_view(EachDayConfAdmin(models.EachDayConf))
