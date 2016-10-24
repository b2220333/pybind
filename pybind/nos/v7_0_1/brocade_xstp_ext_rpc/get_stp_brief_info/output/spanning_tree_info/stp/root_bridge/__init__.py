
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class root_bridge(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc/get-stp-brief-info/output/spanning-tree-info/stp/root-bridge. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__priority','__bridge_id','__hello_time','__max_age','__forward_delay',)

  _yang_name = 'root-bridge'
  _rest_name = 'root-bridge'

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
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    self.__bridge_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="bridge-id", rest_name="bridge-id", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)
    self.__forward_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)

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
      return [u'brocade_xstp_ext_rpc', u'get-stp-brief-info', u'output', u'spanning-tree-info', u'stp', u'root-bridge']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-stp-brief-info', u'output', u'spanning-tree-info', u'stp', u'root-bridge']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/priority (uint32)

    YANG Description: Bridge priority (0..65535)
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Bridge priority (0..65535)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)


  def _get_bridge_id(self):
    """
    Getter method for bridge_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/bridge_id (bridge-id-type)

    YANG Description: Bridge id
    """
    return self.__bridge_id
      
  def _set_bridge_id(self, v, load=False):
    """
    Setter method for bridge_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/bridge_id (bridge-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_id() directly.

    YANG Description: Bridge id
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="bridge-id", rest_name="bridge-id", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_id must be of a type compatible with bridge-id-type""",
          'defined-type': "brocade-xstp-ext:bridge-id-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="bridge-id", rest_name="bridge-id", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)""",
        })

    self.__bridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_id(self):
    self.__bridge_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="bridge-id", rest_name="bridge-id", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)


  def _get_hello_time(self):
    """
    Getter method for hello_time, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/hello_time (uint32)

    YANG Description: The interval between two transmissions of BPDU packets
sent by the Root Bridge to tell all other switches that
it is indeed the Root Bridge (1..10 sec)
    """
    return self.__hello_time
      
  def _set_hello_time(self, v, load=False):
    """
    Setter method for hello_time, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/hello_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_time() directly.

    YANG Description: The interval between two transmissions of BPDU packets
sent by the Root Bridge to tell all other switches that
it is indeed the Root Bridge (1..10 sec)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__hello_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_time(self):
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)


  def _get_max_age(self):
    """
    Getter method for max_age, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/max_age (uint32)

    YANG Description: The Max Age may be set to ensure that old information
does not endlessly circulate through redundant paths in
the network, preventing the effective propagation of
new information (6..40 sec)
    """
    return self.__max_age
      
  def _set_max_age(self, v, load=False):
    """
    Setter method for max_age, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/max_age (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_age() directly.

    YANG Description: The Max Age may be set to ensure that old information
does not endlessly circulate through redundant paths in
the network, preventing the effective propagation of
new information (6..40 sec)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_age must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__max_age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_age(self):
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)


  def _get_forward_delay(self):
    """
    Getter method for forward_delay, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/forward_delay (uint32)

    YANG Description: Port on the Switch spends this time in the listening
state while moving from the blocking state to the
forwarding state (4..30 sec)
    """
    return self.__forward_delay
      
  def _set_forward_delay(self, v, load=False):
    """
    Setter method for forward_delay, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge/forward_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forward_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forward_delay() directly.

    YANG Description: Port on the Switch spends this time in the listening
state while moving from the blocking state to the
forwarding state (4..30 sec)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forward_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__forward_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forward_delay(self):
    self.__forward_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)

  priority = __builtin__.property(_get_priority, _set_priority)
  bridge_id = __builtin__.property(_get_bridge_id, _set_bridge_id)
  hello_time = __builtin__.property(_get_hello_time, _set_hello_time)
  max_age = __builtin__.property(_get_max_age, _set_max_age)
  forward_delay = __builtin__.property(_get_forward_delay, _set_forward_delay)

  __choices__ = {u'spanning-tree-mode': {u'stp': [u'priority', u'bridge_id', u'hello_time', u'max_age', u'forward_delay']}}
  _pyangbind_elements = {'priority': priority, 'bridge_id': bridge_id, 'hello_time': hello_time, 'max_age': max_age, 'forward_delay': forward_delay, }


