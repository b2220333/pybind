
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class as_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/route-map/content/set/as-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Prepend string for a BGP AS-path attribute
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__aspath_tag','__prepend',)

  _yang_name = 'as-path'
  _rest_name = 'as-path'

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
    self.__aspath_tag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="aspath-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Tag as an AS-path attribute', u'alt-name': u'tag'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    self.__prepend = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*(\\d+))*'}), is_leaf=True, yang_name="prepend", rest_name="prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prepend to the AS-path', u'cli-full-command': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='string', is_config=True)

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
      return [u'routing-system', u'route-map', u'content', u'set', u'as-path']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'set', u'as-path']

  def _get_aspath_tag(self):
    """
    Getter method for aspath_tag, mapped from YANG variable /routing_system/route_map/content/set/as_path/aspath_tag (empty)

    YANG Description: Tag as an AS-path attribute
    """
    return self.__aspath_tag
      
  def _set_aspath_tag(self, v, load=False):
    """
    Setter method for aspath_tag, mapped from YANG variable /routing_system/route_map/content/set/as_path/aspath_tag (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aspath_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aspath_tag() directly.

    YANG Description: Tag as an AS-path attribute
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="aspath-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Tag as an AS-path attribute', u'alt-name': u'tag'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aspath_tag must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="aspath-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Tag as an AS-path attribute', u'alt-name': u'tag'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__aspath_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aspath_tag(self):
    self.__aspath_tag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="aspath-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Tag as an AS-path attribute', u'alt-name': u'tag'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)


  def _get_prepend(self):
    """
    Getter method for prepend, mapped from YANG variable /routing_system/route_map/content/set/as_path/prepend (string)
    """
    return self.__prepend
      
  def _set_prepend(self, v, load=False):
    """
    Setter method for prepend, mapped from YANG variable /routing_system/route_map/content/set/as_path/prepend (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prepend is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prepend() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*(\\d+))*'}), is_leaf=True, yang_name="prepend", rest_name="prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prepend to the AS-path', u'cli-full-command': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prepend must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*(\\d+))*'}), is_leaf=True, yang_name="prepend", rest_name="prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prepend to the AS-path', u'cli-full-command': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='string', is_config=True)""",
        })

    self.__prepend = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prepend(self):
    self.__prepend = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*(\\d+))*'}), is_leaf=True, yang_name="prepend", rest_name="prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prepend to the AS-path', u'cli-full-command': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='string', is_config=True)

  aspath_tag = __builtin__.property(_get_aspath_tag, _set_aspath_tag)
  prepend = __builtin__.property(_get_prepend, _set_prepend)


  _pyangbind_elements = {'aspath_tag': aspath_tag, 'prepend': prepend, }


