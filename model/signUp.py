import email
from unicodedata import name
from odoo import api, fields, models, _

class signUp(models.Model):
    _description='Sign UP from flutter'
    _name='signup.insert'

    email = fields.Char(string='email',required=True)
    password = fields.Char(string='password',required=True)