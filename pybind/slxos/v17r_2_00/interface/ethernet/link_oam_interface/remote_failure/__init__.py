
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dying_gasp
import link_fault
import critical_event
class remote_failure(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/link-oam-interface/remote-failure. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dying_gasp','__link_fault','__critical_event',)

  _yang_name = 'remote-failure'
  _rest_name = 'remote-failure'

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
    self.__dying_gasp = YANGDynClass(base=dying_gasp.dying_gasp, is_container='container', presence=False, yang_name="dying-gasp", rest_name="dying-gasp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event dying-gasp', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)
    self.__critical_event = YANGDynClass(base=critical_event.critical_event, is_container='container', presence=False, yang_name="critical-event", rest_name="critical-event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event critical-event', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)
    self.__link_fault = YANGDynClass(base=link_fault.link_fault, is_container='container', presence=False, yang_name="link-fault", rest_name="link-fault", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event link-fault', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)

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
      return [u'interface', u'ethernet', u'link-oam-interface', u'remote-failure']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'link-oam', u'remote-failure']

  def _get_dying_gasp(self):
    """
    Getter method for dying_gasp, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/dying_gasp (container)
    """
    return self.__dying_gasp
      
  def _set_dying_gasp(self, v, load=False):
    """
    Setter method for dying_gasp, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/dying_gasp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dying_gasp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dying_gasp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dying_gasp.dying_gasp, is_container='container', presence=False, yang_name="dying-gasp", rest_name="dying-gasp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event dying-gasp', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dying_gasp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dying_gasp.dying_gasp, is_container='container', presence=False, yang_name="dying-gasp", rest_name="dying-gasp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event dying-gasp', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)""",
        })

    self.__dying_gasp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dying_gasp(self):
    self.__dying_gasp = YANGDynClass(base=dying_gasp.dying_gasp, is_container='container', presence=False, yang_name="dying-gasp", rest_name="dying-gasp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event dying-gasp', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)


  def _get_link_fault(self):
    """
    Getter method for link_fault, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/link_fault (container)
    """
    return self.__link_fault
      
  def _set_link_fault(self, v, load=False):
    """
    Setter method for link_fault, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/link_fault (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_fault is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_fault() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=link_fault.link_fault, is_container='container', presence=False, yang_name="link-fault", rest_name="link-fault", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event link-fault', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_fault must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=link_fault.link_fault, is_container='container', presence=False, yang_name="link-fault", rest_name="link-fault", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event link-fault', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)""",
        })

    self.__link_fault = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_fault(self):
    self.__link_fault = YANGDynClass(base=link_fault.link_fault, is_container='container', presence=False, yang_name="link-fault", rest_name="link-fault", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event link-fault', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)


  def _get_critical_event(self):
    """
    Getter method for critical_event, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/critical_event (container)
    """
    return self.__critical_event
      
  def _set_critical_event(self, v, load=False):
    """
    Setter method for critical_event, mapped from YANG variable /interface/ethernet/link_oam_interface/remote_failure/critical_event (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_critical_event is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_critical_event() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=critical_event.critical_event, is_container='container', presence=False, yang_name="critical-event", rest_name="critical-event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event critical-event', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """critical_event must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=critical_event.critical_event, is_container='container', presence=False, yang_name="critical-event", rest_name="critical-event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event critical-event', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)""",
        })

    self.__critical_event = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_critical_event(self):
    self.__critical_event = YANGDynClass(base=critical_event.critical_event, is_container='container', presence=False, yang_name="critical-event", rest_name="critical-event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event critical-event', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot3ah', defining_module='brocade-dot3ah', yang_type='container', is_config=True)

  dying_gasp = __builtin__.property(_get_dying_gasp, _set_dying_gasp)
  link_fault = __builtin__.property(_get_link_fault, _set_link_fault)
  critical_event = __builtin__.property(_get_critical_event, _set_critical_event)


  _pyangbind_elements = {'dying_gasp': dying_gasp, 'link_fault': link_fault, 'critical_event': critical_event, }


