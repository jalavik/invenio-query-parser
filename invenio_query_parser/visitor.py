# -*- coding: utf-8 -*-
#
# This file is part of Invenio Query Parser.
# Copyright (C) 2014 CERN.
#
# Invenio Query Parser is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio Query Parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Store the actual visitor methods."""


def make_visitor():
    """Make a visitor decorator."""
    _methods = {}

    # The actual @visitor decorator
    def _visitor(arg_type):
        """Decorator that creates a visitor method."""

        # Delegating visitor implementation

        def _visitor_impl(self, arg, *args, **kwargs):
            """Actual visitor method implementation."""
            method = _methods[type(arg)]
            return method(self, arg, *args, **kwargs)

        def decorator(fn):
            _methods[arg_type] = fn
            # Replace all decorated methods with _visitor_impl
            return _visitor_impl

        return decorator

    return _visitor
