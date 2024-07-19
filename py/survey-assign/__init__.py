#
# See top-level LICENSE.rst file for Copyright information
#
# -*- coding: utf-8 -*-
"""
survey-assign
========

Tools for estimating fiber assignment efficiency in large spectroscopic surveys

.. _desispec: https://github.com/forero/survey-assign
.. _Python: http://python.org
"""

from .fiber_assignment import get_faprob, get_faprob_total

__all__ = ['get_faprob', 'get_faprob_total']

__version__ = '0.1.0'

