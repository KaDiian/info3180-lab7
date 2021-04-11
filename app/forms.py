
from flask_wtf import FlaskForm
from flask import Flask, render_template, flash, redirect, url_for
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired()])
    photo = FileField('photo', validators=[FileRequired(), FileAllowed(['jpeg', 'jpg', 'png', 'Images Only!'])])
