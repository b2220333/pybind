
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import isns_device_list
class isns_entity_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isns-ext - based on the path /brocade_isns_ext_rpc/isns-get-device-brief/output/isns-entity-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This is a list of logged-in iSNS devices.
Each row represents a logged-in iSNS device
operational details such as entity id,
The entity id is used as the key for this
list as it will be unique for each entry.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__isns_device_entity_id','__isns_device_list',)

  _yang_name = 'isns-entity-list'
  _rest_name = 'isns-entity-list'

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
    self.__isns_device_entity_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-entity-id", rest_name="isns-device-entity-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-entity-id-type', is_config=True)
    self.__isns_device_list = YANGDynClass(base=YANGListType("isns_device_iqn",isns_device_list.isns_device_list, yang_name="isns-device-list", rest_name="isns-device-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='isns-device-iqn', extensions=None), is_container='list', yang_name="isns-device-list", rest_name="isns-device-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='list', is_config=True)

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
      return [u'brocade_isns_ext_rpc', u'isns-get-device-brief', u'output', u'isns-entity-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isns-get-device-brief', u'output', u'isns-entity-list']

  def _get_isns_device_entity_id(self):
    """
    Getter method for isns_device_entity_id, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_entity_id (isns-entity-id-type)

    YANG Description: This leaf indicates the fabric assigned
session MAC address of the End Node.
    """
    return self.__isns_device_entity_id
      
  def _set_isns_device_entity_id(self, v, load=False):
    """
    Setter method for isns_device_entity_id, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_entity_id (isns-entity-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_device_entity_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_device_entity_id() directly.

    YANG Description: This leaf indicates the fabric assigned
session MAC address of the End Node.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-entity-id", rest_name="isns-device-entity-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-entity-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_device_entity_id must be of a type compatible with isns-entity-id-type""",
          'defined-type': "brocade-isns-ext:isns-entity-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-entity-id", rest_name="isns-device-entity-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-entity-id-type', is_config=True)""",
        })

    self.__isns_device_entity_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_device_entity_id(self):
    self.__isns_device_entity_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-entity-id", rest_name="isns-device-entity-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-entity-id-type', is_config=True)


  def _get_isns_device_list(self):
    """
    Getter method for isns_device_list, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list (list)

    YANG Description: This is a list of logged-in iSNS devices.
Each row represents a logged-in iSNS device
operational details such as iqn,,
ip addressand device type.
The device iqn is used as the key for this
list as it will be unique for each entry.
    """
    return self.__isns_device_list
      
  def _set_isns_device_list(self, v, load=False):
    """
    Setter method for isns_device_list, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_device_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_device_list() directly.

    YANG Description: This is a list of logged-in iSNS devices.
Each row represents a logged-in iSNS device
operational details such as iqn,,
ip addressand device type.
The device iqn is used as the key for this
list as it will be unique for each entry.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("isns_device_iqn",isns_device_list.isns_device_list, yang_name="isns-device-list", rest_name="isns-device-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='isns-device-iqn', extensions=None), is_container='list', yang_name="isns-device-list", rest_name="isns-device-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_device_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("isns_device_iqn",isns_device_list.isns_device_list, yang_name="isns-device-list", rest_name="isns-device-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='isns-device-iqn', extensions=None), is_container='list', yang_name="isns-device-list", rest_name="isns-device-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='list', is_config=True)""",
        })

    self.__isns_device_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_device_list(self):
    self.__isns_device_list = YANGDynClass(base=YANGListType("isns_device_iqn",isns_device_list.isns_device_list, yang_name="isns-device-list", rest_name="isns-device-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='isns-device-iqn', extensions=None), is_container='list', yang_name="isns-device-list", rest_name="isns-device-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='list', is_config=True)

  isns_device_entity_id = __builtin__.property(_get_isns_device_entity_id, _set_isns_device_entity_id)
  isns_device_list = __builtin__.property(_get_isns_device_list, _set_isns_device_list)


  _pyangbind_elements = {'isns_device_entity_id': isns_device_entity_id, 'isns_device_list': isns_device_list, }


