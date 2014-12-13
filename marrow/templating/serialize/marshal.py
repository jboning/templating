# encoding: utf-8

from __future__ import unicode_literals, absolute_import

import marshal


__all__ = ['render']


def render(data, template=None, i18n=None, **kw):
	"""Serialize data using Python marshal standard library.
	
	Accepts the same extended arguments as the marshal.dumps() function, see:
	
		http://www.python.org/doc/2.6/library/marshal.html#marshal.dumps
	
	"""
	
	return b'application/octet-stream', marshal.dumps(data, **kw)
