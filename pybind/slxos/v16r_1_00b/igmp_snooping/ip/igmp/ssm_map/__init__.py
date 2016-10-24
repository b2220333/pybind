
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import igmps_prefix_list
class ssm_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-igmp-snooping - based on the path /igmp-snooping/ip/igmp/ssm-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__igmps_ssmmap','__igmps_prefix_list',)

  _yang_name = 'ssm-map'
  _rest_name = 'ssm-map'

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
    self.__igmps_prefix_list = YANGDynClass(base=YANGListType("igmps_prefix_list_name igmps_prefix_src_addr",igmps_prefix_list.igmps_prefix_list, yang_name="igmps-prefix-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-prefix-list-name igmps-prefix-src-addr', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-prefix-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)
    self.__igmps_ssmmap = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-ssmmap", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enables IGMPv2 SSM Mapping', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)

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
      return [u'igmp-snooping', u'ip', u'igmp', u'ssm-map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ip', u'igmp', u'ssm-map']

  def _get_igmps_ssmmap(self):
    """
    Getter method for igmps_ssmmap, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_ssmmap (empty)
    """
    return self.__igmps_ssmmap
      
  def _set_igmps_ssmmap(self, v, load=False):
    """
    Setter method for igmps_ssmmap, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_ssmmap (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_ssmmap is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_ssmmap() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igmps-ssmmap", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enables IGMPv2 SSM Mapping', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_ssmmap must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-ssmmap", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enables IGMPv2 SSM Mapping', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)""",
        })

    self.__igmps_ssmmap = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_ssmmap(self):
    self.__igmps_ssmmap = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-ssmmap", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enables IGMPv2 SSM Mapping', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)


  def _get_igmps_prefix_list(self):
    """
    Getter method for igmps_prefix_list, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_prefix_list (list)
    """
    return self.__igmps_prefix_list
      
  def _set_igmps_prefix_list(self, v, load=False):
    """
    Setter method for igmps_prefix_list, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_prefix_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_prefix_list() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("igmps_prefix_list_name igmps_prefix_src_addr",igmps_prefix_list.igmps_prefix_list, yang_name="igmps-prefix-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-prefix-list-name igmps-prefix-src-addr', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-prefix-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_prefix_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("igmps_prefix_list_name igmps_prefix_src_addr",igmps_prefix_list.igmps_prefix_list, yang_name="igmps-prefix-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-prefix-list-name igmps-prefix-src-addr', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-prefix-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)""",
        })

    self.__igmps_prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_prefix_list(self):
    self.__igmps_prefix_list = YANGDynClass(base=YANGListType("igmps_prefix_list_name igmps_prefix_src_addr",igmps_prefix_list.igmps_prefix_list, yang_name="igmps-prefix-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-prefix-list-name igmps-prefix-src-addr', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-prefix-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IgmpsPrefixList', u'cli-suppress-mode': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)

  igmps_ssmmap = __builtin__.property(_get_igmps_ssmmap, _set_igmps_ssmmap)
  igmps_prefix_list = __builtin__.property(_get_igmps_prefix_list, _set_igmps_prefix_list)


  _pyangbind_elements = {'igmps_ssmmap': igmps_ssmmap, 'igmps_prefix_list': igmps_prefix_list, }


