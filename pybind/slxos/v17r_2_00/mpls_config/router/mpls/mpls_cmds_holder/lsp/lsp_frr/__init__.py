
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import lsp_frr_bandwidth
import lsp_frr_priority
import lsp_frr_revertive
class lsp_frr(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/lsp/lsp-frr. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_frr_bandwidth','__lsp_frr_exclude_any','__lsp_frr_include_any','__lsp_frr_include_all','__lsp_frr_hop_limit','__lsp_frr_facility_backup','__lsp_frr_link_protection','__lsp_frr_priority','__lsp_frr_revertive',)

  _yang_name = 'lsp-frr'
  _rest_name = 'frr'

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
    self.__lsp_frr_include_all = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-all", rest_name="include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include all of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_frr_priority = YANGDynClass(base=lsp_frr_priority.lsp_frr_priority, is_container='container', presence=False, yang_name="lsp-frr-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Setup/hold priorites', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__lsp_frr_exclude_any = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-exclude-any", rest_name="exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Exclude any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'exclude-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_frr_link_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-link-protection", rest_name="link-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Request link protection for LSP', u'cli-full-no': None, u'alt-name': u'link-protection'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__lsp_frr_include_any = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-any", rest_name="include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_frr_revertive = YANGDynClass(base=lsp_frr_revertive.lsp_frr_revertive, is_container='container', presence=False, yang_name="lsp-frr-revertive", rest_name="revertive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRR revertiveness for the LSP', u'alt-name': u'revertive', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__lsp_frr_hop_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="lsp-frr-hop-limit", rest_name="hop-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Limit of hops the detour/backup LSP can traverse (from PLR to MP)', u'cli-full-no': None, u'alt-name': u'hop-limit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    self.__lsp_frr_facility_backup = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-facility-backup", rest_name="facility-backup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select the frr protection mode', u'cli-full-no': None, u'alt-name': u'facility-backup'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__lsp_frr_bandwidth = YANGDynClass(base=lsp_frr_bandwidth.lsp_frr_bandwidth, is_container='container', presence=False, yang_name="lsp-frr-bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set bandwidth for detour/backup LSP', u'alt-name': u'bandwidth'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'lsp', u'lsp-frr']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'lsp', u'frr']

  def _get_lsp_frr_bandwidth(self):
    """
    Getter method for lsp_frr_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_bandwidth (container)
    """
    return self.__lsp_frr_bandwidth
      
  def _set_lsp_frr_bandwidth(self, v, load=False):
    """
    Setter method for lsp_frr_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_bandwidth (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_bandwidth() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lsp_frr_bandwidth.lsp_frr_bandwidth, is_container='container', presence=False, yang_name="lsp-frr-bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set bandwidth for detour/backup LSP', u'alt-name': u'bandwidth'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_bandwidth must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lsp_frr_bandwidth.lsp_frr_bandwidth, is_container='container', presence=False, yang_name="lsp-frr-bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set bandwidth for detour/backup LSP', u'alt-name': u'bandwidth'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__lsp_frr_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_bandwidth(self):
    self.__lsp_frr_bandwidth = YANGDynClass(base=lsp_frr_bandwidth.lsp_frr_bandwidth, is_container='container', presence=False, yang_name="lsp-frr-bandwidth", rest_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set bandwidth for detour/backup LSP', u'alt-name': u'bandwidth'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_lsp_frr_exclude_any(self):
    """
    Getter method for lsp_frr_exclude_any, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_exclude_any (string)
    """
    return self.__lsp_frr_exclude_any
      
  def _set_lsp_frr_exclude_any(self, v, load=False):
    """
    Setter method for lsp_frr_exclude_any, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_exclude_any (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_exclude_any is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_exclude_any() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-exclude-any", rest_name="exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Exclude any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'exclude-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_exclude_any must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-exclude-any", rest_name="exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Exclude any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'exclude-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_frr_exclude_any = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_exclude_any(self):
    self.__lsp_frr_exclude_any = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-exclude-any", rest_name="exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Exclude any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'exclude-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_lsp_frr_include_any(self):
    """
    Getter method for lsp_frr_include_any, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_include_any (string)
    """
    return self.__lsp_frr_include_any
      
  def _set_lsp_frr_include_any(self, v, load=False):
    """
    Setter method for lsp_frr_include_any, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_include_any (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_include_any is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_include_any() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-any", rest_name="include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_include_any must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-any", rest_name="include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_frr_include_any = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_include_any(self):
    self.__lsp_frr_include_any = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-any", rest_name="include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include any of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-any'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_lsp_frr_include_all(self):
    """
    Getter method for lsp_frr_include_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_include_all (string)
    """
    return self.__lsp_frr_include_all
      
  def _set_lsp_frr_include_all(self, v, load=False):
    """
    Setter method for lsp_frr_include_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_include_all (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_include_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_include_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-all", rest_name="include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include all of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_include_all must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-all", rest_name="include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include all of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_frr_include_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_include_all(self):
    self.__lsp_frr_include_all = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..256']})), is_leaf=False, yang_name="lsp-frr-include-all", rest_name="include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include all of the administrative groups', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'cli-flat-list-syntax': None, u'alt-name': u'include-all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_lsp_frr_hop_limit(self):
    """
    Getter method for lsp_frr_hop_limit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_hop_limit (uint8)
    """
    return self.__lsp_frr_hop_limit
      
  def _set_lsp_frr_hop_limit(self, v, load=False):
    """
    Setter method for lsp_frr_hop_limit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_hop_limit (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_hop_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_hop_limit() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="lsp-frr-hop-limit", rest_name="hop-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Limit of hops the detour/backup LSP can traverse (from PLR to MP)', u'cli-full-no': None, u'alt-name': u'hop-limit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_hop_limit must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="lsp-frr-hop-limit", rest_name="hop-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Limit of hops the detour/backup LSP can traverse (from PLR to MP)', u'cli-full-no': None, u'alt-name': u'hop-limit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__lsp_frr_hop_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_hop_limit(self):
    self.__lsp_frr_hop_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="lsp-frr-hop-limit", rest_name="hop-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Limit of hops the detour/backup LSP can traverse (from PLR to MP)', u'cli-full-no': None, u'alt-name': u'hop-limit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_lsp_frr_facility_backup(self):
    """
    Getter method for lsp_frr_facility_backup, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_facility_backup (empty)
    """
    return self.__lsp_frr_facility_backup
      
  def _set_lsp_frr_facility_backup(self, v, load=False):
    """
    Setter method for lsp_frr_facility_backup, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_facility_backup (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_facility_backup is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_facility_backup() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-frr-facility-backup", rest_name="facility-backup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select the frr protection mode', u'cli-full-no': None, u'alt-name': u'facility-backup'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_facility_backup must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-facility-backup", rest_name="facility-backup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select the frr protection mode', u'cli-full-no': None, u'alt-name': u'facility-backup'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__lsp_frr_facility_backup = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_facility_backup(self):
    self.__lsp_frr_facility_backup = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-facility-backup", rest_name="facility-backup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select the frr protection mode', u'cli-full-no': None, u'alt-name': u'facility-backup'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_lsp_frr_link_protection(self):
    """
    Getter method for lsp_frr_link_protection, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_link_protection (empty)
    """
    return self.__lsp_frr_link_protection
      
  def _set_lsp_frr_link_protection(self, v, load=False):
    """
    Setter method for lsp_frr_link_protection, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_link_protection (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_link_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_link_protection() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-frr-link-protection", rest_name="link-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Request link protection for LSP', u'cli-full-no': None, u'alt-name': u'link-protection'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_link_protection must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-link-protection", rest_name="link-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Request link protection for LSP', u'cli-full-no': None, u'alt-name': u'link-protection'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__lsp_frr_link_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_link_protection(self):
    self.__lsp_frr_link_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-link-protection", rest_name="link-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Request link protection for LSP', u'cli-full-no': None, u'alt-name': u'link-protection'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_lsp_frr_priority(self):
    """
    Getter method for lsp_frr_priority, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_priority (container)
    """
    return self.__lsp_frr_priority
      
  def _set_lsp_frr_priority(self, v, load=False):
    """
    Setter method for lsp_frr_priority, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_priority (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lsp_frr_priority.lsp_frr_priority, is_container='container', presence=False, yang_name="lsp-frr-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Setup/hold priorites', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_priority must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lsp_frr_priority.lsp_frr_priority, is_container='container', presence=False, yang_name="lsp-frr-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Setup/hold priorites', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__lsp_frr_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_priority(self):
    self.__lsp_frr_priority = YANGDynClass(base=lsp_frr_priority.lsp_frr_priority, is_container='container', presence=False, yang_name="lsp-frr-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Setup/hold priorites', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_lsp_frr_revertive(self):
    """
    Getter method for lsp_frr_revertive, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_revertive (container)
    """
    return self.__lsp_frr_revertive
      
  def _set_lsp_frr_revertive(self, v, load=False):
    """
    Setter method for lsp_frr_revertive, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_revertive (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_revertive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_revertive() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lsp_frr_revertive.lsp_frr_revertive, is_container='container', presence=False, yang_name="lsp-frr-revertive", rest_name="revertive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRR revertiveness for the LSP', u'alt-name': u'revertive', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_revertive must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lsp_frr_revertive.lsp_frr_revertive, is_container='container', presence=False, yang_name="lsp-frr-revertive", rest_name="revertive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRR revertiveness for the LSP', u'alt-name': u'revertive', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__lsp_frr_revertive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_revertive(self):
    self.__lsp_frr_revertive = YANGDynClass(base=lsp_frr_revertive.lsp_frr_revertive, is_container='container', presence=False, yang_name="lsp-frr-revertive", rest_name="revertive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRR revertiveness for the LSP', u'alt-name': u'revertive', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  lsp_frr_bandwidth = __builtin__.property(_get_lsp_frr_bandwidth, _set_lsp_frr_bandwidth)
  lsp_frr_exclude_any = __builtin__.property(_get_lsp_frr_exclude_any, _set_lsp_frr_exclude_any)
  lsp_frr_include_any = __builtin__.property(_get_lsp_frr_include_any, _set_lsp_frr_include_any)
  lsp_frr_include_all = __builtin__.property(_get_lsp_frr_include_all, _set_lsp_frr_include_all)
  lsp_frr_hop_limit = __builtin__.property(_get_lsp_frr_hop_limit, _set_lsp_frr_hop_limit)
  lsp_frr_facility_backup = __builtin__.property(_get_lsp_frr_facility_backup, _set_lsp_frr_facility_backup)
  lsp_frr_link_protection = __builtin__.property(_get_lsp_frr_link_protection, _set_lsp_frr_link_protection)
  lsp_frr_priority = __builtin__.property(_get_lsp_frr_priority, _set_lsp_frr_priority)
  lsp_frr_revertive = __builtin__.property(_get_lsp_frr_revertive, _set_lsp_frr_revertive)


  _pyangbind_elements = {'lsp_frr_bandwidth': lsp_frr_bandwidth, 'lsp_frr_exclude_any': lsp_frr_exclude_any, 'lsp_frr_include_any': lsp_frr_include_any, 'lsp_frr_include_all': lsp_frr_include_all, 'lsp_frr_hop_limit': lsp_frr_hop_limit, 'lsp_frr_facility_backup': lsp_frr_facility_backup, 'lsp_frr_link_protection': lsp_frr_link_protection, 'lsp_frr_priority': lsp_frr_priority, 'lsp_frr_revertive': lsp_frr_revertive, }


