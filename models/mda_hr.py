# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class ResCountryLGA(models.Model):
    _name = 'res.country.lga'
    _description = 'Local Government Area'

    name = fields.Char(string='LGA', required=True)
    state_id = fields.Many2one(
        'res.country.state', string='State', required=True,
        domain="[('country_id.code', '=', 'NG')]",
        help="The Nigerian state to which this LGA belongs."
    )

class Employee(models.Model):
    _inherit = 'hr.employee'

    # --- Defaults & New Fields ---
    country_id = fields.Many2one(
        'res.country', string='Country',
        default=lambda self: self.env.ref('base.ng').id,
        domain="[('code', '=', 'NG')]",
        required=True,
        readonly=True,
        help="Fixed to Nigeria"
    )

    state_id = fields.Many2one(
        'res.country.state', string='State',
        domain="[('country_id.code', '=', 'NG')]",
        required=True
    )
    lga_id = fields.Many2one(
        'res.country.lga', string='LGA',
        domain="[('state_id', '=', state_id)]",
        required=True
    )

    # (other fields as before… File Number, IPPIS, etc.)
    file_number             = fields.Char(string="File Number")
    ippis                   = fields.Char(string="IPPIS")
    surname                 = fields.Char(string="Surname")
    first_name              = fields.Char(string="First Name")
    middle_name             = fields.Char(string="Middle Name")

    sex                     = fields.Selection(
                                [('male','Male'),('female','Female')],
                                string="Sex")


    salary_grade_level      = fields.Char(string="Salary Grade Level")
    type_of_appointment     = fields.Char(string="Type Of Appointment")
    date_of_first_appointment  = fields.Date(string="Date Of First Appointment")
    date_of_present_appointment= fields.Date(string="Date Of Present Appointment")
    pfa_name                = fields.Char(string="PFA Name")
    rsa_pin                 = fields.Char(string="RSA Pin")
    email                   = fields.Char(string="Email")
    geo_political_zone      = fields.Char(string="Geo Political Zone")
    remark                  = fields.Text(string="Remark")
    status                  = fields.Char(string="Status")
    location                = fields.Char(string="Location")
    qualification           = fields.Char(string="Qualification")
    nature_of_job           = fields.Char(string="Nature Of Job")
    description_of_job      = fields.Text(string="Description Of Job")
    salary_structure        = fields.Char(string="Salary Structure")

    # Override name
    name = fields.Char(compute='_compute_name', store=True)
    @api.depends('surname', 'first_name', 'middle_name')
    def _compute_name(self):
        for rec in self:
            rec.name = ' '.join(filter(None, [rec.surname, rec.first_name, rec.middle_name]))

    # Age On Entry
    age_on_entry = fields.Integer(
        compute='_compute_age_on_entry', store=True,
        string="Age On Entry")
    @api.depends('birthday', 'date_of_present_appointment')
    def _compute_age_on_entry(self):
        for rec in self:
            if rec.birthday and rec.date_of_present_appointment:
                rec.age_on_entry = relativedelta(rec.date_of_present_appointment, rec.birthday).years
            else:
                rec.age_on_entry = 0

    # Retirement Date
    retirement_date = fields.Date(
        compute='_compute_retirement_date', store=True,
        string="Date of Retirement")
    @api.depends('date_of_first_appointment', 'birthday')
    def _compute_retirement_date(self):
        for rec in self:
            dates = []
            if rec.date_of_first_appointment:
                dates.append(rec.date_of_first_appointment + relativedelta(years=35))
            if rec.birthday:
                dates.append(rec.birthday + relativedelta(years=60))
            rec.retirement_date = min(dates) if dates else False

# Test comment for git cache