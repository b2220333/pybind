
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-te-path/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipAddr','__bandwidth','__cspfCompMode','__excludeAny','__hopLimit','__includeAny','__includeAll','__tePathName','__priority','__tieBreaking',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__cspfCompMode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'use-igp-metric': {'value': 1}, u'use-te-metric': {'value': 2}},), is_leaf=True, yang_name="cspfCompMode", rest_name="cspfCompMode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='cspf-computation-mode', is_config=True)
    self.__includeAny = YANGDynClass(base=unicode, is_leaf=True, yang_name="includeAny", rest_name="includeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__hopLimit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hopLimit", rest_name="hopLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    self.__tePathName = YANGDynClass(base=unicode, is_leaf=True, yang_name="tePathName", rest_name="tePathName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__ipAddr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipAddr", rest_name="ipAddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__tieBreaking = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'most-fill': {'value': 2}, u'random': {'value': 0}, u'least-fill': {'value': 1}},), is_leaf=True, yang_name="tieBreaking", rest_name="tieBreaking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='tie-breaking', is_config=True)
    self.__excludeAny = YANGDynClass(base=unicode, is_leaf=True, yang_name="excludeAny", rest_name="excludeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__includeAll = YANGDynClass(base=unicode, is_leaf=True, yang_name="includeAll", rest_name="includeAll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-te-path', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-te-path', u'input']

  def _get_ipAddr(self):
    """
    Getter method for ipAddr, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/ipAddr (inet:ipv4-address)

    YANG Description: Destination IP Address
    """
    return self.__ipAddr
      
  def _set_ipAddr(self, v, load=False):
    """
    Setter method for ipAddr, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/ipAddr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipAddr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipAddr() directly.

    YANG Description: Destination IP Address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipAddr", rest_name="ipAddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipAddr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipAddr", rest_name="ipAddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ipAddr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipAddr(self):
    self.__ipAddr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipAddr", rest_name="ipAddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_bandwidth(self):
    """
    Getter method for bandwidth, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/bandwidth (uint32)

    YANG Description: Desired minimum bandwidth of the path
    """
    return self.__bandwidth
      
  def _set_bandwidth(self, v, load=False):
    """
    Setter method for bandwidth, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth() directly.

    YANG Description: Desired minimum bandwidth of the path
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth(self):
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_cspfCompMode(self):
    """
    Getter method for cspfCompMode, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/cspfCompMode (cspf-computation-mode)

    YANG Description: Select cspf computation mode used for calculating the path
    """
    return self.__cspfCompMode
      
  def _set_cspfCompMode(self, v, load=False):
    """
    Setter method for cspfCompMode, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/cspfCompMode (cspf-computation-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cspfCompMode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cspfCompMode() directly.

    YANG Description: Select cspf computation mode used for calculating the path
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'use-igp-metric': {'value': 1}, u'use-te-metric': {'value': 2}},), is_leaf=True, yang_name="cspfCompMode", rest_name="cspfCompMode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='cspf-computation-mode', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cspfCompMode must be of a type compatible with cspf-computation-mode""",
          'defined-type': "brocade-mpls:cspf-computation-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'use-igp-metric': {'value': 1}, u'use-te-metric': {'value': 2}},), is_leaf=True, yang_name="cspfCompMode", rest_name="cspfCompMode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='cspf-computation-mode', is_config=True)""",
        })

    self.__cspfCompMode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cspfCompMode(self):
    self.__cspfCompMode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'use-igp-metric': {'value': 1}, u'use-te-metric': {'value': 2}},), is_leaf=True, yang_name="cspfCompMode", rest_name="cspfCompMode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='cspf-computation-mode', is_config=True)


  def _get_excludeAny(self):
    """
    Getter method for excludeAny, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/excludeAny (string)

    YANG Description: Exclude any of the administrative groups
    """
    return self.__excludeAny
      
  def _set_excludeAny(self, v, load=False):
    """
    Setter method for excludeAny, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/excludeAny (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_excludeAny is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_excludeAny() directly.

    YANG Description: Exclude any of the administrative groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="excludeAny", rest_name="excludeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """excludeAny must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="excludeAny", rest_name="excludeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__excludeAny = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_excludeAny(self):
    self.__excludeAny = YANGDynClass(base=unicode, is_leaf=True, yang_name="excludeAny", rest_name="excludeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_hopLimit(self):
    """
    Getter method for hopLimit, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/hopLimit (uint8)

    YANG Description: Desired maximum hop that the path can traverse
    """
    return self.__hopLimit
      
  def _set_hopLimit(self, v, load=False):
    """
    Setter method for hopLimit, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/hopLimit (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hopLimit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hopLimit() directly.

    YANG Description: Desired maximum hop that the path can traverse
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hopLimit", rest_name="hopLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hopLimit must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hopLimit", rest_name="hopLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__hopLimit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hopLimit(self):
    self.__hopLimit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hopLimit", rest_name="hopLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_includeAny(self):
    """
    Getter method for includeAny, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/includeAny (string)

    YANG Description: Include any of the administrative groups
    """
    return self.__includeAny
      
  def _set_includeAny(self, v, load=False):
    """
    Setter method for includeAny, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/includeAny (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_includeAny is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_includeAny() directly.

    YANG Description: Include any of the administrative groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="includeAny", rest_name="includeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """includeAny must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="includeAny", rest_name="includeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__includeAny = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_includeAny(self):
    self.__includeAny = YANGDynClass(base=unicode, is_leaf=True, yang_name="includeAny", rest_name="includeAny", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_includeAll(self):
    """
    Getter method for includeAll, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/includeAll (string)

    YANG Description: Include all of the administrative groups
    """
    return self.__includeAll
      
  def _set_includeAll(self, v, load=False):
    """
    Setter method for includeAll, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/includeAll (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_includeAll is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_includeAll() directly.

    YANG Description: Include all of the administrative groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="includeAll", rest_name="includeAll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """includeAll must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="includeAll", rest_name="includeAll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__includeAll = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_includeAll(self):
    self.__includeAll = YANGDynClass(base=unicode, is_leaf=True, yang_name="includeAll", rest_name="includeAll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_tePathName(self):
    """
    Getter method for tePathName, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/tePathName (string)

    YANG Description: Display by Path name
    """
    return self.__tePathName
      
  def _set_tePathName(self, v, load=False):
    """
    Setter method for tePathName, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/tePathName (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tePathName is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tePathName() directly.

    YANG Description: Display by Path name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tePathName", rest_name="tePathName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tePathName must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tePathName", rest_name="tePathName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__tePathName = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tePathName(self):
    self.__tePathName = YANGDynClass(base=unicode, is_leaf=True, yang_name="tePathName", rest_name="tePathName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/priority (uint8)

    YANG Description: Setup priority of the path
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Setup priority of the path
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_tieBreaking(self):
    """
    Getter method for tieBreaking, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/tieBreaking (tie-breaking)

    YANG Description: Tie breaking mode for CSPF when multiple paths to destination exists
    """
    return self.__tieBreaking
      
  def _set_tieBreaking(self, v, load=False):
    """
    Setter method for tieBreaking, mapped from YANG variable /brocade_mpls_rpc/show_mpls_te_path/input/tieBreaking (tie-breaking)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tieBreaking is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tieBreaking() directly.

    YANG Description: Tie breaking mode for CSPF when multiple paths to destination exists
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'most-fill': {'value': 2}, u'random': {'value': 0}, u'least-fill': {'value': 1}},), is_leaf=True, yang_name="tieBreaking", rest_name="tieBreaking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='tie-breaking', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tieBreaking must be of a type compatible with tie-breaking""",
          'defined-type': "brocade-mpls:tie-breaking",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'most-fill': {'value': 2}, u'random': {'value': 0}, u'least-fill': {'value': 1}},), is_leaf=True, yang_name="tieBreaking", rest_name="tieBreaking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='tie-breaking', is_config=True)""",
        })

    self.__tieBreaking = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tieBreaking(self):
    self.__tieBreaking = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'most-fill': {'value': 2}, u'random': {'value': 0}, u'least-fill': {'value': 1}},), is_leaf=True, yang_name="tieBreaking", rest_name="tieBreaking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='tie-breaking', is_config=True)

  ipAddr = __builtin__.property(_get_ipAddr, _set_ipAddr)
  bandwidth = __builtin__.property(_get_bandwidth, _set_bandwidth)
  cspfCompMode = __builtin__.property(_get_cspfCompMode, _set_cspfCompMode)
  excludeAny = __builtin__.property(_get_excludeAny, _set_excludeAny)
  hopLimit = __builtin__.property(_get_hopLimit, _set_hopLimit)
  includeAny = __builtin__.property(_get_includeAny, _set_includeAny)
  includeAll = __builtin__.property(_get_includeAll, _set_includeAll)
  tePathName = __builtin__.property(_get_tePathName, _set_tePathName)
  priority = __builtin__.property(_get_priority, _set_priority)
  tieBreaking = __builtin__.property(_get_tieBreaking, _set_tieBreaking)


  _pyangbind_elements = {'ipAddr': ipAddr, 'bandwidth': bandwidth, 'cspfCompMode': cspfCompMode, 'excludeAny': excludeAny, 'hopLimit': hopLimit, 'includeAny': includeAny, 'includeAll': includeAll, 'tePathName': tePathName, 'priority': priority, 'tieBreaking': tieBreaking, }


