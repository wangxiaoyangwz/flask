# -*- coding: utf-8 -*-
from flask import Flask,render_template,session,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app=Flask(__name__)
manager=Manager(app)
bootstrap=Bootstrap(app)
moment=Moment(app)
app.config['SECRET_KEY']='hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/',methods=['GET','POST'])#告诉flaskzei URL 映射中index注册为GET/POST的请求的处理程序
def index():
	form=NameForm()#实例表示表单 创建表单
	if form.validate_on_submit():#测试函数 True
		session['name']=form.name.data#用户输入名字 用date获取  session[]字典存储name 用户会话
		return redirect(url_for('index'))#生成http重定向响应 参数实际是‘/’
		                                  #
	return render_template('index.html',form=form,name=session.get('name'))#字典获取name


if __name__=='__main__':
    manager.run()
