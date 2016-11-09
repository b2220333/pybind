
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag/load-balance/hash/mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__label1','__label2','__label3',)

  _yang_name = 'mpls'
  _rest_name = 'mpls'

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
    self.__label1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label1", rest_name="label1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label1', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label1\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__label2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label2", rest_name="label2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label2', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label2\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__label3 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label3", rest_name="label3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label3', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label3\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

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
      return [u'load-balance-lag', u'load-balance', u'hash', u'mpls']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'load-balance', u'hash', u'mpls']

  def _get_label1(self):
    """
    Getter method for label1, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls/label1 (empty)
    """
    return self.__label1
      
  def _set_label1(self, v, load=False):
    """
    Setter method for label1, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls/label1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label1() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="label1", rest_name="label1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label1', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label1\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label1", rest_name="label1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label1', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label1\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__label1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label1(self):
    self.__label1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label1", rest_name="label1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label1', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label1\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_label2(self):
    """
    Getter method for label2, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls/label2 (empty)
    """
    return self.__label2
      
  def _set_label2(self, v, load=False):
    """
    Setter method for label2, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls/label2 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label2() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="label2", rest_name="label2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label2', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label2\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label2 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label2", rest_name="label2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label2', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label2\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__label2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label2(self):
    self.__label2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label2", rest_name="label2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label2', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label2\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_label3(self):
    """
    Getter method for label3, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls/label3 (empty)
    """
    return self.__label3
      
  def _set_label3(self, v, load=False):
    """
    Setter method for label3, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls/label3 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label3() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="label3", rest_name="label3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label3', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label3\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label3 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label3", rest_name="label3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label3', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label3\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__label3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label3(self):
    self.__label3 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="label3", rest_name="label3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'label3', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash mpls label3\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

  label1 = __builtin__.property(_get_label1, _set_label1)
  label2 = __builtin__.property(_get_label2, _set_label2)
  label3 = __builtin__.property(_get_label3, _set_label3)


  _pyangbind_elements = {'label1': label1, 'label2': label2, 'label3': label3, }


