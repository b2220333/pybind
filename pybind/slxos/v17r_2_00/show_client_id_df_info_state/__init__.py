
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import df_vlans
class show_client_id_df_info_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct-operational - based on the path /show-client-id-df-info-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: VLANs elected as designated forwarder
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cluster_id','__client_id','__client_state','__is_all_vlan_elected','__is_df_election_pending','__num_df_vlans','__num_df_bds','__df_bds','__df_vlans',)

  _yang_name = 'show-client-id-df-info-state'
  _rest_name = 'show-client-id-df-info-state'

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
    self.__df_bds = YANGDynClass(base=unicode, is_leaf=True, yang_name="df-bds", rest_name="df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)
    self.__is_all_vlan_elected = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-all-vlan-elected", rest_name="is-all-vlan-elected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__num_df_bds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-bds", rest_name="num-df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__df_vlans = YANGDynClass(base=YANGListType("vlan_id",df_vlans.df_vlans, yang_name="df-vlans", rest_name="df-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}), is_container='list', yang_name="df-vlans", rest_name="df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__is_df_election_pending = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-df-election-pending", rest_name="is-df-election-pending", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__num_df_vlans = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-vlans", rest_name="num-df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__client_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)

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
      return [u'show-client-id-df-info-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-client-id-df-info-state']

  def _get_cluster_id(self):
    """
    Getter method for cluster_id, mapped from YANG variable /show_client_id_df_info_state/cluster_id (uint32)

    YANG Description: Cluster ID
    """
    return self.__cluster_id
      
  def _set_cluster_id(self, v, load=False):
    """
    Setter method for cluster_id, mapped from YANG variable /show_client_id_df_info_state/cluster_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_id() directly.

    YANG Description: Cluster ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__cluster_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_id(self):
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_client_id(self):
    """
    Getter method for client_id, mapped from YANG variable /show_client_id_df_info_state/client_id (uint32)

    YANG Description: Client Id
    """
    return self.__client_id
      
  def _set_client_id(self, v, load=False):
    """
    Setter method for client_id, mapped from YANG variable /show_client_id_df_info_state/client_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_id() directly.

    YANG Description: Client Id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__client_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_id(self):
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_client_state(self):
    """
    Getter method for client_state, mapped from YANG variable /show_client_id_df_info_state/client_state (uint32)

    YANG Description: Client state
    """
    return self.__client_state
      
  def _set_client_state(self, v, load=False):
    """
    Setter method for client_state, mapped from YANG variable /show_client_id_df_info_state/client_state (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_state() directly.

    YANG Description: Client state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_state must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__client_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_state(self):
    self.__client_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_is_all_vlan_elected(self):
    """
    Getter method for is_all_vlan_elected, mapped from YANG variable /show_client_id_df_info_state/is_all_vlan_elected (uint32)

    YANG Description: All VLANs are elected as DF
    """
    return self.__is_all_vlan_elected
      
  def _set_is_all_vlan_elected(self, v, load=False):
    """
    Setter method for is_all_vlan_elected, mapped from YANG variable /show_client_id_df_info_state/is_all_vlan_elected (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_all_vlan_elected is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_all_vlan_elected() directly.

    YANG Description: All VLANs are elected as DF
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-all-vlan-elected", rest_name="is-all-vlan-elected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_all_vlan_elected must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-all-vlan-elected", rest_name="is-all-vlan-elected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__is_all_vlan_elected = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_all_vlan_elected(self):
    self.__is_all_vlan_elected = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-all-vlan-elected", rest_name="is-all-vlan-elected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_is_df_election_pending(self):
    """
    Getter method for is_df_election_pending, mapped from YANG variable /show_client_id_df_info_state/is_df_election_pending (uint32)

    YANG Description: DF election pending
    """
    return self.__is_df_election_pending
      
  def _set_is_df_election_pending(self, v, load=False):
    """
    Setter method for is_df_election_pending, mapped from YANG variable /show_client_id_df_info_state/is_df_election_pending (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_df_election_pending is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_df_election_pending() directly.

    YANG Description: DF election pending
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-df-election-pending", rest_name="is-df-election-pending", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_df_election_pending must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-df-election-pending", rest_name="is-df-election-pending", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__is_df_election_pending = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_df_election_pending(self):
    self.__is_df_election_pending = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="is-df-election-pending", rest_name="is-df-election-pending", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_num_df_vlans(self):
    """
    Getter method for num_df_vlans, mapped from YANG variable /show_client_id_df_info_state/num_df_vlans (uint32)

    YANG Description: No. of DF Vlans configured
    """
    return self.__num_df_vlans
      
  def _set_num_df_vlans(self, v, load=False):
    """
    Setter method for num_df_vlans, mapped from YANG variable /show_client_id_df_info_state/num_df_vlans (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_df_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_df_vlans() directly.

    YANG Description: No. of DF Vlans configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-vlans", rest_name="num-df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_df_vlans must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-vlans", rest_name="num-df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_df_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_df_vlans(self):
    self.__num_df_vlans = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-vlans", rest_name="num-df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_num_df_bds(self):
    """
    Getter method for num_df_bds, mapped from YANG variable /show_client_id_df_info_state/num_df_bds (uint32)

    YANG Description: No. of DF BDs configured
    """
    return self.__num_df_bds
      
  def _set_num_df_bds(self, v, load=False):
    """
    Setter method for num_df_bds, mapped from YANG variable /show_client_id_df_info_state/num_df_bds (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_df_bds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_df_bds() directly.

    YANG Description: No. of DF BDs configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-bds", rest_name="num-df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_df_bds must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-bds", rest_name="num-df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_df_bds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_df_bds(self):
    self.__num_df_bds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-df-bds", rest_name="num-df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_df_bds(self):
    """
    Getter method for df_bds, mapped from YANG variable /show_client_id_df_info_state/df_bds (string)

    YANG Description: df bds
    """
    return self.__df_bds
      
  def _set_df_bds(self, v, load=False):
    """
    Setter method for df_bds, mapped from YANG variable /show_client_id_df_info_state/df_bds (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_df_bds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_df_bds() directly.

    YANG Description: df bds
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="df-bds", rest_name="df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """df_bds must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="df-bds", rest_name="df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)""",
        })

    self.__df_bds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_df_bds(self):
    self.__df_bds = YANGDynClass(base=unicode, is_leaf=True, yang_name="df-bds", rest_name="df-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)


  def _get_df_vlans(self):
    """
    Getter method for df_vlans, mapped from YANG variable /show_client_id_df_info_state/df_vlans (list)

    YANG Description: VLANs elected as designated forwarder
    """
    return self.__df_vlans
      
  def _set_df_vlans(self, v, load=False):
    """
    Setter method for df_vlans, mapped from YANG variable /show_client_id_df_info_state/df_vlans (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_df_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_df_vlans() directly.

    YANG Description: VLANs elected as designated forwarder
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",df_vlans.df_vlans, yang_name="df-vlans", rest_name="df-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}), is_container='list', yang_name="df-vlans", rest_name="df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """df_vlans must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",df_vlans.df_vlans, yang_name="df-vlans", rest_name="df-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}), is_container='list', yang_name="df-vlans", rest_name="df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)""",
        })

    self.__df_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_df_vlans(self):
    self.__df_vlans = YANGDynClass(base=YANGListType("vlan_id",df_vlans.df_vlans, yang_name="df-vlans", rest_name="df-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}), is_container='list', yang_name="df-vlans", rest_name="df-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-df-vlans', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)

  cluster_id = __builtin__.property(_get_cluster_id)
  client_id = __builtin__.property(_get_client_id)
  client_state = __builtin__.property(_get_client_state)
  is_all_vlan_elected = __builtin__.property(_get_is_all_vlan_elected)
  is_df_election_pending = __builtin__.property(_get_is_df_election_pending)
  num_df_vlans = __builtin__.property(_get_num_df_vlans)
  num_df_bds = __builtin__.property(_get_num_df_bds)
  df_bds = __builtin__.property(_get_df_bds)
  df_vlans = __builtin__.property(_get_df_vlans)


  _pyangbind_elements = {'cluster_id': cluster_id, 'client_id': client_id, 'client_state': client_state, 'is_all_vlan_elected': is_all_vlan_elected, 'is_df_election_pending': is_df_election_pending, 'num_df_vlans': num_df_vlans, 'num_df_bds': num_df_bds, 'df_bds': df_bds, 'df_vlans': df_vlans, }


