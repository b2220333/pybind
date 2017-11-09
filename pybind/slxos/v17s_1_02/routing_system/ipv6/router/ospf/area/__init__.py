
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import nssa
import stub
import authentication
import virtual_link
import area_range
class area(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/area. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Set the OSPF router area id
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__area_id','__normal','__nssa','__stub','__authentication','__virtual_link','__area_range',)

  _yang_name = 'area'
  _rest_name = 'area'

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
    self.__area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:ospf-area-id', is_config=True)
    self.__normal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__nssa = YANGDynClass(base=nssa.nssa, is_container='container', presence=True, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify an nssa area', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__stub = YANGDynClass(base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify a stub area', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__virtual_link = YANGDynClass(base=YANGListType("virtual_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-link-neighbor', extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)
    self.__area_range = YANGDynClass(base=YANGListType("range_address",area_range.area_range, yang_name="area-range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address', extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}), is_container='list', yang_name="area-range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'area']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'area']

  def _get_area_id(self):
    """
    Getter method for area_id, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_id (ospf:ospf-area-id)
    """
    return self.__area_id
      
  def _set_area_id(self, v, load=False):
    """
    Setter method for area_id, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_id (ospf:ospf-area-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_area_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_area_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:ospf-area-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """area_id must be of a type compatible with ospf:ospf-area-id""",
          'defined-type': "ospf:ospf-area-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:ospf-area-id', is_config=True)""",
        })

    self.__area_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_area_id(self):
    self.__area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:ospf-area-id', is_config=True)


  def _get_normal(self):
    """
    Getter method for normal, mapped from YANG variable /routing_system/ipv6/router/ospf/area/normal (empty)
    """
    return self.__normal
      
  def _set_normal(self, v, load=False):
    """
    Setter method for normal, mapped from YANG variable /routing_system/ipv6/router/ospf/area/normal (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_normal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_normal() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """normal must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__normal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_normal(self):
    self.__normal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)


  def _get_nssa(self):
    """
    Getter method for nssa, mapped from YANG variable /routing_system/ipv6/router/ospf/area/nssa (container)

    YANG Description: Specify the area as a Not-So-Stubby Area.NSSA allows to configure OSPF areas that provide the benefits of stub areas, but that also are capable of importing external route information. OSPF does not flood external routes from other areas into an NSSA, but does translate and flood route information from the NSSA into other areas such as the backbone. NSSAs are especially useful to summarize Type-5 External LSAs (external routes) before forwarding them into an area. The OSPF specification (RFC 2328) prohibits summarization of Type-5 LSAs and requires OSPF to flood Type-5 LSAs throughout a routing domain. With NSSA, it is possible specify an address range for aggregating the external routes that the NSSAs ABR exports into other areas.Since the NSSA is partially 'stubby' the ABR does not flood external LSAs from the backbone into the NSSA.To provide access to the rest of the Autonomous System (AS), the ABR generates a default Type-7 LSA into the NSSA.
    """
    return self.__nssa
      
  def _set_nssa(self, v, load=False):
    """
    Setter method for nssa, mapped from YANG variable /routing_system/ipv6/router/ospf/area/nssa (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nssa is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nssa() directly.

    YANG Description: Specify the area as a Not-So-Stubby Area.NSSA allows to configure OSPF areas that provide the benefits of stub areas, but that also are capable of importing external route information. OSPF does not flood external routes from other areas into an NSSA, but does translate and flood route information from the NSSA into other areas such as the backbone. NSSAs are especially useful to summarize Type-5 External LSAs (external routes) before forwarding them into an area. The OSPF specification (RFC 2328) prohibits summarization of Type-5 LSAs and requires OSPF to flood Type-5 LSAs throughout a routing domain. With NSSA, it is possible specify an address range for aggregating the external routes that the NSSAs ABR exports into other areas.Since the NSSA is partially 'stubby' the ABR does not flood external LSAs from the backbone into the NSSA.To provide access to the rest of the Autonomous System (AS), the ABR generates a default Type-7 LSA into the NSSA.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=nssa.nssa, is_container='container', presence=True, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify an nssa area', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nssa must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=nssa.nssa, is_container='container', presence=True, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify an nssa area', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__nssa = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nssa(self):
    self.__nssa = YANGDynClass(base=nssa.nssa, is_container='container', presence=True, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify an nssa area', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_stub(self):
    """
    Getter method for stub, mapped from YANG variable /routing_system/ipv6/router/ospf/area/stub (container)

    YANG Description: Specify the area as a stub area.OSPFv3 routers within a stub area cannot send or receive External LSAs. In addition,routers in a stub area must use a default route to the area's Area Border Router (ABR) orAutonomous System Boundary Router (ASBR) to send traffic out of the area.
    """
    return self.__stub
      
  def _set_stub(self, v, load=False):
    """
    Setter method for stub, mapped from YANG variable /routing_system/ipv6/router/ospf/area/stub (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stub is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stub() directly.

    YANG Description: Specify the area as a stub area.OSPFv3 routers within a stub area cannot send or receive External LSAs. In addition,routers in a stub area must use a default route to the area's Area Border Router (ABR) orAutonomous System Boundary Router (ASBR) to send traffic out of the area.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify a stub area', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stub must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify a stub area', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__stub = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stub(self):
    self.__stub = YANGDynClass(base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Specify a stub area', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_authentication(self):
    """
    Getter method for authentication, mapped from YANG variable /routing_system/ipv6/router/ospf/area/authentication (container)

    YANG Description: Authentication of OSPF messages
    """
    return self.__authentication
      
  def _set_authentication(self, v, load=False):
    """
    Setter method for authentication, mapped from YANG variable /routing_system/ipv6/router/ospf/area/authentication (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication() directly.

    YANG Description: Authentication of OSPF messages
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication(self):
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_virtual_link(self):
    """
    Getter method for virtual_link, mapped from YANG variable /routing_system/ipv6/router/ospf/area/virtual_link (list)

    YANG Description: All ABRs must have either a direct or indirect link to an OSPF backbone area (0.0.0.0 or 0). If an ABR does not have a physical link to a backbone area, a virtual link can be configured from the ABR to another router within the same area that has a physical connection to the backbone area.The path for a virtual link is through an area shared by the neighbor ABR (router with a physical backbone connection) and the ABR requiring a logical connection to the backbone.
    """
    return self.__virtual_link
      
  def _set_virtual_link(self, v, load=False):
    """
    Setter method for virtual_link, mapped from YANG variable /routing_system/ipv6/router/ospf/area/virtual_link (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_link() directly.

    YANG Description: All ABRs must have either a direct or indirect link to an OSPF backbone area (0.0.0.0 or 0). If an ABR does not have a physical link to a backbone area, a virtual link can be configured from the ABR to another router within the same area that has a physical connection to the backbone area.The path for a virtual link is through an area shared by the neighbor ABR (router with a physical backbone connection) and the ABR requiring a logical connection to the backbone.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("virtual_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-link-neighbor', extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_link must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("virtual_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-link-neighbor', extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)""",
        })

    self.__virtual_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_link(self):
    self.__virtual_link = YANGDynClass(base=YANGListType("virtual_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-link-neighbor', extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define a virtual link and its parameters', u'cli-suppress-mode': None, u'callpoint': u'Ospfv3VirtualLink', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)


  def _get_area_range(self):
    """
    Getter method for area_range, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range (list)

    YANG Description: If the ABR that connects the NSSA to other areas needs to summarize the routes in the NSSA before translating them into Type-5 LSAs and flooding them into the other areas, configure an address range. The ABR creates an aggregate value based on the address range. The aggregate value becomes the address that the ABR advertises instead of advertising the individual addresses represented by the aggregate.
    """
    return self.__area_range
      
  def _set_area_range(self, v, load=False):
    """
    Setter method for area_range, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_area_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_area_range() directly.

    YANG Description: If the ABR that connects the NSSA to other areas needs to summarize the routes in the NSSA before translating them into Type-5 LSAs and flooding them into the other areas, configure an address range. The ABR creates an aggregate value based on the address range. The aggregate value becomes the address that the ABR advertises instead of advertising the individual addresses represented by the aggregate.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("range_address",area_range.area_range, yang_name="area-range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address', extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}), is_container='list', yang_name="area-range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """area_range must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("range_address",area_range.area_range, yang_name="area-range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address', extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}), is_container='list', yang_name="area-range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)""",
        })

    self.__area_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_area_range(self):
    self.__area_range = YANGDynClass(base=YANGListType("range_address",area_range.area_range, yang_name="area-range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address', extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}), is_container='list', yang_name="area-range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To define or undefine a type-3 address range (ABR only)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'range', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'Ospfv3AreaRange'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='list', is_config=True)

  area_id = __builtin__.property(_get_area_id, _set_area_id)
  normal = __builtin__.property(_get_normal, _set_normal)
  nssa = __builtin__.property(_get_nssa, _set_nssa)
  stub = __builtin__.property(_get_stub, _set_stub)
  authentication = __builtin__.property(_get_authentication, _set_authentication)
  virtual_link = __builtin__.property(_get_virtual_link, _set_virtual_link)
  area_range = __builtin__.property(_get_area_range, _set_area_range)


  _pyangbind_elements = {'area_id': area_id, 'normal': normal, 'nssa': nssa, 'stub': stub, 'authentication': authentication, 'virtual_link': virtual_link, 'area_range': area_range, }


