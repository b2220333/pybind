
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import match
class cmap_seq(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-overlay-policy - based on the path /overlay-class-map/cmap-seq. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cmap_seq_num','__match',)

  _yang_name = 'cmap-seq'
  _rest_name = 'seq'

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
    self.__match = YANGDynClass(base=match.match, is_container='container', presence=False, yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'match IP', u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='container', is_config=True)
    self.__cmap_seq_num = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="cmap-seq-num", rest_name="cmap-seq-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='seq-num', is_config=True)

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
      return [u'overlay-class-map', u'cmap-seq']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-class-map', u'seq']

  def _get_cmap_seq_num(self):
    """
    Getter method for cmap_seq_num, mapped from YANG variable /overlay_class_map/cmap_seq/cmap_seq_num (seq-num)
    """
    return self.__cmap_seq_num
      
  def _set_cmap_seq_num(self, v, load=False):
    """
    Setter method for cmap_seq_num, mapped from YANG variable /overlay_class_map/cmap_seq/cmap_seq_num (seq-num)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cmap_seq_num is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cmap_seq_num() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="cmap-seq-num", rest_name="cmap-seq-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='seq-num', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cmap_seq_num must be of a type compatible with seq-num""",
          'defined-type': "brocade-overlay-policy:seq-num",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="cmap-seq-num", rest_name="cmap-seq-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='seq-num', is_config=True)""",
        })

    self.__cmap_seq_num = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cmap_seq_num(self):
    self.__cmap_seq_num = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="cmap-seq-num", rest_name="cmap-seq-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='seq-num', is_config=True)


  def _get_match(self):
    """
    Getter method for match, mapped from YANG variable /overlay_class_map/cmap_seq/match (container)
    """
    return self.__match
      
  def _set_match(self, v, load=False):
    """
    Setter method for match, mapped from YANG variable /overlay_class_map/cmap_seq/match (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match.match, is_container='container', presence=False, yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'match IP', u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match.match, is_container='container', presence=False, yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'match IP', u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='container', is_config=True)""",
        })

    self.__match = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match(self):
    self.__match = YANGDynClass(base=match.match, is_container='container', presence=False, yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'match IP', u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='container', is_config=True)

  cmap_seq_num = __builtin__.property(_get_cmap_seq_num, _set_cmap_seq_num)
  match = __builtin__.property(_get_match, _set_match)


  _pyangbind_elements = {'cmap_seq_num': cmap_seq_num, 'match': match, }


