
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import linecards
class linecard(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/global-lc-holder/linecard. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__linecards',)

  _yang_name = 'linecard'
  _rest_name = 'linecard'

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
    self.__linecards = YANGDynClass(base=YANGListType("linecardName",linecards.linecards, yang_name="linecards", rest_name="linecards", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='linecardName', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}), is_container='list', yang_name="linecards", rest_name="linecards", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}, namespace='urn:brocade.com:mgmt:brocade-linecard-management', defining_module='brocade-linecard-management', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'global-lc-holder', u'linecard']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'linecard']

  def _get_linecards(self):
    """
    Getter method for linecards, mapped from YANG variable /rbridge_id/global_lc_holder/linecard/linecards (list)
    """
    return self.__linecards
      
  def _set_linecards(self, v, load=False):
    """
    Setter method for linecards, mapped from YANG variable /rbridge_id/global_lc_holder/linecard/linecards (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_linecards is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_linecards() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("linecardName",linecards.linecards, yang_name="linecards", rest_name="linecards", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='linecardName', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}), is_container='list', yang_name="linecards", rest_name="linecards", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}, namespace='urn:brocade.com:mgmt:brocade-linecard-management', defining_module='brocade-linecard-management', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """linecards must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("linecardName",linecards.linecards, yang_name="linecards", rest_name="linecards", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='linecardName', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}), is_container='list', yang_name="linecards", rest_name="linecards", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}, namespace='urn:brocade.com:mgmt:brocade-linecard-management', defining_module='brocade-linecard-management', yang_type='list', is_config=True)""",
        })

    self.__linecards = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_linecards(self):
    self.__linecards = YANGDynClass(base=YANGListType("linecardName",linecards.linecards, yang_name="linecards", rest_name="linecards", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='linecardName', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}), is_container='list', yang_name="linecards", rest_name="linecards", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'linecardManagement'}}, namespace='urn:brocade.com:mgmt:brocade-linecard-management', defining_module='brocade-linecard-management', yang_type='list', is_config=True)

  linecards = __builtin__.property(_get_linecards, _set_linecards)


  _pyangbind_elements = {'linecards': linecards, }


