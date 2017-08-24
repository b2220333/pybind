
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class delay_link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/delay-link-event/delay-link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__delay_link_event_entry','__delay_link_event_type',)

  _yang_name = 'delay-link'
  _rest_name = ''

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
    self.__delay_link_event_entry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..200']}), is_leaf=True, yang_name="delay-link-event-entry", rest_name="delay-link-event-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='uint32', is_config=True)
    self.__delay_link_event_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 2}, u'both': {'value': 3}, u'up': {'value': 1}},), is_leaf=True, yang_name="delay-link-event-type", rest_name="delay-link-event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../delay-link-event-entry)'}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='enumeration', is_config=True)

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
      return [u'interface', u'ethernet', u'delay-link-event', u'delay-link']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'delay-link-event']

  def _get_delay_link_event_entry(self):
    """
    Getter method for delay_link_event_entry, mapped from YANG variable /interface/ethernet/delay_link_event/delay_link/delay_link_event_entry (uint32)
    """
    return self.__delay_link_event_entry
      
  def _set_delay_link_event_entry(self, v, load=False):
    """
    Setter method for delay_link_event_entry, mapped from YANG variable /interface/ethernet/delay_link_event/delay_link/delay_link_event_entry (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_delay_link_event_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_delay_link_event_entry() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..200']}), is_leaf=True, yang_name="delay-link-event-entry", rest_name="delay-link-event-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """delay_link_event_entry must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..200']}), is_leaf=True, yang_name="delay-link-event-entry", rest_name="delay-link-event-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='uint32', is_config=True)""",
        })

    self.__delay_link_event_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_delay_link_event_entry(self):
    self.__delay_link_event_entry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..200']}), is_leaf=True, yang_name="delay-link-event-entry", rest_name="delay-link-event-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='uint32', is_config=True)


  def _get_delay_link_event_type(self):
    """
    Getter method for delay_link_event_type, mapped from YANG variable /interface/ethernet/delay_link_event/delay_link/delay_link_event_type (enumeration)
    """
    return self.__delay_link_event_type
      
  def _set_delay_link_event_type(self, v, load=False):
    """
    Setter method for delay_link_event_type, mapped from YANG variable /interface/ethernet/delay_link_event/delay_link/delay_link_event_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_delay_link_event_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_delay_link_event_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 2}, u'both': {'value': 3}, u'up': {'value': 1}},), is_leaf=True, yang_name="delay-link-event-type", rest_name="delay-link-event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../delay-link-event-entry)'}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """delay_link_event_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-dle:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 2}, u'both': {'value': 3}, u'up': {'value': 1}},), is_leaf=True, yang_name="delay-link-event-type", rest_name="delay-link-event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../delay-link-event-entry)'}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='enumeration', is_config=True)""",
        })

    self.__delay_link_event_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_delay_link_event_type(self):
    self.__delay_link_event_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 2}, u'both': {'value': 3}, u'up': {'value': 1}},), is_leaf=True, yang_name="delay-link-event-type", rest_name="delay-link-event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../delay-link-event-entry)'}}, namespace='urn:brocade.com:mgmt:brocade-dle', defining_module='brocade-dle', yang_type='enumeration', is_config=True)

  delay_link_event_entry = __builtin__.property(_get_delay_link_event_entry, _set_delay_link_event_entry)
  delay_link_event_type = __builtin__.property(_get_delay_link_event_type, _set_delay_link_event_type)


  _pyangbind_elements = {'delay_link_event_entry': delay_link_event_entry, 'delay_link_event_type': delay_link_event_type, }


