
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class suppress_ra(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/ipv6/ipv6-nd-ra/ipv6-intf-cmds/nd/suppress-ra. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__suppress_ra_flag','__suppress_ra_mtu','__suppress_ra_all',)

  _yang_name = 'suppress-ra'
  _rest_name = 'suppress-ra'

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
    self.__suppress_ra_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress response to RS in addition to not sending Ras', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__suppress_ra_mtu = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable sending MTU in Router-Advertisement messages', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__suppress_ra_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-flag", rest_name="suppress-ra-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds', u'nd', u'suppress-ra']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'ipv6', u'nd', u'suppress-ra']

  def _get_suppress_ra_flag(self):
    """
    Getter method for suppress_ra_flag, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/suppress_ra/suppress_ra_flag (empty)
    """
    return self.__suppress_ra_flag
      
  def _set_suppress_ra_flag(self, v, load=False):
    """
    Setter method for suppress_ra_flag, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/suppress_ra/suppress_ra_flag (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_ra_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_ra_flag() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suppress-ra-flag", rest_name="suppress-ra-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_ra_flag must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-flag", rest_name="suppress-ra-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__suppress_ra_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_ra_flag(self):
    self.__suppress_ra_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-flag", rest_name="suppress-ra-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_suppress_ra_mtu(self):
    """
    Getter method for suppress_ra_mtu, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/suppress_ra/suppress_ra_mtu (empty)
    """
    return self.__suppress_ra_mtu
      
  def _set_suppress_ra_mtu(self, v, load=False):
    """
    Setter method for suppress_ra_mtu, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/suppress_ra/suppress_ra_mtu (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_ra_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_ra_mtu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suppress-ra-mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable sending MTU in Router-Advertisement messages', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_ra_mtu must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable sending MTU in Router-Advertisement messages', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__suppress_ra_mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_ra_mtu(self):
    self.__suppress_ra_mtu = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable sending MTU in Router-Advertisement messages', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_suppress_ra_all(self):
    """
    Getter method for suppress_ra_all, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/suppress_ra/suppress_ra_all (empty)
    """
    return self.__suppress_ra_all
      
  def _set_suppress_ra_all(self, v, load=False):
    """
    Setter method for suppress_ra_all, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/suppress_ra/suppress_ra_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_ra_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_ra_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suppress-ra-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress response to RS in addition to not sending Ras', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_ra_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress response to RS in addition to not sending Ras', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__suppress_ra_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_ra_all(self):
    self.__suppress_ra_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-ra-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress response to RS in addition to not sending Ras', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

  suppress_ra_flag = __builtin__.property(_get_suppress_ra_flag, _set_suppress_ra_flag)
  suppress_ra_mtu = __builtin__.property(_get_suppress_ra_mtu, _set_suppress_ra_mtu)
  suppress_ra_all = __builtin__.property(_get_suppress_ra_all, _set_suppress_ra_all)


  _pyangbind_elements = {'suppress_ra_flag': suppress_ra_flag, 'suppress_ra_mtu': suppress_ra_mtu, 'suppress_ra_all': suppress_ra_all, }


