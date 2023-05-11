#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the sonic_aaa module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class AaaArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_aaa module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'authentication': {
                    'options': {
                        'data': {
                            'options': {
                                'fail_through': {'type': 'bool'},
                                'default_auth': {
                                    'choices': ['local', 'ldap', 'radius', 'tacacs+'],
                                    'type': 'list',
                                    'elements': 'str'
                                },
                            },
                            'type': 'dict'
                        }
                    },
                    'type': 'dict'
                }
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'deleted', 'overridden', 'replaced'],
            'default': 'merged', 'type': 'str'
        }
    }  # pylint: disable=C0301
