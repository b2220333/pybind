
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /rule/command/interface-ve-leaf/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ve_leaf',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__ve_leaf = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-leaf", rest_name="ve", parent=self, choice=(u'cmdlist', u'interface-q'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u've'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:ve-type', is_config=True)

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
      return [u'rule', u'command', u'interface-ve-leaf', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rule', u'command', u'interface']

  def _get_ve_leaf(self):
    """
    Getter method for ve_leaf, mapped from YANG variable /rule/command/interface_ve_leaf/interface/ve_leaf (interface:ve-type)
    """
    return self.__ve_leaf
      
  def _set_ve_leaf(self, v, load=False):
    """
    Setter method for ve_leaf, mapped from YANG variable /rule/command/interface_ve_leaf/interface/ve_leaf (interface:ve-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ve_leaf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ve_leaf() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-leaf", rest_name="ve", parent=self, choice=(u'cmdlist', u'interface-q'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u've'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:ve-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ve_leaf must be of a type compatible with interface:ve-type""",
          'defined-type': "interface:ve-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-leaf", rest_name="ve", parent=self, choice=(u'cmdlist', u'interface-q'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u've'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:ve-type', is_config=True)""",
        })

    self.__ve_leaf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ve_leaf(self):
    self.__ve_leaf = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-leaf", rest_name="ve", parent=self, choice=(u'cmdlist', u'interface-q'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u've'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:ve-type', is_config=True)

  ve_leaf = __builtin__.property(_get_ve_leaf, _set_ve_leaf)

  __choices__ = {u'cmdlist': {u'interface-q': [u've_leaf']}}
  _pyangbind_elements = {'ve_leaf': ve_leaf, }


