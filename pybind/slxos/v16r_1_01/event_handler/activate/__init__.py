
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import name
class activate(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-event-handler - based on the path /event-handler/activate. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name',)

  _yang_name = 'activate'
  _rest_name = 'activate'

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
    self.__name = YANGDynClass(base=YANGListType("name",name.name, yang_name="name", rest_name="name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)

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
      return [u'event-handler', u'activate']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'event-handler', u'activate']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /event_handler/activate/name (list)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /event_handler/activate/name (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",name.name, yang_name="name", rest_name="name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",name.name, yang_name="name", rest_name="name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=YANGListType("name",name.name, yang_name="name", rest_name="name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)


  _pyangbind_elements = {'name': name, }


