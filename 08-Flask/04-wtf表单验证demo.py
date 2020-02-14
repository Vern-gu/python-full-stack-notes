from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.secret_key = 'alab'


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    passwd = PasswordField('密码', validators=[DataRequired()])
    passwd2 = PasswordField('确认密码', validators=[DataRequired(), EqualTo('passwd', '密码不一致')])
    submit = SubmitField('提交')


@app.route('/register', methods=['POST', 'GET'])
def form():
    register_form = RegisterForm()
    if request.method == 'POST':
        # username = request.form.get('username')
        if register_form.validate_on_submit():
            return '注册成功'
        else:
            flash('信息有误')

    return render_template('register.html', form=register_form)


if __name__ == '__main__':
    app.run(debug=True)