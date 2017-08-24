
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class egress_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-access-list - based on the path /brocade_mac_access_list_rpc/get-mac-acl-for-intf/output/interface/egress-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Egress policy details applied on this
interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__policy_name',)

  _yang_name = 'egress-policy'
  _rest_name = 'egress-policy'

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
    self.__policy_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="policy-name", rest_name="policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='string', is_config=True)

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
      return [u'brocade_mac_access_list_rpc', u'get-mac-acl-for-intf', u'output', u'interface', u'egress-policy']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-mac-acl-for-intf', u'output', u'interface', u'egress-policy']

  def _get_policy_name(self):
    """
    Getter method for policy_name, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/egress_policy/policy_name (string)

    YANG Description: MAC ACL policy name.
    """
    return self.__policy_name
      
  def _set_policy_name(self, v, load=False):
    """
    Setter method for policy_name, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/egress_policy/policy_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy_name() directly.

    YANG Description: MAC ACL policy name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="policy-name", rest_name="policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="policy-name", rest_name="policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='string', is_config=True)""",
        })

    self.__policy_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy_name(self):
    self.__policy_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="policy-name", rest_name="policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='string', is_config=True)

  policy_name = __builtin__.property(_get_policy_name, _set_policy_name)


  _pyangbind_elements = {'policy_name': policy_name, }


