
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import input
import output
class get_tunnel_statistics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels-ext - based on the path /brocade_tunnels_ext_rpc/get-tunnel-statistics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Retrieves tunnel statistics - count of bytes & frames
transmitted and received. Output records are sorted in
ascending order of tunnel id.

Data is aggregated from all rbridges of cluster. Clients can
use 'rbridge-id' filter to retrieve statistics from specific
rbridges.

When output contains large number of records, they are sent
in multiple pages. Page size is implementation specific.
Output contains an opaque data 'next-page-cursor' when more
pages exist. Client is expected to invoke the RPC again
with same filters and pass this opaque data as 'page-cursor'
paramater. This cycle should be repeated until the output
does not include 'next-page-cursor' value, indicating there
are no more data. Client should not pass 'page-cursor'
paramater to retrieve first page.

This RPC is equivalent of 'show tunnel statistics' CLI.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__input','__output',)

  _yang_name = 'get-tunnel-statistics'
  _rest_name = 'get-tunnel-statistics'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__input = YANGDynClass(base=input.input, is_leaf=True, yang_name="input", rest_name="input", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='input', is_config=True)
    self.__output = YANGDynClass(base=output.output, is_leaf=True, yang_name="output", rest_name="output", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='output', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'brocade_tunnels_ext_rpc', u'get-tunnel-statistics']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-tunnel-statistics']

  def _get_input(self):
    """
    Getter method for input, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/input (input)
    """
    return self.__input
      
  def _set_input(self, v, load=False):
    """
    Setter method for input, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/input (input)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_input is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_input() directly.
    """
    try:
      t = YANGDynClass(v,base=input.input, is_leaf=True, yang_name="input", rest_name="input", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='input', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """input must be of a type compatible with input""",
          'defined-type': "brocade-tunnels-ext:input",
          'generated-type': """YANGDynClass(base=input.input, is_leaf=True, yang_name="input", rest_name="input", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='input', is_config=True)""",
        })

    self.__input = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_input(self):
    self.__input = YANGDynClass(base=input.input, is_leaf=True, yang_name="input", rest_name="input", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='input', is_config=True)


  def _get_output(self):
    """
    Getter method for output, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output (output)
    """
    return self.__output
      
  def _set_output(self, v, load=False):
    """
    Setter method for output, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output (output)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output() directly.
    """
    try:
      t = YANGDynClass(v,base=output.output, is_leaf=True, yang_name="output", rest_name="output", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='output', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output must be of a type compatible with output""",
          'defined-type': "brocade-tunnels-ext:output",
          'generated-type': """YANGDynClass(base=output.output, is_leaf=True, yang_name="output", rest_name="output", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='output', is_config=True)""",
        })

    self.__output = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output(self):
    self.__output = YANGDynClass(base=output.output, is_leaf=True, yang_name="output", rest_name="output", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='output', is_config=True)

  input = __builtin__.property(_get_input, _set_input)
  output = __builtin__.property(_get_output, _set_output)


  _pyangbind_elements = {'input': input, 'output': output, }


