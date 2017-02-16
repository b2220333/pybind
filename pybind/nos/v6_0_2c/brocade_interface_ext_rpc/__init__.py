
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_vlan_brief
import get_interface_switchport
import get_ip_interface
import get_interface_detail
import get_media_detail
class brocade_interface_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface-ext - based on the path /brocade_interface_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module is an extension to interface model for 
 - Defining RPCs to retrieve interface related operational data
   in the managed device.
 
Glossary of the terms used:
--------------------------- 
HDLC - High-Level Data Link Control.
PPP  - Point-to-Point Protocol.
ATM  - Asynchronous Transfer Mode.
GBIC - Gigabit Interface Converter.
SFP  - small form-factor.
XFP  - 10 Gigabit Small Form Factor Pluggable.
xFF  -
XFP-E - XFP Extended.
ISL   - Inter switch Link.

  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__get_vlan_brief','__get_interface_switchport','__get_ip_interface','__get_interface_detail','__get_media_detail',)

  _yang_name = 'brocade-interface-ext'
  _rest_name = ''

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
    self.__get_ip_interface = YANGDynClass(base=get_ip_interface.get_ip_interface, is_leaf=True, yang_name="get-ip-interface", rest_name="get-ip-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    self.__get_media_detail = YANGDynClass(base=get_media_detail.get_media_detail, is_leaf=True, yang_name="get-media-detail", rest_name="get-media-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getmediaport-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    self.__get_interface_switchport = YANGDynClass(base=get_interface_switchport.get_interface_switchport, is_leaf=True, yang_name="get-interface-switchport", rest_name="get-interface-switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    self.__get_vlan_brief = YANGDynClass(base=get_vlan_brief.get_vlan_brief, is_leaf=True, yang_name="get-vlan-brief", rest_name="get-vlan-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    self.__get_interface_detail = YANGDynClass(base=get_interface_detail.get_interface_detail, is_leaf=True, yang_name="get-interface-detail", rest_name="get-interface-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_interface_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_get_vlan_brief(self):
    """
    Getter method for get_vlan_brief, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief (rpc)

    YANG Description: This is a function that returns operational data for a 
given vlan and enumeration of all the interfaces belonging 
to this vlan. The vlan output records are fetched similar
to the snmp get-next model. When no input is given to this
rpc, first set of vlan output records will be fetched. If
there are any more extra vlan output records that are there
to be fetched, the flag has-more at the end of the output
will be set to true and the next set of vlan records will
have to be fetched by querying with the last-vlan-id, in
get-next-request, as the input to this function, again.
When a vlan-id is  given as an input argument in the 
get-request case, only that corresponding vlan output 
record, if exists, will be fetched.
    """
    return self.__get_vlan_brief
      
  def _set_get_vlan_brief(self, v, load=False):
    """
    Setter method for get_vlan_brief, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vlan_brief is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vlan_brief() directly.

    YANG Description: This is a function that returns operational data for a 
given vlan and enumeration of all the interfaces belonging 
to this vlan. The vlan output records are fetched similar
to the snmp get-next model. When no input is given to this
rpc, first set of vlan output records will be fetched. If
there are any more extra vlan output records that are there
to be fetched, the flag has-more at the end of the output
will be set to true and the next set of vlan records will
have to be fetched by querying with the last-vlan-id, in
get-next-request, as the input to this function, again.
When a vlan-id is  given as an input argument in the 
get-request case, only that corresponding vlan output 
record, if exists, will be fetched.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vlan_brief.get_vlan_brief, is_leaf=True, yang_name="get-vlan-brief", rest_name="get-vlan-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vlan_brief must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vlan_brief.get_vlan_brief, is_leaf=True, yang_name="get-vlan-brief", rest_name="get-vlan-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_vlan_brief = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vlan_brief(self):
    self.__get_vlan_brief = YANGDynClass(base=get_vlan_brief.get_vlan_brief, is_leaf=True, yang_name="get-vlan-brief", rest_name="get-vlan-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)


  def _get_get_interface_switchport(self):
    """
    Getter method for get_interface_switchport, mapped from YANG variable /brocade_interface_ext_rpc/get_interface_switchport (rpc)

    YANG Description: This is a function that returns switch-port/L2 
characteristics of all the interfaces in the managed 
device.
    """
    return self.__get_interface_switchport
      
  def _set_get_interface_switchport(self, v, load=False):
    """
    Setter method for get_interface_switchport, mapped from YANG variable /brocade_interface_ext_rpc/get_interface_switchport (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_interface_switchport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_interface_switchport() directly.

    YANG Description: This is a function that returns switch-port/L2 
characteristics of all the interfaces in the managed 
device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_interface_switchport.get_interface_switchport, is_leaf=True, yang_name="get-interface-switchport", rest_name="get-interface-switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_interface_switchport must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_interface_switchport.get_interface_switchport, is_leaf=True, yang_name="get-interface-switchport", rest_name="get-interface-switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_interface_switchport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_interface_switchport(self):
    self.__get_interface_switchport = YANGDynClass(base=get_interface_switchport.get_interface_switchport, is_leaf=True, yang_name="get-interface-switchport", rest_name="get-interface-switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)


  def _get_get_ip_interface(self):
    """
    Getter method for get_ip_interface, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface (rpc)

    YANG Description: This is a function that serves to return brief details 
of all interfaces, loopback and VE interface details of  
particular managed entity. Phy interface details of 
particular managed entity cannot be given
    """
    return self.__get_ip_interface
      
  def _set_get_ip_interface(self, v, load=False):
    """
    Setter method for get_ip_interface, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_ip_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_ip_interface() directly.

    YANG Description: This is a function that serves to return brief details 
of all interfaces, loopback and VE interface details of  
particular managed entity. Phy interface details of 
particular managed entity cannot be given
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_ip_interface.get_ip_interface, is_leaf=True, yang_name="get-ip-interface", rest_name="get-ip-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_ip_interface must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_ip_interface.get_ip_interface, is_leaf=True, yang_name="get-ip-interface", rest_name="get-ip-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_ip_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_ip_interface(self):
    self.__get_ip_interface = YANGDynClass(base=get_ip_interface.get_ip_interface, is_leaf=True, yang_name="get-ip-interface", rest_name="get-ip-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)


  def _get_get_interface_detail(self):
    """
    Getter method for get_interface_detail, mapped from YANG variable /brocade_interface_ext_rpc/get_interface_detail (rpc)

    YANG Description: This is a function that serves to return all the possible
interfaces of the managed entity. This function can be used
to discover basic characteristics of all the interfaces in
the system. Each sub-layer below the internetwork-layer of
a network interface is considered to be an interface.
    """
    return self.__get_interface_detail
      
  def _set_get_interface_detail(self, v, load=False):
    """
    Setter method for get_interface_detail, mapped from YANG variable /brocade_interface_ext_rpc/get_interface_detail (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_interface_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_interface_detail() directly.

    YANG Description: This is a function that serves to return all the possible
interfaces of the managed entity. This function can be used
to discover basic characteristics of all the interfaces in
the system. Each sub-layer below the internetwork-layer of
a network interface is considered to be an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_interface_detail.get_interface_detail, is_leaf=True, yang_name="get-interface-detail", rest_name="get-interface-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_interface_detail must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_interface_detail.get_interface_detail, is_leaf=True, yang_name="get-interface-detail", rest_name="get-interface-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_interface_detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_interface_detail(self):
    self.__get_interface_detail = YANGDynClass(base=get_interface_detail.get_interface_detail, is_leaf=True, yang_name="get-interface-detail", rest_name="get-interface-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getinterfaceall-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)


  def _get_get_media_detail(self):
    """
    Getter method for get_media_detail, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail (rpc)

    YANG Description: This is a function that serves to return the media 
properities of all the interfaces of the managed entity.
    """
    return self.__get_media_detail
      
  def _set_get_media_detail(self, v, load=False):
    """
    Setter method for get_media_detail, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_media_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_media_detail() directly.

    YANG Description: This is a function that serves to return the media 
properities of all the interfaces of the managed entity.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_media_detail.get_media_detail, is_leaf=True, yang_name="get-media-detail", rest_name="get-media-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getmediaport-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_media_detail must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_media_detail.get_media_detail, is_leaf=True, yang_name="get-media-detail", rest_name="get-media-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getmediaport-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_media_detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_media_detail(self):
    self.__get_media_detail = YANGDynClass(base=get_media_detail.get_media_detail, is_leaf=True, yang_name="get-media-detail", rest_name="get-media-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getmediaport-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='rpc', is_config=True)

  get_vlan_brief = __builtin__.property(_get_get_vlan_brief, _set_get_vlan_brief)
  get_interface_switchport = __builtin__.property(_get_get_interface_switchport, _set_get_interface_switchport)
  get_ip_interface = __builtin__.property(_get_get_ip_interface, _set_get_ip_interface)
  get_interface_detail = __builtin__.property(_get_get_interface_detail, _set_get_interface_detail)
  get_media_detail = __builtin__.property(_get_get_media_detail, _set_get_media_detail)


  _pyangbind_elements = {'get_vlan_brief': get_vlan_brief, 'get_interface_switchport': get_interface_switchport, 'get_ip_interface': get_ip_interface, 'get_interface_detail': get_interface_detail, 'get_media_detail': get_media_detail, }

