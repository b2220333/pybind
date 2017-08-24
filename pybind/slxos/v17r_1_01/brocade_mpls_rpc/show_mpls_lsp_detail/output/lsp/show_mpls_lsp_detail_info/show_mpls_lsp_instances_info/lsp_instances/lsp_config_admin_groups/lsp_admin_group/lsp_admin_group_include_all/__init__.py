
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class lsp_admin_group_include_all(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-lsp-detail/output/lsp/show-mpls-lsp-detail-info/show-mpls-lsp-instances-info/lsp-instances/lsp-config-admin-groups/lsp-admin-group/lsp-admin-group-include-all. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_admin_group_include_all_group_id',)

  _yang_name = 'lsp-admin-group-include-all'
  _rest_name = 'lsp-admin-group-include-all'

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
    self.__lsp_admin_group_include_all_group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-admin-group-include-all-group-id", rest_name="lsp-admin-group-include-all-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-lsp-detail', u'output', u'lsp', u'show-mpls-lsp-detail-info', u'show-mpls-lsp-instances-info', u'lsp-instances', u'lsp-config-admin-groups', u'lsp-admin-group', u'lsp-admin-group-include-all']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-lsp-detail', u'output', u'lsp', u'lsp-instances', u'lsp-config-admin-groups', u'lsp-admin-group-include-all']

  def _get_lsp_admin_group_include_all_group_id(self):
    """
    Getter method for lsp_admin_group_include_all_group_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_instances_info/lsp_instances/lsp_config_admin_groups/lsp_admin_group/lsp_admin_group_include_all/lsp_admin_group_include_all_group_id (uint32)

    YANG Description: Include all admin group id
    """
    return self.__lsp_admin_group_include_all_group_id
      
  def _set_lsp_admin_group_include_all_group_id(self, v, load=False):
    """
    Setter method for lsp_admin_group_include_all_group_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_instances_info/lsp_instances/lsp_config_admin_groups/lsp_admin_group/lsp_admin_group_include_all/lsp_admin_group_include_all_group_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_admin_group_include_all_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_admin_group_include_all_group_id() directly.

    YANG Description: Include all admin group id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-admin-group-include-all-group-id", rest_name="lsp-admin-group-include-all-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_admin_group_include_all_group_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-admin-group-include-all-group-id", rest_name="lsp-admin-group-include-all-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__lsp_admin_group_include_all_group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_admin_group_include_all_group_id(self):
    self.__lsp_admin_group_include_all_group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-admin-group-include-all-group-id", rest_name="lsp-admin-group-include-all-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  lsp_admin_group_include_all_group_id = __builtin__.property(_get_lsp_admin_group_include_all_group_id, _set_lsp_admin_group_include_all_group_id)


  _pyangbind_elements = {'lsp_admin_group_include_all_group_id': lsp_admin_group_include_all_group_id, }


