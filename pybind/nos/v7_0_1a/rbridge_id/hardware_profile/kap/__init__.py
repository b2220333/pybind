
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import predefined
import customized
class kap(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/hardware-profile/kap. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__predefined','__customized',)

  _yang_name = 'kap'
  _rest_name = 'kap'

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
    self.__predefined = YANGDynClass(base=predefined.predefined, is_container='container', yang_name="predefined", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__customized = YANGDynClass(base=customized.customized, is_container='container', yang_name="customized", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Customized profile', u'alt-name': u'custom-profile', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'hardware-profile', u'kap']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'hardware-profile', u'kap']

  def _get_predefined(self):
    """
    Getter method for predefined, mapped from YANG variable /rbridge_id/hardware_profile/kap/predefined (container)
    """
    return self.__predefined
      
  def _set_predefined(self, v, load=False):
    """
    Setter method for predefined, mapped from YANG variable /rbridge_id/hardware_profile/kap/predefined (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_predefined is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_predefined() directly.
    """
    try:
      t = YANGDynClass(v,base=predefined.predefined, is_container='container', yang_name="predefined", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """predefined must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=predefined.predefined, is_container='container', yang_name="predefined", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__predefined = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_predefined(self):
    self.__predefined = YANGDynClass(base=predefined.predefined, is_container='container', yang_name="predefined", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_customized(self):
    """
    Getter method for customized, mapped from YANG variable /rbridge_id/hardware_profile/kap/customized (container)
    """
    return self.__customized
      
  def _set_customized(self, v, load=False):
    """
    Setter method for customized, mapped from YANG variable /rbridge_id/hardware_profile/kap/customized (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_customized is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_customized() directly.
    """
    try:
      t = YANGDynClass(v,base=customized.customized, is_container='container', yang_name="customized", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Customized profile', u'alt-name': u'custom-profile', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """customized must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=customized.customized, is_container='container', yang_name="customized", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Customized profile', u'alt-name': u'custom-profile', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__customized = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_customized(self):
    self.__customized = YANGDynClass(base=customized.customized, is_container='container', yang_name="customized", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Customized profile', u'alt-name': u'custom-profile', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

  predefined = __builtin__.property(_get_predefined, _set_predefined)
  customized = __builtin__.property(_get_customized, _set_customized)


  _pyangbind_elements = {'predefined': predefined, 'customized': customized, }


