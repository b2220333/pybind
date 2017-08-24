
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ip
import map_
import site
import access_lists
class overlay_gateway(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__gw_type','__ip','__map_','__site','__access_lists','__activate',)

  _yang_name = 'overlay-gateway'
  _rest_name = 'overlay-gateway'

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
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the Overlay Gateway instance'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-name-type', is_config=True)
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address configuration for the Overlay Gateway', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__site = YANGDynClass(base=YANGListType("name",site.site, yang_name="site", rest_name="site", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}), is_container='list', yang_name="site", rest_name="site", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)
    self.__access_lists = YANGDynClass(base=access_lists.access_lists, is_container='container', presence=False, yang_name="access-lists", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__gw_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'layer2-extension': {'value': 2}},), is_leaf=True, yang_name="gw-type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the type of Overlay Gateway.', u'alt-name': u'type', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-type', is_config=True)
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the vlan to vni mappings for the Overlay Gateway.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)

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
      return [u'overlay-gateway']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-gateway']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /overlay_gateway/name (overlay-gw-name-type)

    YANG Description: Name of Overlay Gateway
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /overlay_gateway/name (overlay-gw-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of Overlay Gateway
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with overlay-gw-name-type""",
          'defined-type': "brocade-tunnels:overlay-gw-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-name-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-name-type', is_config=True)


  def _get_gw_type(self):
    """
    Getter method for gw_type, mapped from YANG variable /overlay_gateway/gw_type (overlay-gw-type)

    YANG Description: Defines type of function provided by this gateway.
    """
    return self.__gw_type
      
  def _set_gw_type(self, v, load=False):
    """
    Setter method for gw_type, mapped from YANG variable /overlay_gateway/gw_type (overlay-gw-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gw_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gw_type() directly.

    YANG Description: Defines type of function provided by this gateway.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'layer2-extension': {'value': 2}},), is_leaf=True, yang_name="gw-type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the type of Overlay Gateway.', u'alt-name': u'type', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gw_type must be of a type compatible with overlay-gw-type""",
          'defined-type': "brocade-tunnels:overlay-gw-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'layer2-extension': {'value': 2}},), is_leaf=True, yang_name="gw-type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the type of Overlay Gateway.', u'alt-name': u'type', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-type', is_config=True)""",
        })

    self.__gw_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gw_type(self):
    self.__gw_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'layer2-extension': {'value': 2}},), is_leaf=True, yang_name="gw-type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the type of Overlay Gateway.', u'alt-name': u'type', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='overlay-gw-type', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /overlay_gateway/ip (container)
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /overlay_gateway/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address configuration for the Overlay Gateway', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address configuration for the Overlay Gateway', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address configuration for the Overlay Gateway', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_map_(self):
    """
    Getter method for map_, mapped from YANG variable /overlay_gateway/map (container)
    """
    return self.__map_
      
  def _set_map_(self, v, load=False):
    """
    Setter method for map_, mapped from YANG variable /overlay_gateway/map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the vlan to vni mappings for the Overlay Gateway.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the vlan to vni mappings for the Overlay Gateway.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__map_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_(self):
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the vlan to vni mappings for the Overlay Gateway.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_site(self):
    """
    Getter method for site, mapped from YANG variable /overlay_gateway/site (list)

    YANG Description: Site represents a remote VCS to which tunnel need to be
setup. Site is identified by a name.
    """
    return self.__site
      
  def _set_site(self, v, load=False):
    """
    Setter method for site, mapped from YANG variable /overlay_gateway/site (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_site is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_site() directly.

    YANG Description: Site represents a remote VCS to which tunnel need to be
setup. Site is identified by a name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",site.site, yang_name="site", rest_name="site", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}), is_container='list', yang_name="site", rest_name="site", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """site must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",site.site, yang_name="site", rest_name="site", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}), is_container='list', yang_name="site", rest_name="site", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)""",
        })

    self.__site = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_site(self):
    self.__site = YANGDynClass(base=YANGListType("name",site.site, yang_name="site", rest_name="site", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}), is_container='list', yang_name="site", rest_name="site", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure remote extension site', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'overlay-site-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)


  def _get_access_lists(self):
    """
    Getter method for access_lists, mapped from YANG variable /overlay_gateway/access_lists (container)
    """
    return self.__access_lists
      
  def _set_access_lists(self, v, load=False):
    """
    Setter method for access_lists, mapped from YANG variable /overlay_gateway/access_lists (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_lists is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_lists() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access_lists.access_lists, is_container='container', presence=False, yang_name="access-lists", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_lists must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_lists.access_lists, is_container='container', presence=False, yang_name="access-lists", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__access_lists = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_lists(self):
    self.__access_lists = YANGDynClass(base=access_lists.access_lists, is_container='container', presence=False, yang_name="access-lists", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_activate(self):
    """
    Getter method for activate, mapped from YANG variable /overlay_gateway/activate (empty)

    YANG Description: Activates the Overlay gateway instance. Gateway is
inactive by default. When gateway is inactive all
associated tunnels will also be inactive (oper down).
    """
    return self.__activate
      
  def _set_activate(self, v, load=False):
    """
    Setter method for activate, mapped from YANG variable /overlay_gateway/activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_activate() directly.

    YANG Description: Activates the Overlay gateway instance. Gateway is
inactive by default. When gateway is inactive all
associated tunnels will also be inactive (oper down).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the Overlay Gateway instance'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the Overlay Gateway instance'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)""",
        })

    self.__activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_activate(self):
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the Overlay Gateway instance'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  gw_type = __builtin__.property(_get_gw_type, _set_gw_type)
  ip = __builtin__.property(_get_ip, _set_ip)
  map_ = __builtin__.property(_get_map_, _set_map_)
  site = __builtin__.property(_get_site, _set_site)
  access_lists = __builtin__.property(_get_access_lists, _set_access_lists)
  activate = __builtin__.property(_get_activate, _set_activate)


  _pyangbind_elements = {'name': name, 'gw_type': gw_type, 'ip': ip, 'map_': map_, 'site': site, 'access_lists': access_lists, 'activate': activate, }


