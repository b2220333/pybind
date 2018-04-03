
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class slm_stats_session_history_brief(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag-operational - based on the path /cfm-state/slm/slm-stats-session-brief/slm-stats-session-history-brief. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Brief display of SLM statistics for histories
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__suspect_status','__start_time','__elapsed_time','__tx_fwd','__rx_fwd','__tx_bwd','__rx_bwd','__flr_ratio','__blr_ratio','__history_index',)

  _yang_name = 'slm-stats-session-history-brief'
  _rest_name = 'slm-stats-session-history-brief'

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
    self.__tx_bwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-bwd", rest_name="tx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    self.__rx_bwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-bwd", rest_name="rx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    self.__blr_ratio = YANGDynClass(base=unicode, is_leaf=True, yang_name="blr-ratio", rest_name="blr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    self.__suspect_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suspect-status", rest_name="suspect-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='boolean', is_config=False)
    self.__elapsed_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="elapsed-time", rest_name="elapsed-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    self.__history_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="history-index", rest_name="history-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    self.__flr_ratio = YANGDynClass(base=unicode, is_leaf=True, yang_name="flr-ratio", rest_name="flr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    self.__rx_fwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-fwd", rest_name="rx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    self.__tx_fwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-fwd", rest_name="tx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    self.__start_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)

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
      return [u'cfm-state', u'slm', u'slm-stats-session-brief', u'slm-stats-session-history-brief']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cfm-state', u'slm', u'slm-stats-session-brief', u'slm-stats-session-history-brief']

  def _get_suspect_status(self):
    """
    Getter method for suspect_status, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/suspect_status (boolean)

    YANG Description: Suspect status
    """
    return self.__suspect_status
      
  def _set_suspect_status(self, v, load=False):
    """
    Setter method for suspect_status, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/suspect_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suspect_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suspect_status() directly.

    YANG Description: Suspect status
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suspect-status", rest_name="suspect-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suspect_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suspect-status", rest_name="suspect-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='boolean', is_config=False)""",
        })

    self.__suspect_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suspect_status(self):
    self.__suspect_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suspect-status", rest_name="suspect-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='boolean', is_config=False)


  def _get_start_time(self):
    """
    Getter method for start_time, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/start_time (string)

    YANG Description: Start time
    """
    return self.__start_time
      
  def _set_start_time(self, v, load=False):
    """
    Setter method for start_time, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/start_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_time() directly.

    YANG Description: Start time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__start_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_time(self):
    self.__start_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_elapsed_time(self):
    """
    Getter method for elapsed_time, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/elapsed_time (string)

    YANG Description: Start time
    """
    return self.__elapsed_time
      
  def _set_elapsed_time(self, v, load=False):
    """
    Setter method for elapsed_time, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/elapsed_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_elapsed_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_elapsed_time() directly.

    YANG Description: Start time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="elapsed-time", rest_name="elapsed-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """elapsed_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="elapsed-time", rest_name="elapsed-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__elapsed_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_elapsed_time(self):
    self.__elapsed_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="elapsed-time", rest_name="elapsed-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_tx_fwd(self):
    """
    Getter method for tx_fwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/tx_fwd (uint32)

    YANG Description: TX in Forward direction
    """
    return self.__tx_fwd
      
  def _set_tx_fwd(self, v, load=False):
    """
    Setter method for tx_fwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/tx_fwd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_fwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_fwd() directly.

    YANG Description: TX in Forward direction
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-fwd", rest_name="tx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_fwd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-fwd", rest_name="tx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tx_fwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_fwd(self):
    self.__tx_fwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-fwd", rest_name="tx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)


  def _get_rx_fwd(self):
    """
    Getter method for rx_fwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/rx_fwd (uint32)

    YANG Description: RX in Forward direction
    """
    return self.__rx_fwd
      
  def _set_rx_fwd(self, v, load=False):
    """
    Setter method for rx_fwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/rx_fwd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rx_fwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rx_fwd() directly.

    YANG Description: RX in Forward direction
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-fwd", rest_name="rx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rx_fwd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-fwd", rest_name="rx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__rx_fwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rx_fwd(self):
    self.__rx_fwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-fwd", rest_name="rx-fwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)


  def _get_tx_bwd(self):
    """
    Getter method for tx_bwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/tx_bwd (uint32)

    YANG Description: TX in Backward direction
    """
    return self.__tx_bwd
      
  def _set_tx_bwd(self, v, load=False):
    """
    Setter method for tx_bwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/tx_bwd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_bwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_bwd() directly.

    YANG Description: TX in Backward direction
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-bwd", rest_name="tx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_bwd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-bwd", rest_name="tx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tx_bwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_bwd(self):
    self.__tx_bwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tx-bwd", rest_name="tx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)


  def _get_rx_bwd(self):
    """
    Getter method for rx_bwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/rx_bwd (uint32)

    YANG Description: RX in Backward direction
    """
    return self.__rx_bwd
      
  def _set_rx_bwd(self, v, load=False):
    """
    Setter method for rx_bwd, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/rx_bwd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rx_bwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rx_bwd() directly.

    YANG Description: RX in Backward direction
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-bwd", rest_name="rx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rx_bwd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-bwd", rest_name="rx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__rx_bwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rx_bwd(self):
    self.__rx_bwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rx-bwd", rest_name="rx-bwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)


  def _get_flr_ratio(self):
    """
    Getter method for flr_ratio, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/flr_ratio (string)

    YANG Description: FLR (Ratio)
    """
    return self.__flr_ratio
      
  def _set_flr_ratio(self, v, load=False):
    """
    Setter method for flr_ratio, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/flr_ratio (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flr_ratio is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flr_ratio() directly.

    YANG Description: FLR (Ratio)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="flr-ratio", rest_name="flr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flr_ratio must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="flr-ratio", rest_name="flr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__flr_ratio = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flr_ratio(self):
    self.__flr_ratio = YANGDynClass(base=unicode, is_leaf=True, yang_name="flr-ratio", rest_name="flr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_blr_ratio(self):
    """
    Getter method for blr_ratio, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/blr_ratio (string)

    YANG Description: BLR (Ratio)
    """
    return self.__blr_ratio
      
  def _set_blr_ratio(self, v, load=False):
    """
    Setter method for blr_ratio, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/blr_ratio (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blr_ratio is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blr_ratio() directly.

    YANG Description: BLR (Ratio)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="blr-ratio", rest_name="blr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blr_ratio must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="blr-ratio", rest_name="blr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__blr_ratio = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blr_ratio(self):
    self.__blr_ratio = YANGDynClass(base=unicode, is_leaf=True, yang_name="blr-ratio", rest_name="blr-ratio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_history_index(self):
    """
    Getter method for history_index, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/history_index (uint32)

    YANG Description: SLM history index for the session
    """
    return self.__history_index
      
  def _set_history_index(self, v, load=False):
    """
    Setter method for history_index, mapped from YANG variable /cfm_state/slm/slm_stats_session_brief/slm_stats_session_history_brief/history_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_history_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_history_index() directly.

    YANG Description: SLM history index for the session
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="history-index", rest_name="history-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """history_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="history-index", rest_name="history-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__history_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_history_index(self):
    self.__history_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="history-index", rest_name="history-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)

  suspect_status = __builtin__.property(_get_suspect_status)
  start_time = __builtin__.property(_get_start_time)
  elapsed_time = __builtin__.property(_get_elapsed_time)
  tx_fwd = __builtin__.property(_get_tx_fwd)
  rx_fwd = __builtin__.property(_get_rx_fwd)
  tx_bwd = __builtin__.property(_get_tx_bwd)
  rx_bwd = __builtin__.property(_get_rx_bwd)
  flr_ratio = __builtin__.property(_get_flr_ratio)
  blr_ratio = __builtin__.property(_get_blr_ratio)
  history_index = __builtin__.property(_get_history_index)


  _pyangbind_elements = {'suspect_status': suspect_status, 'start_time': start_time, 'elapsed_time': elapsed_time, 'tx_fwd': tx_fwd, 'rx_fwd': rx_fwd, 'tx_bwd': tx_bwd, 'rx_bwd': rx_bwd, 'flr_ratio': flr_ratio, 'blr_ratio': blr_ratio, 'history_index': history_index, }

