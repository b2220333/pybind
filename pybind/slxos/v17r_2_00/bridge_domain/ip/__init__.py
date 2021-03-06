
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bd_pim
import bd_ip_igmp
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-bridge-domain - based on the path /bridge-domain/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IP configurations for an interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bd_pim','__bd_ip_igmp',)

  _yang_name = 'ip'
  _rest_name = 'ip'

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
    self.__bd_pim = YANGDynClass(base=bd_pim.bd_pim, is_container='container', presence=False, yang_name="bd-pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP PIM Snooping', u'alt-name': u'pim', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'131', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    self.__bd_ip_igmp = YANGDynClass(base=bd_ip_igmp.bd_ip_igmp, is_container='container', presence=False, yang_name="bd-ip-igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'alt-name': u'igmp', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'130', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)

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
      return [u'bridge-domain', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'bridge-domain', u'ip']

  def _get_bd_pim(self):
    """
    Getter method for bd_pim, mapped from YANG variable /bridge_domain/ip/bd_pim (container)
    """
    return self.__bd_pim
      
  def _set_bd_pim(self, v, load=False):
    """
    Setter method for bd_pim, mapped from YANG variable /bridge_domain/ip/bd_pim (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bd_pim is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bd_pim() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bd_pim.bd_pim, is_container='container', presence=False, yang_name="bd-pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP PIM Snooping', u'alt-name': u'pim', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'131', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bd_pim must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bd_pim.bd_pim, is_container='container', presence=False, yang_name="bd-pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP PIM Snooping', u'alt-name': u'pim', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'131', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)""",
        })

    self.__bd_pim = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bd_pim(self):
    self.__bd_pim = YANGDynClass(base=bd_pim.bd_pim, is_container='container', presence=False, yang_name="bd-pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP PIM Snooping', u'alt-name': u'pim', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'131', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)


  def _get_bd_ip_igmp(self):
    """
    Getter method for bd_ip_igmp, mapped from YANG variable /bridge_domain/ip/bd_ip_igmp (container)
    """
    return self.__bd_ip_igmp
      
  def _set_bd_ip_igmp(self, v, load=False):
    """
    Setter method for bd_ip_igmp, mapped from YANG variable /bridge_domain/ip/bd_ip_igmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bd_ip_igmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bd_ip_igmp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bd_ip_igmp.bd_ip_igmp, is_container='container', presence=False, yang_name="bd-ip-igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'alt-name': u'igmp', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'130', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bd_ip_igmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bd_ip_igmp.bd_ip_igmp, is_container='container', presence=False, yang_name="bd-ip-igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'alt-name': u'igmp', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'130', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)""",
        })

    self.__bd_ip_igmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bd_ip_igmp(self):
    self.__bd_ip_igmp = YANGDynClass(base=bd_ip_igmp.bd_ip_igmp, is_container='container', presence=False, yang_name="bd-ip-igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'alt-name': u'igmp', u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'sort-priority': u'130', u'callpoint': u'BDIgmps'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)

  bd_pim = __builtin__.property(_get_bd_pim, _set_bd_pim)
  bd_ip_igmp = __builtin__.property(_get_bd_ip_igmp, _set_bd_ip_igmp)


  _pyangbind_elements = {'bd_pim': bd_pim, 'bd_ip_igmp': bd_ip_igmp, }


