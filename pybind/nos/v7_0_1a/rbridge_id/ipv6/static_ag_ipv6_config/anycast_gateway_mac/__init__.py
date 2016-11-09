
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class anycast_gateway_mac(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/static-ag-ipv6-config/anycast-gateway-mac. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Anycast gateway MAC address.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_anycast_gateway_mac','__ipv6_anycast_default_mac',)

  _yang_name = 'anycast-gateway-mac'
  _rest_name = 'anycast-gateway-mac'

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
    self.__ipv6_anycast_gateway_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-anycast-gateway-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='mac-access-list:mac-address-type', is_config=True)
    self.__ipv6_anycast_default_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-anycast-default-mac", rest_name="default-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Anycast gateway default MAC.', u'alt-name': u'default-mac'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'static-ag-ipv6-config', u'anycast-gateway-mac']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'anycast-gateway-mac']

  def _get_ipv6_anycast_gateway_mac(self):
    """
    Getter method for ipv6_anycast_gateway_mac, mapped from YANG variable /rbridge_id/ipv6/static_ag_ipv6_config/anycast_gateway_mac/ipv6_anycast_gateway_mac (mac-access-list:mac-address-type)
    """
    return self.__ipv6_anycast_gateway_mac
      
  def _set_ipv6_anycast_gateway_mac(self, v, load=False):
    """
    Setter method for ipv6_anycast_gateway_mac, mapped from YANG variable /rbridge_id/ipv6/static_ag_ipv6_config/anycast_gateway_mac/ipv6_anycast_gateway_mac (mac-access-list:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_anycast_gateway_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_anycast_gateway_mac() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ipv6-anycast-gateway-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='mac-access-list:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_anycast_gateway_mac must be of a type compatible with mac-access-list:mac-address-type""",
          'defined-type': "mac-access-list:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-anycast-gateway-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='mac-access-list:mac-address-type', is_config=True)""",
        })

    self.__ipv6_anycast_gateway_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_anycast_gateway_mac(self):
    self.__ipv6_anycast_gateway_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-anycast-gateway-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='mac-access-list:mac-address-type', is_config=True)


  def _get_ipv6_anycast_default_mac(self):
    """
    Getter method for ipv6_anycast_default_mac, mapped from YANG variable /rbridge_id/ipv6/static_ag_ipv6_config/anycast_gateway_mac/ipv6_anycast_default_mac (empty)

    YANG Description: Anycast gateway default MAC.
    """
    return self.__ipv6_anycast_default_mac
      
  def _set_ipv6_anycast_default_mac(self, v, load=False):
    """
    Setter method for ipv6_anycast_default_mac, mapped from YANG variable /rbridge_id/ipv6/static_ag_ipv6_config/anycast_gateway_mac/ipv6_anycast_default_mac (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_anycast_default_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_anycast_default_mac() directly.

    YANG Description: Anycast gateway default MAC.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6-anycast-default-mac", rest_name="default-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Anycast gateway default MAC.', u'alt-name': u'default-mac'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_anycast_default_mac must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-anycast-default-mac", rest_name="default-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Anycast gateway default MAC.', u'alt-name': u'default-mac'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)""",
        })

    self.__ipv6_anycast_default_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_anycast_default_mac(self):
    self.__ipv6_anycast_default_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-anycast-default-mac", rest_name="default-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Anycast gateway default MAC.', u'alt-name': u'default-mac'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)

  ipv6_anycast_gateway_mac = __builtin__.property(_get_ipv6_anycast_gateway_mac, _set_ipv6_anycast_gateway_mac)
  ipv6_anycast_default_mac = __builtin__.property(_get_ipv6_anycast_default_mac, _set_ipv6_anycast_default_mac)


  _pyangbind_elements = {'ipv6_anycast_gateway_mac': ipv6_anycast_gateway_mac, 'ipv6_anycast_default_mac': ipv6_anycast_default_mac, }


