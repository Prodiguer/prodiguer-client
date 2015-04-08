# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client/metrics/formatter/constants.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Constants used across the package.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Supported input formats.
INPUT_FORMAT_PCMDI = 'pcmdi'

# Set of supported input formats.
INPUT_FORMAT_SET = set([
	INPUT_FORMAT_PCMDI,
	])


# Supported output formats.
OUTPUT_FORMAT_BLOCKS = 'blocks'

# Set of supported output formats.
OUTPUT_FORMAT_SET = set([
	OUTPUT_FORMAT_BLOCKS,
	])