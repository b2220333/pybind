
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class isns_discovery_domain_set(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isns - based on the path /isns/isns-vrf/isns-discovery-domain-set. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of Discovery Domain Set Parameters.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__isns_discovery_domain_set_name','__isns_discovery_domain_set_enable','__isns_dds_discovery_domain',)

  _yang_name = 'isns-discovery-domain-set'
  _rest_name = 'discovery-domain-set'

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
    self.__isns_discovery_domain_set_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isns-discovery-domain-set-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Discovery Domain Set', u'hidden': u'isns-discovery-domain-set-enable', u'alt-name': u'enable', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='empty', is_config=True)
    self.__isns_discovery_domain_set_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-discovery-domain-set-name", rest_name="isns-discovery-domain-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'iSNS Discovery Domain Set Name (Max Size - 256)', u'cli-drop-node-name': None, u'hidden': u'isns-discovery-domain-set-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dds-name-type', is_config=True)
    self.__isns_dds_discovery_domain = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']})), is_leaf=False, yang_name="isns-dds-discovery-domain", rest_name="discovery-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure isns discovery domain for Discovery Domain Set', u'cli-flat-list-syntax': None, u'hidden': u'isns-dds-discovery-domain', u'alt-name': u'discovery-domain'}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dd-name-type', is_config=True)

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
      return [u'isns', u'isns-vrf', u'isns-discovery-domain-set']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isns', u'vrf-forwarding', u'discovery-domain-set']

  def _get_isns_discovery_domain_set_name(self):
    """
    Getter method for isns_discovery_domain_set_name, mapped from YANG variable /isns/isns_vrf/isns_discovery_domain_set/isns_discovery_domain_set_name (isns-dds-name-type)

    YANG Description: This specifies the name for the Discovery Domain Set.
    """
    return self.__isns_discovery_domain_set_name
      
  def _set_isns_discovery_domain_set_name(self, v, load=False):
    """
    Setter method for isns_discovery_domain_set_name, mapped from YANG variable /isns/isns_vrf/isns_discovery_domain_set/isns_discovery_domain_set_name (isns-dds-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_discovery_domain_set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_discovery_domain_set_name() directly.

    YANG Description: This specifies the name for the Discovery Domain Set.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-discovery-domain-set-name", rest_name="isns-discovery-domain-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'iSNS Discovery Domain Set Name (Max Size - 256)', u'cli-drop-node-name': None, u'hidden': u'isns-discovery-domain-set-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dds-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_discovery_domain_set_name must be of a type compatible with isns-dds-name-type""",
          'defined-type': "brocade-isns:isns-dds-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-discovery-domain-set-name", rest_name="isns-discovery-domain-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'iSNS Discovery Domain Set Name (Max Size - 256)', u'cli-drop-node-name': None, u'hidden': u'isns-discovery-domain-set-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dds-name-type', is_config=True)""",
        })

    self.__isns_discovery_domain_set_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_discovery_domain_set_name(self):
    self.__isns_discovery_domain_set_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-discovery-domain-set-name", rest_name="isns-discovery-domain-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'iSNS Discovery Domain Set Name (Max Size - 256)', u'cli-drop-node-name': None, u'hidden': u'isns-discovery-domain-set-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dds-name-type', is_config=True)


  def _get_isns_discovery_domain_set_enable(self):
    """
    Getter method for isns_discovery_domain_set_enable, mapped from YANG variable /isns/isns_vrf/isns_discovery_domain_set/isns_discovery_domain_set_enable (empty)

    YANG Description: This specifies how to enable Discovery Domain Set.
    """
    return self.__isns_discovery_domain_set_enable
      
  def _set_isns_discovery_domain_set_enable(self, v, load=False):
    """
    Setter method for isns_discovery_domain_set_enable, mapped from YANG variable /isns/isns_vrf/isns_discovery_domain_set/isns_discovery_domain_set_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_discovery_domain_set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_discovery_domain_set_enable() directly.

    YANG Description: This specifies how to enable Discovery Domain Set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="isns-discovery-domain-set-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Discovery Domain Set', u'hidden': u'isns-discovery-domain-set-enable', u'alt-name': u'enable', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_discovery_domain_set_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isns-discovery-domain-set-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Discovery Domain Set', u'hidden': u'isns-discovery-domain-set-enable', u'alt-name': u'enable', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='empty', is_config=True)""",
        })

    self.__isns_discovery_domain_set_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_discovery_domain_set_enable(self):
    self.__isns_discovery_domain_set_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isns-discovery-domain-set-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Discovery Domain Set', u'hidden': u'isns-discovery-domain-set-enable', u'alt-name': u'enable', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='empty', is_config=True)


  def _get_isns_dds_discovery_domain(self):
    """
    Getter method for isns_dds_discovery_domain, mapped from YANG variable /isns/isns_vrf/isns_discovery_domain_set/isns_dds_discovery_domain (isns-dd-name-type)

    YANG Description: This specifies the discovery domain under discovery domain set.
    """
    return self.__isns_dds_discovery_domain
      
  def _set_isns_dds_discovery_domain(self, v, load=False):
    """
    Setter method for isns_dds_discovery_domain, mapped from YANG variable /isns/isns_vrf/isns_discovery_domain_set/isns_dds_discovery_domain (isns-dd-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_dds_discovery_domain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_dds_discovery_domain() directly.

    YANG Description: This specifies the discovery domain under discovery domain set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']})), is_leaf=False, yang_name="isns-dds-discovery-domain", rest_name="discovery-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure isns discovery domain for Discovery Domain Set', u'cli-flat-list-syntax': None, u'hidden': u'isns-dds-discovery-domain', u'alt-name': u'discovery-domain'}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dd-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_dds_discovery_domain must be of a type compatible with isns-dd-name-type""",
          'defined-type': "brocade-isns:isns-dd-name-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']})), is_leaf=False, yang_name="isns-dds-discovery-domain", rest_name="discovery-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure isns discovery domain for Discovery Domain Set', u'cli-flat-list-syntax': None, u'hidden': u'isns-dds-discovery-domain', u'alt-name': u'discovery-domain'}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dd-name-type', is_config=True)""",
        })

    self.__isns_dds_discovery_domain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_dds_discovery_domain(self):
    self.__isns_dds_discovery_domain = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']})), is_leaf=False, yang_name="isns-dds-discovery-domain", rest_name="discovery-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure isns discovery domain for Discovery Domain Set', u'cli-flat-list-syntax': None, u'hidden': u'isns-dds-discovery-domain', u'alt-name': u'discovery-domain'}}, namespace='urn:brocade.com:mgmt:brocade-isns', defining_module='brocade-isns', yang_type='isns-dd-name-type', is_config=True)

  isns_discovery_domain_set_name = __builtin__.property(_get_isns_discovery_domain_set_name, _set_isns_discovery_domain_set_name)
  isns_discovery_domain_set_enable = __builtin__.property(_get_isns_discovery_domain_set_enable, _set_isns_discovery_domain_set_enable)
  isns_dds_discovery_domain = __builtin__.property(_get_isns_dds_discovery_domain, _set_isns_dds_discovery_domain)


  _pyangbind_elements = {'isns_discovery_domain_set_name': isns_discovery_domain_set_name, 'isns_discovery_domain_set_enable': isns_discovery_domain_set_enable, 'isns_dds_discovery_domain': isns_dds_discovery_domain, }


