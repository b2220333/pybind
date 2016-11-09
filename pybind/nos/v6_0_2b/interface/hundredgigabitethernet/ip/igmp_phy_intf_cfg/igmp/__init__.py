
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import static_group
class igmp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/ip/igmp-phy-intf-cfg/igmp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__last_member_query_interval','__query_interval','__query_max_response_time','__immediate_leave','__static_group',)

  _yang_name = 'igmp'
  _rest_name = 'igmp'

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
    self.__immediate_leave = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="immediate-leave", rest_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Immediate Leave Processing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='empty', is_config=True)
    self.__last_member_query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:lmqt-type', is_config=True)
    self.__static_group = YANGDynClass(base=YANGListType("sg_addr",static_group.static_group, yang_name="static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sg-addr', extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}), is_container='list', yang_name="static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='list', is_config=True)
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qi-type', is_config=True)
    self.__query_max_response_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qmrt-type', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'ip', u'igmp-phy-intf-cfg', u'igmp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'ip', u'igmp']

  def _get_last_member_query_interval(self):
    """
    Getter method for last_member_query_interval, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/last_member_query_interval (igmp-snooping:lmqt-type)
    """
    return self.__last_member_query_interval
      
  def _set_last_member_query_interval(self, v, load=False):
    """
    Setter method for last_member_query_interval, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/last_member_query_interval (igmp-snooping:lmqt-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_member_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_member_query_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:lmqt-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_member_query_interval must be of a type compatible with igmp-snooping:lmqt-type""",
          'defined-type': "igmp-snooping:lmqt-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:lmqt-type', is_config=True)""",
        })

    self.__last_member_query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_member_query_interval(self):
    self.__last_member_query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:lmqt-type', is_config=True)


  def _get_query_interval(self):
    """
    Getter method for query_interval, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/query_interval (igmp-snooping:qi-type)
    """
    return self.__query_interval
      
  def _set_query_interval(self, v, load=False):
    """
    Setter method for query_interval, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/query_interval (igmp-snooping:qi-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_query_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qi-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """query_interval must be of a type compatible with igmp-snooping:qi-type""",
          'defined-type': "igmp-snooping:qi-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qi-type', is_config=True)""",
        })

    self.__query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_query_interval(self):
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qi-type', is_config=True)


  def _get_query_max_response_time(self):
    """
    Getter method for query_max_response_time, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/query_max_response_time (igmp-snooping:qmrt-type)
    """
    return self.__query_max_response_time
      
  def _set_query_max_response_time(self, v, load=False):
    """
    Setter method for query_max_response_time, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/query_max_response_time (igmp-snooping:qmrt-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_query_max_response_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_query_max_response_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qmrt-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """query_max_response_time must be of a type compatible with igmp-snooping:qmrt-type""",
          'defined-type': "igmp-snooping:qmrt-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qmrt-type', is_config=True)""",
        })

    self.__query_max_response_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_query_max_response_time(self):
    self.__query_max_response_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='igmp-snooping:qmrt-type', is_config=True)


  def _get_immediate_leave(self):
    """
    Getter method for immediate_leave, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/immediate_leave (empty)
    """
    return self.__immediate_leave
      
  def _set_immediate_leave(self, v, load=False):
    """
    Setter method for immediate_leave, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/immediate_leave (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_immediate_leave is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_immediate_leave() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="immediate-leave", rest_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Immediate Leave Processing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """immediate_leave must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="immediate-leave", rest_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Immediate Leave Processing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='empty', is_config=True)""",
        })

    self.__immediate_leave = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_immediate_leave(self):
    self.__immediate_leave = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="immediate-leave", rest_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Immediate Leave Processing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='empty', is_config=True)


  def _get_static_group(self):
    """
    Getter method for static_group, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/static_group (list)
    """
    return self.__static_group
      
  def _set_static_group(self, v, load=False):
    """
    Setter method for static_group, mapped from YANG variable /interface/hundredgigabitethernet/ip/igmp_phy_intf_cfg/igmp/static_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_group() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("sg_addr",static_group.static_group, yang_name="static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sg-addr', extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}), is_container='list', yang_name="static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sg_addr",static_group.static_group, yang_name="static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sg-addr', extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}), is_container='list', yang_name="static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='list', is_config=True)""",
        })

    self.__static_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_group(self):
    self.__static_group = YANGDynClass(base=YANGListType("sg_addr",static_group.static_group, yang_name="static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sg-addr', extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}), is_container='list', yang_name="static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static Group to be Joined', u'cli-suppress-mode': None, u'callpoint': u'IgmpSgPhy'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='list', is_config=True)

  last_member_query_interval = __builtin__.property(_get_last_member_query_interval, _set_last_member_query_interval)
  query_interval = __builtin__.property(_get_query_interval, _set_query_interval)
  query_max_response_time = __builtin__.property(_get_query_max_response_time, _set_query_max_response_time)
  immediate_leave = __builtin__.property(_get_immediate_leave, _set_immediate_leave)
  static_group = __builtin__.property(_get_static_group, _set_static_group)


  _pyangbind_elements = {'last_member_query_interval': last_member_query_interval, 'query_interval': query_interval, 'query_max_response_time': query_max_response_time, 'immediate_leave': immediate_leave, 'static_group': static_group, }


