#coding:UTF-8
__author__ = 'YAN'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')