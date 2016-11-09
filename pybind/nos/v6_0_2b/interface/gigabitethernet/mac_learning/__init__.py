
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mac_learn_disable
class mac_learning(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/mac-learning. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_learn_disable',)

  _yang_name = 'mac-learning'
  _rest_name = 'mac-learning'

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
    self.__mac_learn_disable = YANGDynClass(base=mac_learn_disable.mac_learn_disable, is_container='container', yang_name="mac-learn-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC learning disable.', u'cli-full-no': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'mac-learning']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'mac-learning']

  def _get_mac_learn_disable(self):
    """
    Getter method for mac_learn_disable, mapped from YANG variable /interface/gigabitethernet/mac_learning/mac_learn_disable (container)
    """
    return self.__mac_learn_disable
      
  def _set_mac_learn_disable(self, v, load=False):
    """
    Setter method for mac_learn_disable, mapped from YANG variable /interface/gigabitethernet/mac_learning/mac_learn_disable (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_learn_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_learn_disable() directly.
    """
    try:
      t = YANGDynClass(v,base=mac_learn_disable.mac_learn_disable, is_container='container', yang_name="mac-learn-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC learning disable.', u'cli-full-no': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_learn_disable must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mac_learn_disable.mac_learn_disable, is_container='container', yang_name="mac-learn-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC learning disable.', u'cli-full-no': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__mac_learn_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_learn_disable(self):
    self.__mac_learn_disable = YANGDynClass(base=mac_learn_disable.mac_learn_disable, is_container='container', yang_name="mac-learn-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC learning disable.', u'cli-full-no': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  mac_learn_disable = __builtin__.property(_get_mac_learn_disable, _set_mac_learn_disable)


  _pyangbind_elements = {'mac_learn_disable': mac_learn_disable, }


