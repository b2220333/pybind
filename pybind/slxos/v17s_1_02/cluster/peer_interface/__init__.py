
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class peer_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct - based on the path /cluster/peer-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__peer_if_type','__peer_if_name',)

  _yang_name = 'peer-interface'
  _rest_name = 'peer-interface'

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
    self.__peer_if_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="peer-if-name", rest_name="peer-if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'info': u'Peer Interface Name', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string-type', is_config=True)
    self.__peer_if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Ethernet': {'value': 8}, u'Port-channel': {'value': 3}},), is_leaf=True, yang_name="peer-if-type", rest_name="peer-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)

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
      return [u'cluster', u'peer-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cluster', u'peer-interface']

  def _get_peer_if_type(self):
    """
    Getter method for peer_if_type, mapped from YANG variable /cluster/peer_interface/peer_if_type (enumeration)
    """
    return self.__peer_if_type
      
  def _set_peer_if_type(self, v, load=False):
    """
    Setter method for peer_if_type, mapped from YANG variable /cluster/peer_interface/peer_if_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_if_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_if_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Ethernet': {'value': 8}, u'Port-channel': {'value': 3}},), is_leaf=True, yang_name="peer-if-type", rest_name="peer-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_if_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mct:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Ethernet': {'value': 8}, u'Port-channel': {'value': 3}},), is_leaf=True, yang_name="peer-if-type", rest_name="peer-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)""",
        })

    self.__peer_if_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_if_type(self):
    self.__peer_if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Ethernet': {'value': 8}, u'Port-channel': {'value': 3}},), is_leaf=True, yang_name="peer-if-type", rest_name="peer-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)


  def _get_peer_if_name(self):
    """
    Getter method for peer_if_name, mapped from YANG variable /cluster/peer_interface/peer_if_name (string-type)
    """
    return self.__peer_if_name
      
  def _set_peer_if_name(self, v, load=False):
    """
    Setter method for peer_if_name, mapped from YANG variable /cluster/peer_interface/peer_if_name (string-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_if_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_if_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="peer-if-name", rest_name="peer-if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'info': u'Peer Interface Name', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_if_name must be of a type compatible with string-type""",
          'defined-type': "brocade-mct:string-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="peer-if-name", rest_name="peer-if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'info': u'Peer Interface Name', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string-type', is_config=True)""",
        })

    self.__peer_if_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_if_name(self):
    self.__peer_if_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="peer-if-name", rest_name="peer-if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-show-conf-path': None, u'info': u'Peer Interface Name', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string-type', is_config=True)

  peer_if_type = __builtin__.property(_get_peer_if_type, _set_peer_if_type)
  peer_if_name = __builtin__.property(_get_peer_if_name, _set_peer_if_name)


  _pyangbind_elements = {'peer_if_type': peer_if_type, 'peer_if_name': peer_if_name, }

