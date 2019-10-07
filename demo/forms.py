import wtforms
from flask_wtf import Form
from wtforms import ValidationError
from wtforms import validators


def keyword_valid(form,field):
    data = field.data
    keywords = ["admin","asd"]
    if data in keywords:
        raise ValidationError("敏感词")


class TaskForm(Form):
    name = wtforms.StringField(
        render_kw= {
            "class":"form-control",
            "plaeholder":"任务名称"
        }
    )
    description = wtforms.TextField(
        render_kw={
            "class": "form-control",
            "plaeholder": "任务描述"
        }
    )
    time = wtforms.DateField(
        render_kw={
            "class": "form-control",
            "plaeholder": "任务时间"
        }
    )
    public = wtforms.StringField(
        render_kw={
            "class": "form-control",
            "plaeholder": "公布任务人"
        }
    )