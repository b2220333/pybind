
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/route-map/content/match/ip/address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Route address
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__prefix_list_rmm','__acl_rmm',)

  _yang_name = 'address'
  _rest_name = 'address'

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
    self.__prefix_list_rmm = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="prefix-list-rmm", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-prefix-name-t', is_config=True)
    self.__acl_rmm = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="acl-rmm", rest_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP ACL', u'alt-name': u'acl'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)

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
      return [u'routing-system', u'route-map', u'content', u'match', u'ip', u'address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'match', u'ip', u'address']

  def _get_prefix_list_rmm(self):
    """
    Getter method for prefix_list_rmm, mapped from YANG variable /routing_system/route_map/content/match/ip/address/prefix_list_rmm (ip-prefix-name-t)

    YANG Description: IP prefix-list
    """
    return self.__prefix_list_rmm
      
  def _set_prefix_list_rmm(self, v, load=False):
    """
    Setter method for prefix_list_rmm, mapped from YANG variable /routing_system/route_map/content/match/ip/address/prefix_list_rmm (ip-prefix-name-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list_rmm() directly.

    YANG Description: IP prefix-list
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="prefix-list-rmm", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-prefix-name-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list_rmm must be of a type compatible with ip-prefix-name-t""",
          'defined-type': "brocade-ip-policy:ip-prefix-name-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="prefix-list-rmm", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-prefix-name-t', is_config=True)""",
        })

    self.__prefix_list_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list_rmm(self):
    self.__prefix_list_rmm = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="prefix-list-rmm", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-prefix-name-t', is_config=True)


  def _get_acl_rmm(self):
    """
    Getter method for acl_rmm, mapped from YANG variable /routing_system/route_map/content/match/ip/address/acl_rmm (ip-access-list:l3-acl-policy-name)

    YANG Description: IP ACL
    """
    return self.__acl_rmm
      
  def _set_acl_rmm(self, v, load=False):
    """
    Setter method for acl_rmm, mapped from YANG variable /routing_system/route_map/content/match/ip/address/acl_rmm (ip-access-list:l3-acl-policy-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_acl_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_acl_rmm() directly.

    YANG Description: IP ACL
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="acl-rmm", rest_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP ACL', u'alt-name': u'acl'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """acl_rmm must be of a type compatible with ip-access-list:l3-acl-policy-name""",
          'defined-type': "ip-access-list:l3-acl-policy-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="acl-rmm", rest_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP ACL', u'alt-name': u'acl'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)""",
        })

    self.__acl_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_acl_rmm(self):
    self.__acl_rmm = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="acl-rmm", rest_name="acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP ACL', u'alt-name': u'acl'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)

  prefix_list_rmm = __builtin__.property(_get_prefix_list_rmm, _set_prefix_list_rmm)
  acl_rmm = __builtin__.property(_get_acl_rmm, _set_acl_rmm)


  _pyangbind_elements = {'prefix_list_rmm': prefix_list_rmm, 'acl_rmm': acl_rmm, }


