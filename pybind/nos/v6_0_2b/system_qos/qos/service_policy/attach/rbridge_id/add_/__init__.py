
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class add_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-policer - based on the path /system-qos/qos/service-policy/attach/rbridge-id/add. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rb_add_range',)

  _yang_name = 'add'
  _rest_name = 'add'

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
    self.__rb_add_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="rb-add-range", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'RANGE;;Range of rbridge ids to add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='rbridge-ui32-range', is_config=True)

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
      return [u'system-qos', u'qos', u'service-policy', u'attach', u'rbridge-id', u'add']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'service-policy', u'attach', u'rbridge-id', u'add']

  def _get_rb_add_range(self):
    """
    Getter method for rb_add_range, mapped from YANG variable /system_qos/qos/service_policy/attach/rbridge_id/add/rb_add_range (rbridge-ui32-range)
    """
    return self.__rb_add_range
      
  def _set_rb_add_range(self, v, load=False):
    """
    Setter method for rb_add_range, mapped from YANG variable /system_qos/qos/service_policy/attach/rbridge_id/add/rb_add_range (rbridge-ui32-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rb_add_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rb_add_range() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="rb-add-range", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'RANGE;;Range of rbridge ids to add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='rbridge-ui32-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rb_add_range must be of a type compatible with rbridge-ui32-range""",
          'defined-type': "brocade-policer:rbridge-ui32-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="rb-add-range", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'RANGE;;Range of rbridge ids to add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='rbridge-ui32-range', is_config=True)""",
        })

    self.__rb_add_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rb_add_range(self):
    self.__rb_add_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="rb-add-range", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'RANGE;;Range of rbridge ids to add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='rbridge-ui32-range', is_config=True)

  rb_add_range = __builtin__.property(_get_rb_add_range, _set_rb_add_range)


  _pyangbind_elements = {'rb_add_range': rb_add_range, }

