
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class link_fault(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/link-oam-interface/remote-failure/link-fault. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__link_fault_action',)

  _yang_name = 'link-fault'
  _rest_name = 'link-fault'

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
    self.__link_fault_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'block-interface': {'value': 1}},), is_leaf=True, yang_name="link-fault-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configures an action for the event', u'cli-full-no': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='action-type', is_config=True)

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
      return [u'interface', u'ethernet', u'link-oam-interface', u'remote-failure', u'link-fault']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'link-oam', u'remote-failure', u'link-fault']

  def _get_link_fault_action(self):
    """
    Getter method for link_fault_action, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/link_fault/link_fault_action (action-type)
    """
    return self.__link_fault_action
      
  def _set_link_fault_action(self, v, load=False):
    """
    Setter method for link_fault_action, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/link_fault/link_fault_action (action-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_fault_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_fault_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'block-interface': {'value': 1}},), is_leaf=True, yang_name="link-fault-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configures an action for the event', u'cli-full-no': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='action-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_fault_action must be of a type compatible with action-type""",
          'defined-type': "brocade-dot3ah:action-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'block-interface': {'value': 1}},), is_leaf=True, yang_name="link-fault-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configures an action for the event', u'cli-full-no': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='action-type', is_config=True)""",
        })

    self.__link_fault_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_fault_action(self):
    self.__link_fault_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'block-interface': {'value': 1}},), is_leaf=True, yang_name="link-fault-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configures an action for the event', u'cli-full-no': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='action-type', is_config=True)

  link_fault_action = __builtin__.property(_get_link_fault_action, _set_link_fault_action)


  _pyangbind_elements = {'link_fault_action': link_fault_action, }


