
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class priority_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-cee - based on the path /cee-map/priority-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure Priority Table
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_cos0_pgid','__map_cos1_pgid','__map_cos2_pgid','__map_cos3_pgid','__map_cos4_pgid','__map_cos5_pgid','__map_cos6_pgid','__map_cos7_pgid',)

  _yang_name = 'priority-table'
  _rest_name = 'priority-table'

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
    self.__map_cos3_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos3-pgid", rest_name="map-cos3-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    self.__map_cos2_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos2-pgid", rest_name="map-cos2-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    self.__map_cos7_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos7-pgid", rest_name="map-cos7-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    self.__map_cos6_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos6-pgid", rest_name="map-cos6-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    self.__map_cos5_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos5-pgid", rest_name="map-cos5-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    self.__map_cos4_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos4-pgid", rest_name="map-cos4-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    self.__map_cos1_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos1-pgid", rest_name="map-cos1-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    self.__map_cos0_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos0-pgid", rest_name="map-cos0-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)

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
      return [u'cee-map', u'priority-table']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cee-map', u'priority-table']

  def _get_map_cos0_pgid(self):
    """
    Getter method for map_cos0_pgid, mapped from YANG variable /cee_map/priority_table/map_cos0_pgid (string)
    """
    return self.__map_cos0_pgid
      
  def _set_map_cos0_pgid(self, v, load=False):
    """
    Setter method for map_cos0_pgid, mapped from YANG variable /cee_map/priority_table/map_cos0_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos0_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos0_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos0-pgid", rest_name="map-cos0-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos0_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos0-pgid", rest_name="map-cos0-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos0_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos0_pgid(self):
    self.__map_cos0_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos0-pgid", rest_name="map-cos0-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)


  def _get_map_cos1_pgid(self):
    """
    Getter method for map_cos1_pgid, mapped from YANG variable /cee_map/priority_table/map_cos1_pgid (string)
    """
    return self.__map_cos1_pgid
      
  def _set_map_cos1_pgid(self, v, load=False):
    """
    Setter method for map_cos1_pgid, mapped from YANG variable /cee_map/priority_table/map_cos1_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos1_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos1_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos1-pgid", rest_name="map-cos1-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos1_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos1-pgid", rest_name="map-cos1-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos1_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos1_pgid(self):
    self.__map_cos1_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos1-pgid", rest_name="map-cos1-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)


  def _get_map_cos2_pgid(self):
    """
    Getter method for map_cos2_pgid, mapped from YANG variable /cee_map/priority_table/map_cos2_pgid (string)
    """
    return self.__map_cos2_pgid
      
  def _set_map_cos2_pgid(self, v, load=False):
    """
    Setter method for map_cos2_pgid, mapped from YANG variable /cee_map/priority_table/map_cos2_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos2_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos2_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos2-pgid", rest_name="map-cos2-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos2_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos2-pgid", rest_name="map-cos2-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos2_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos2_pgid(self):
    self.__map_cos2_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos2-pgid", rest_name="map-cos2-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)


  def _get_map_cos3_pgid(self):
    """
    Getter method for map_cos3_pgid, mapped from YANG variable /cee_map/priority_table/map_cos3_pgid (string)
    """
    return self.__map_cos3_pgid
      
  def _set_map_cos3_pgid(self, v, load=False):
    """
    Setter method for map_cos3_pgid, mapped from YANG variable /cee_map/priority_table/map_cos3_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos3_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos3_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos3-pgid", rest_name="map-cos3-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos3_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos3-pgid", rest_name="map-cos3-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos3_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos3_pgid(self):
    self.__map_cos3_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos3-pgid", rest_name="map-cos3-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)


  def _get_map_cos4_pgid(self):
    """
    Getter method for map_cos4_pgid, mapped from YANG variable /cee_map/priority_table/map_cos4_pgid (string)
    """
    return self.__map_cos4_pgid
      
  def _set_map_cos4_pgid(self, v, load=False):
    """
    Setter method for map_cos4_pgid, mapped from YANG variable /cee_map/priority_table/map_cos4_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos4_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos4_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos4-pgid", rest_name="map-cos4-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos4_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos4-pgid", rest_name="map-cos4-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos4_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos4_pgid(self):
    self.__map_cos4_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos4-pgid", rest_name="map-cos4-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)


  def _get_map_cos5_pgid(self):
    """
    Getter method for map_cos5_pgid, mapped from YANG variable /cee_map/priority_table/map_cos5_pgid (string)
    """
    return self.__map_cos5_pgid
      
  def _set_map_cos5_pgid(self, v, load=False):
    """
    Setter method for map_cos5_pgid, mapped from YANG variable /cee_map/priority_table/map_cos5_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos5_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos5_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos5-pgid", rest_name="map-cos5-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos5_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos5-pgid", rest_name="map-cos5-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos5_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos5_pgid(self):
    self.__map_cos5_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos5-pgid", rest_name="map-cos5-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)


  def _get_map_cos6_pgid(self):
    """
    Getter method for map_cos6_pgid, mapped from YANG variable /cee_map/priority_table/map_cos6_pgid (string)
    """
    return self.__map_cos6_pgid
      
  def _set_map_cos6_pgid(self, v, load=False):
    """
    Setter method for map_cos6_pgid, mapped from YANG variable /cee_map/priority_table/map_cos6_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos6_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos6_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos6-pgid", rest_name="map-cos6-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos6_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos6-pgid", rest_name="map-cos6-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos6_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos6_pgid(self):
    self.__map_cos6_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos6-pgid", rest_name="map-cos6-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)


  def _get_map_cos7_pgid(self):
    """
    Getter method for map_cos7_pgid, mapped from YANG variable /cee_map/priority_table/map_cos7_pgid (string)
    """
    return self.__map_cos7_pgid
      
  def _set_map_cos7_pgid(self, v, load=False):
    """
    Setter method for map_cos7_pgid, mapped from YANG variable /cee_map/priority_table/map_cos7_pgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_cos7_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_cos7_pgid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos7-pgid", rest_name="map-cos7-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_cos7_pgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos7-pgid", rest_name="map-cos7-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)""",
        })

    self.__map_cos7_pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_cos7_pgid(self):
    self.__map_cos7_pgid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-7]|15\\.[0-7]', 'length': [u'1..32']}), is_leaf=True, yang_name="map-cos7-pgid", rest_name="map-cos7-pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='string', is_config=True)

  map_cos0_pgid = __builtin__.property(_get_map_cos0_pgid, _set_map_cos0_pgid)
  map_cos1_pgid = __builtin__.property(_get_map_cos1_pgid, _set_map_cos1_pgid)
  map_cos2_pgid = __builtin__.property(_get_map_cos2_pgid, _set_map_cos2_pgid)
  map_cos3_pgid = __builtin__.property(_get_map_cos3_pgid, _set_map_cos3_pgid)
  map_cos4_pgid = __builtin__.property(_get_map_cos4_pgid, _set_map_cos4_pgid)
  map_cos5_pgid = __builtin__.property(_get_map_cos5_pgid, _set_map_cos5_pgid)
  map_cos6_pgid = __builtin__.property(_get_map_cos6_pgid, _set_map_cos6_pgid)
  map_cos7_pgid = __builtin__.property(_get_map_cos7_pgid, _set_map_cos7_pgid)


  _pyangbind_elements = {'map_cos0_pgid': map_cos0_pgid, 'map_cos1_pgid': map_cos1_pgid, 'map_cos2_pgid': map_cos2_pgid, 'map_cos3_pgid': map_cos3_pgid, 'map_cos4_pgid': map_cos4_pgid, 'map_cos5_pgid': map_cos5_pgid, 'map_cos6_pgid': map_cos6_pgid, 'map_cos7_pgid': map_cos7_pgid, }


