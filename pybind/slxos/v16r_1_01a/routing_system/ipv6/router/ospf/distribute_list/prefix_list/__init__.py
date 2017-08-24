
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class prefix_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/distribute-list/prefix-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Use prefix list to control routes learned by OSPFv3
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__distribute_list_prefix_list_name','__distribute_list_prefix_list_in',)

  _yang_name = 'prefix-list'
  _rest_name = 'prefix-list'

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
    self.__distribute_list_prefix_list_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="distribute-list-prefix-list-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inbound Filtering', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__distribute_list_prefix_list_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="distribute-list-prefix-list-name", rest_name="distribute-list-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list  name.', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'distribute-list', u'prefix-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'distribute-list', u'prefix-list']

  def _get_distribute_list_prefix_list_name(self):
    """
    Getter method for distribute_list_prefix_list_name, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/prefix_list/distribute_list_prefix_list_name (common-def:name-string63)

    YANG Description: Prefix list name.
    """
    return self.__distribute_list_prefix_list_name
      
  def _set_distribute_list_prefix_list_name(self, v, load=False):
    """
    Setter method for distribute_list_prefix_list_name, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/prefix_list/distribute_list_prefix_list_name (common-def:name-string63)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_distribute_list_prefix_list_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_distribute_list_prefix_list_name() directly.

    YANG Description: Prefix list name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="distribute-list-prefix-list-name", rest_name="distribute-list-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list  name.', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """distribute_list_prefix_list_name must be of a type compatible with common-def:name-string63""",
          'defined-type': "common-def:name-string63",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="distribute-list-prefix-list-name", rest_name="distribute-list-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list  name.', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)""",
        })

    self.__distribute_list_prefix_list_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_distribute_list_prefix_list_name(self):
    self.__distribute_list_prefix_list_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="distribute-list-prefix-list-name", rest_name="distribute-list-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list  name.', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)


  def _get_distribute_list_prefix_list_in(self):
    """
    Getter method for distribute_list_prefix_list_in, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/prefix_list/distribute_list_prefix_list_in (empty)

    YANG Description: Apply filter for incoming Routes
    """
    return self.__distribute_list_prefix_list_in
      
  def _set_distribute_list_prefix_list_in(self, v, load=False):
    """
    Setter method for distribute_list_prefix_list_in, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/prefix_list/distribute_list_prefix_list_in (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_distribute_list_prefix_list_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_distribute_list_prefix_list_in() directly.

    YANG Description: Apply filter for incoming Routes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="distribute-list-prefix-list-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inbound Filtering', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """distribute_list_prefix_list_in must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="distribute-list-prefix-list-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inbound Filtering', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__distribute_list_prefix_list_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_distribute_list_prefix_list_in(self):
    self.__distribute_list_prefix_list_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="distribute-list-prefix-list-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inbound Filtering', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

  distribute_list_prefix_list_name = __builtin__.property(_get_distribute_list_prefix_list_name, _set_distribute_list_prefix_list_name)
  distribute_list_prefix_list_in = __builtin__.property(_get_distribute_list_prefix_list_in, _set_distribute_list_prefix_list_in)


  _pyangbind_elements = {'distribute_list_prefix_list_name': distribute_list_prefix_list_name, 'distribute_list_prefix_list_in': distribute_list_prefix_list_in, }


