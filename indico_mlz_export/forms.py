# This file is part of Indico.
# Copyright (C) 2017 Bjoern Pedersen.
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from wtforms.fields import StringField, FileField
from wtforms.validators import DataRequired, Optional

from indico.web.forms.base import IndicoForm

from indico_mlz_export import _

VERANSTALTUNGS_DESC = """FZJ Veranstaltungscode"""
SAP_EXPORT_DESC = """CSV-Export des aktuellen Stands im SAP. Vorhandene Datensätze werden nicht erneut exportiert.
Keine Datei auswählen, um alle Datensätze aus INDICO zu exportieren."""


class EventSettingsForm(IndicoForm):
    veranstaltungsid = StringField(_('Veranstaltungs id'), [DataRequired()], description=VERANSTALTUNGS_DESC)


class ExportForm(IndicoForm):
    sap_export = FileField(_('Aktueller Stand im SAP'), [Optional()], description=SAP_EXPORT_DESC)