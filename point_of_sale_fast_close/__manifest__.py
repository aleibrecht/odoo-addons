##############################################################################
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Point of Sale Fast Close',
    'version': '11.0.0.0.0',
    'category': 'Tools',
    'summary': "Fix to speedup close on POS",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/odoo-addons',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale'
    ],
    'data': [
        'data/cron_data.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
