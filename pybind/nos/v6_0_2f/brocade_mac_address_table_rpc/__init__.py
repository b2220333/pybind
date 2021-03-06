
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_mac_address_table
class brocade_mac_address_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /brocade_mac_address_table_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Mac forwarding table
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__get_mac_address_table',)

  _yang_name = 'brocade-mac-address-table'
  _rest_name = ''

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
    self.__get_mac_address_table = YANGDynClass(base=get_mac_address_table.get_mac_address_table, is_leaf=True, yang_name="get-mac-address-table", rest_name="get-mac-address-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getl2sysmac-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='rpc', is_config=True)

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
      return [u'brocade_mac_address_table_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_get_mac_address_table(self):
    """
    Getter method for get_mac_address_table, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table (rpc)

    YANG Description: This is a function that returns operational data for a
given mac entry and the corresponding details of that mac
entry. The mac entries are fetched similar to the snmp 
get-next model. When no input is given to this rpc, first
set of mac entries will be fetched. If there are any
more extra mac entries that are there to be fetched,
the flag has-more at the end of the o/p will be set to
true. To get the next set of mac entries, this rpc has to
be queried again with the last mac entry details of the
previous set as the input in get-next-request case. With
get-next-request all three fields i.e. last-mac-address,
last-vlan-id and last-mac-type need to be passed as input.
When the rpc is queried with a mac-address as input in the 
get-request case the corresponding mac entry, if exists,
will be fetched.
    """
    return self.__get_mac_address_table
      
  def _set_get_mac_address_table(self, v, load=False):
    """
    Setter method for get_mac_address_table, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_mac_address_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_mac_address_table() directly.

    YANG Description: This is a function that returns operational data for a
given mac entry and the corresponding details of that mac
entry. The mac entries are fetched similar to the snmp 
get-next model. When no input is given to this rpc, first
set of mac entries will be fetched. If there are any
more extra mac entries that are there to be fetched,
the flag has-more at the end of the o/p will be set to
true. To get the next set of mac entries, this rpc has to
be queried again with the last mac entry details of the
previous set as the input in get-next-request case. With
get-next-request all three fields i.e. last-mac-address,
last-vlan-id and last-mac-type need to be passed as input.
When the rpc is queried with a mac-address as input in the 
get-request case the corresponding mac entry, if exists,
will be fetched.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_mac_address_table.get_mac_address_table, is_leaf=True, yang_name="get-mac-address-table", rest_name="get-mac-address-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getl2sysmac-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_mac_address_table must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_mac_address_table.get_mac_address_table, is_leaf=True, yang_name="get-mac-address-table", rest_name="get-mac-address-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getl2sysmac-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='rpc', is_config=True)""",
        })

    self.__get_mac_address_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_mac_address_table(self):
    self.__get_mac_address_table = YANGDynClass(base=get_mac_address_table.get_mac_address_table, is_leaf=True, yang_name="get-mac-address-table", rest_name="get-mac-address-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getl2sysmac-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='rpc', is_config=True)

  get_mac_address_table = __builtin__.property(_get_get_mac_address_table, _set_get_mac_address_table)


  _pyangbind_elements = {'get_mac_address_table': get_mac_address_table, }


