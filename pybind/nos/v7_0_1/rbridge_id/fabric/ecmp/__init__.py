
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ecmp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/fabric/ecmp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This function allows to configure ECMP
related parameters.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ecmp_load_balance','__load_balance_hash_swap',)

  _yang_name = 'ecmp'
  _rest_name = 'ecmp'

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
    self.__load_balance_hash_swap = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="load-balance-hash-swap", rest_name="load-balance-hash-swap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hash-Swap value', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='hashswap-type', is_config=True)
    self.__ecmp_load_balance = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="ecmp-load-balance", rest_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure load balancing parameters', u'alt-name': u'load-balance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='enumeration', is_config=True)

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
      return [u'rbridge-id', u'fabric', u'ecmp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'fabric', u'ecmp']

  def _get_ecmp_load_balance(self):
    """
    Getter method for ecmp_load_balance, mapped from YANG variable /rbridge_id/fabric/ecmp/ecmp_load_balance (enumeration)

    YANG Description: This function allows to configure load
balancing parameters that are used in
ECMP hashing.
    """
    return self.__ecmp_load_balance
      
  def _set_ecmp_load_balance(self, v, load=False):
    """
    Setter method for ecmp_load_balance, mapped from YANG variable /rbridge_id/fabric/ecmp/ecmp_load_balance (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ecmp_load_balance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ecmp_load_balance() directly.

    YANG Description: This function allows to configure load
balancing parameters that are used in
ECMP hashing.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="ecmp-load-balance", rest_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure load balancing parameters', u'alt-name': u'load-balance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ecmp_load_balance must be of a type compatible with enumeration""",
          'defined-type': "brocade-fabric-service:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="ecmp-load-balance", rest_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure load balancing parameters', u'alt-name': u'load-balance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='enumeration', is_config=True)""",
        })

    self.__ecmp_load_balance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ecmp_load_balance(self):
    self.__ecmp_load_balance = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="ecmp-load-balance", rest_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure load balancing parameters', u'alt-name': u'load-balance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='enumeration', is_config=True)


  def _get_load_balance_hash_swap(self):
    """
    Getter method for load_balance_hash_swap, mapped from YANG variable /rbridge_id/fabric/ecmp/load_balance_hash_swap (hashswap-type)

    YANG Description: This command is used to configure how to swap
the input fields before feeding them to the
hash function.
    """
    return self.__load_balance_hash_swap
      
  def _set_load_balance_hash_swap(self, v, load=False):
    """
    Setter method for load_balance_hash_swap, mapped from YANG variable /rbridge_id/fabric/ecmp/load_balance_hash_swap (hashswap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balance_hash_swap is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balance_hash_swap() directly.

    YANG Description: This command is used to configure how to swap
the input fields before feeding them to the
hash function.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="load-balance-hash-swap", rest_name="load-balance-hash-swap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hash-Swap value', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='hashswap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balance_hash_swap must be of a type compatible with hashswap-type""",
          'defined-type': "brocade-fabric-service:hashswap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="load-balance-hash-swap", rest_name="load-balance-hash-swap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hash-Swap value', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='hashswap-type', is_config=True)""",
        })

    self.__load_balance_hash_swap = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balance_hash_swap(self):
    self.__load_balance_hash_swap = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="load-balance-hash-swap", rest_name="load-balance-hash-swap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hash-Swap value', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='hashswap-type', is_config=True)

  ecmp_load_balance = __builtin__.property(_get_ecmp_load_balance, _set_ecmp_load_balance)
  load_balance_hash_swap = __builtin__.property(_get_load_balance_hash_swap, _set_load_balance_hash_swap)


  _pyangbind_elements = {'ecmp_load_balance': ecmp_load_balance, 'load_balance_hash_swap': load_balance_hash_swap, }

