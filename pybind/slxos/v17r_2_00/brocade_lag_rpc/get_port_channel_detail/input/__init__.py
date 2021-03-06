
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
  from YANG module brocade-lag - based on the path /brocade_lag_rpc/get-port-channel-detail/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__aggregator_id','__last_aggregator_id',)

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
    self.__aggregator_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="aggregator-id", rest_name="aggregator-id", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)
    self.__last_aggregator_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="last-aggregator-id", rest_name="last-aggregator-id", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)

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
      return [u'brocade_lag_rpc', u'get-port-channel-detail', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-port-channel-detail', u'input']

  def _get_aggregator_id(self):
    """
    Getter method for aggregator_id, mapped from YANG variable /brocade_lag_rpc/get_port_channel_detail/input/aggregator_id (interface:portchannel-type)

    YANG Description: Aggregator-id for which configuration paramaters
will be shown.
    """
    return self.__aggregator_id
      
  def _set_aggregator_id(self, v, load=False):
    """
    Setter method for aggregator_id, mapped from YANG variable /brocade_lag_rpc/get_port_channel_detail/input/aggregator_id (interface:portchannel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aggregator_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aggregator_id() directly.

    YANG Description: Aggregator-id for which configuration paramaters
will be shown.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="aggregator-id", rest_name="aggregator-id", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aggregator_id must be of a type compatible with interface:portchannel-type""",
          'defined-type': "interface:portchannel-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="aggregator-id", rest_name="aggregator-id", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)""",
        })

    self.__aggregator_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aggregator_id(self):
    self.__aggregator_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="aggregator-id", rest_name="aggregator-id", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)


  def _get_last_aggregator_id(self):
    """
    Getter method for last_aggregator_id, mapped from YANG variable /brocade_lag_rpc/get_port_channel_detail/input/last_aggregator_id (interface:portchannel-type)

    YANG Description: Aggregator-id value should be given only when previous
response indicates that more records exists. This value
will be the Id of last aggregator received in previous
response.
    """
    return self.__last_aggregator_id
      
  def _set_last_aggregator_id(self, v, load=False):
    """
    Setter method for last_aggregator_id, mapped from YANG variable /brocade_lag_rpc/get_port_channel_detail/input/last_aggregator_id (interface:portchannel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_aggregator_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_aggregator_id() directly.

    YANG Description: Aggregator-id value should be given only when previous
response indicates that more records exists. This value
will be the Id of last aggregator received in previous
response.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="last-aggregator-id", rest_name="last-aggregator-id", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_aggregator_id must be of a type compatible with interface:portchannel-type""",
          'defined-type': "interface:portchannel-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="last-aggregator-id", rest_name="last-aggregator-id", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)""",
        })

    self.__last_aggregator_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_aggregator_id(self):
    self.__last_aggregator_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="last-aggregator-id", rest_name="last-aggregator-id", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)

  aggregator_id = __builtin__.property(_get_aggregator_id, _set_aggregator_id)
  last_aggregator_id = __builtin__.property(_get_last_aggregator_id, _set_last_aggregator_id)

  __choices__ = {u'request-type': {u'get-next-request': [u'last_aggregator_id'], u'get-request': [u'aggregator_id']}}
  _pyangbind_elements = {'aggregator_id': aggregator_id, 'last_aggregator_id': last_aggregator_id, }


