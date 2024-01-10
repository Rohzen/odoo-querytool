# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, timedelta

from odoo import api, models, fields, _
from odoo.exceptions import UserError, AccessError


class QueryTool(models.Model):
    _name = 'query.tool'
    _description = 'Execute query'

    name = fields.Char(string='Description')
    query = fields.Text(string='Query')
    tables = fields.Many2one(comodel_name='query.tables', string='Tables')
    query_type = fields.Many2one(comodel_name='query.types', string='Query types')
    # query_type = fields.Selection([
    #     ('delete', 'DELETE from table_name WHERE id=?'),
    #     ('update', 'UPDATE table_name SET field_name=? WHERE id=?'),
    #     ('insert', 'INSERT INTO table_name(id, name,) VALUES(?, ?)'),
    #     # ('select', 'SELECT from table_name WHERE id=?')
    # ], string='Query type', readonly=False,)

    @api.onchange('query_type', 'tables')
    def onchange_query_type(self):
        if self.tables.name and self.query_type.query:
            self.query = self.query_type.query.replace('table_name', self.tables.name)

    def do_query(self):
        self.env.cr.execute(self.query)

    # @api.one
    # def update_tables_list(self):
    #     query_tables = self.env['query.tables']
    #     delete_cmd = "delete from query_tables"
    #     self.env.cr.execute(delete_cmd)
    #     update_cmd = "select table_name, table_type, table_catalog from information_schema.tables"
    #     cur = self.env.cr.execute(update_cmd)
    #     rows = cur.fetchall()
    #     for row in rows:
    #         query_tables.create({'table_name': row["table_name"]})


class QueryTables(models.Model):
    _name = 'query.tables'
    _description = 'Query tables'

    name = fields.Char('Table name')

class QueryTypes(models.Model):
    _name = 'query.types'
    _description = 'Query types'

    name = fields.Char('name')
    query = fields.Char('query')





