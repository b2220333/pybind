
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class source_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-snmp - based on the path /snmp-server/v3host/source-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__loopback','__ve',)

  _yang_name = 'source-interface'
  _rest_name = 'source-interface'

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
    self.__ve = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve", rest_name="ve", parent=self, choice=(u'source-interface-type', u've'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ve interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='ve-type', is_config=True)
    self.__loopback = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'source-interface-type', u'loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='intf-loopback-port-type', is_config=True)

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
      return [u'snmp-server', u'v3host', u'source-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'snmp-server', u'v3host', u'source-interface']

  def _get_loopback(self):
    """
    Getter method for loopback, mapped from YANG variable /snmp_server/v3host/source_interface/loopback (intf-loopback-port-type)
    """
    return self.__loopback
      
  def _set_loopback(self, v, load=False):
    """
    Setter method for loopback, mapped from YANG variable /snmp_server/v3host/source_interface/loopback (intf-loopback-port-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loopback is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loopback() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'source-interface-type', u'loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='intf-loopback-port-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loopback must be of a type compatible with intf-loopback-port-type""",
          'defined-type': "brocade-snmp:intf-loopback-port-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'source-interface-type', u'loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='intf-loopback-port-type', is_config=True)""",
        })

    self.__loopback = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loopback(self):
    self.__loopback = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'source-interface-type', u'loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='intf-loopback-port-type', is_config=True)


  def _get_ve(self):
    """
    Getter method for ve, mapped from YANG variable /snmp_server/v3host/source_interface/ve (ve-type)
    """
    return self.__ve
      
  def _set_ve(self, v, load=False):
    """
    Setter method for ve, mapped from YANG variable /snmp_server/v3host/source_interface/ve (ve-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ve is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ve() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve", rest_name="ve", parent=self, choice=(u'source-interface-type', u've'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ve interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='ve-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ve must be of a type compatible with ve-type""",
          'defined-type': "brocade-snmp:ve-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve", rest_name="ve", parent=self, choice=(u'source-interface-type', u've'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ve interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='ve-type', is_config=True)""",
        })

    self.__ve = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ve(self):
    self.__ve = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve", rest_name="ve", parent=self, choice=(u'source-interface-type', u've'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ve interface to use', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='ve-type', is_config=True)

  loopback = __builtin__.property(_get_loopback, _set_loopback)
  ve = __builtin__.property(_get_ve, _set_ve)

  __choices__ = {u'source-interface-type': {u've': [u've'], u'loopback': [u'loopback']}}
  _pyangbind_elements = {'loopback': loopback, 've': ve, }


