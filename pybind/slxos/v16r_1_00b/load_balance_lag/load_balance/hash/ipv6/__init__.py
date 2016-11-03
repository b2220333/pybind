
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag/load-balance/hash/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_src_l4_port','__ipv6_dst_l4_port','__ipv6_src_ip','__ipv6_dst_ip','__ipv6_next_hdr',)

  _yang_name = 'ipv6'
  _rest_name = 'ipv6'

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
    self.__ipv6_next_hdr = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-next-hdr", rest_name="ipv6-next-hdr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-next-hdr', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-next-hdr\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__ipv6_src_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-src-l4-port", rest_name="ipv6-src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__ipv6_dst_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-dst-l4-port", rest_name="ipv6-dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__ipv6_dst_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-dst-ip", rest_name="ipv6-dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__ipv6_src_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-src-ip", rest_name="ipv6-src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

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
      return [u'load-balance-lag', u'load-balance', u'hash', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'load-balance', u'hash', u'ipv6']

  def _get_ipv6_src_l4_port(self):
    """
    Getter method for ipv6_src_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_src_l4_port (empty)
    """
    return self.__ipv6_src_l4_port
      
  def _set_ipv6_src_l4_port(self, v, load=False):
    """
    Setter method for ipv6_src_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_src_l4_port (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_src_l4_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_src_l4_port() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6-src-l4-port", rest_name="ipv6-src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_src_l4_port must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-src-l4-port", rest_name="ipv6-src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__ipv6_src_l4_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_src_l4_port(self):
    self.__ipv6_src_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-src-l4-port", rest_name="ipv6-src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_ipv6_dst_l4_port(self):
    """
    Getter method for ipv6_dst_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_dst_l4_port (empty)
    """
    return self.__ipv6_dst_l4_port
      
  def _set_ipv6_dst_l4_port(self, v, load=False):
    """
    Setter method for ipv6_dst_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_dst_l4_port (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_dst_l4_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_dst_l4_port() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6-dst-l4-port", rest_name="ipv6-dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_dst_l4_port must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-dst-l4-port", rest_name="ipv6-dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__ipv6_dst_l4_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_dst_l4_port(self):
    self.__ipv6_dst_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-dst-l4-port", rest_name="ipv6-dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_ipv6_src_ip(self):
    """
    Getter method for ipv6_src_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_src_ip (empty)
    """
    return self.__ipv6_src_ip
      
  def _set_ipv6_src_ip(self, v, load=False):
    """
    Setter method for ipv6_src_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_src_ip (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_src_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_src_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6-src-ip", rest_name="ipv6-src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_src_ip must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-src-ip", rest_name="ipv6-src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__ipv6_src_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_src_ip(self):
    self.__ipv6_src_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-src-ip", rest_name="ipv6-src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_ipv6_dst_ip(self):
    """
    Getter method for ipv6_dst_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_dst_ip (empty)
    """
    return self.__ipv6_dst_ip
      
  def _set_ipv6_dst_ip(self, v, load=False):
    """
    Setter method for ipv6_dst_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_dst_ip (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_dst_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_dst_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6-dst-ip", rest_name="ipv6-dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_dst_ip must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-dst-ip", rest_name="ipv6-dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__ipv6_dst_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_dst_ip(self):
    self.__ipv6_dst_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-dst-ip", rest_name="ipv6-dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_ipv6_next_hdr(self):
    """
    Getter method for ipv6_next_hdr, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_next_hdr (empty)
    """
    return self.__ipv6_next_hdr
      
  def _set_ipv6_next_hdr(self, v, load=False):
    """
    Setter method for ipv6_next_hdr, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6/ipv6_next_hdr (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_next_hdr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_next_hdr() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6-next-hdr", rest_name="ipv6-next-hdr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-next-hdr', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-next-hdr\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_next_hdr must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-next-hdr", rest_name="ipv6-next-hdr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-next-hdr', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-next-hdr\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__ipv6_next_hdr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_next_hdr(self):
    self.__ipv6_next_hdr = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-next-hdr", rest_name="ipv6-next-hdr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6-next-hdr', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ipv6 ipv6-next-hdr\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

  ipv6_src_l4_port = __builtin__.property(_get_ipv6_src_l4_port, _set_ipv6_src_l4_port)
  ipv6_dst_l4_port = __builtin__.property(_get_ipv6_dst_l4_port, _set_ipv6_dst_l4_port)
  ipv6_src_ip = __builtin__.property(_get_ipv6_src_ip, _set_ipv6_src_ip)
  ipv6_dst_ip = __builtin__.property(_get_ipv6_dst_ip, _set_ipv6_dst_ip)
  ipv6_next_hdr = __builtin__.property(_get_ipv6_next_hdr, _set_ipv6_next_hdr)


  _pyangbind_elements = {'ipv6_src_l4_port': ipv6_src_l4_port, 'ipv6_dst_l4_port': ipv6_dst_l4_port, 'ipv6_src_ip': ipv6_src_ip, 'ipv6_dst_ip': ipv6_dst_ip, 'ipv6_next_hdr': ipv6_next_hdr, }

