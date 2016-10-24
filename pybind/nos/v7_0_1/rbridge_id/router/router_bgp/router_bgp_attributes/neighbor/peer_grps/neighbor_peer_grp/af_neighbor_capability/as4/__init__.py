
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class as4(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/neighbor/peer-grps/neighbor-peer-grp/af-neighbor-capability/as4. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__neighbor_as4_enable','__neighbor_as4_disable',)

  _yang_name = 'as4'
  _rest_name = 'as4'

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
    self.__neighbor_as4_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-as4-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable AS4 capability', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__neighbor_as4_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-as4-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable AS4 capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'peer-grps', u'neighbor-peer-grp', u'af-neighbor-capability', u'as4']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'neighbor', u'capability', u'as4']

  def _get_neighbor_as4_enable(self):
    """
    Getter method for neighbor_as4_enable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/af_neighbor_capability/as4/neighbor_as4_enable (empty)
    """
    return self.__neighbor_as4_enable
      
  def _set_neighbor_as4_enable(self, v, load=False):
    """
    Setter method for neighbor_as4_enable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/af_neighbor_capability/as4/neighbor_as4_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_as4_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_as4_enable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="neighbor-as4-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable AS4 capability', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_as4_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-as4-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable AS4 capability', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__neighbor_as4_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_as4_enable(self):
    self.__neighbor_as4_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-as4-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable AS4 capability', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_neighbor_as4_disable(self):
    """
    Getter method for neighbor_as4_disable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/af_neighbor_capability/as4/neighbor_as4_disable (empty)
    """
    return self.__neighbor_as4_disable
      
  def _set_neighbor_as4_disable(self, v, load=False):
    """
    Setter method for neighbor_as4_disable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/af_neighbor_capability/as4/neighbor_as4_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_as4_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_as4_disable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="neighbor-as4-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable AS4 capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_as4_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-as4-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable AS4 capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__neighbor_as4_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_as4_disable(self):
    self.__neighbor_as4_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-as4-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable AS4 capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  neighbor_as4_enable = __builtin__.property(_get_neighbor_as4_enable, _set_neighbor_as4_enable)
  neighbor_as4_disable = __builtin__.property(_get_neighbor_as4_disable, _set_neighbor_as4_disable)


  _pyangbind_elements = {'neighbor_as4_enable': neighbor_as4_enable, 'neighbor_as4_disable': neighbor_as4_disable, }


