
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import preferred
class lifetime(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/ipv6/ipv6-nd-ra/ipv6-intf-cmds/nd/prefix/lifetime. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__no_advertise','__valid_lifetime','__valid_infinite','__preferred',)

  _yang_name = 'lifetime'
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
    self.__valid_lifetime = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="valid-lifetime", rest_name="", parent=self, choice=(u'ch-valid-type', u'ca-valid-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures valid lifetime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)
    self.__valid_infinite = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="valid-infinite", rest_name="infinite", parent=self, choice=(u'ch-valid-type', u'ca-valid-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite valid lifetime', u'alt-name': u'infinite', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__preferred = YANGDynClass(base=preferred.preferred, is_container='container', yang_name="preferred", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    self.__no_advertise = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-advertise", rest_name="no-advertise", parent=self, choice=(u'ch-valid-type', u'ca-no-advertise'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not advertise prefix', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds', u'nd', u'prefix', u'lifetime']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'ipv6', u'nd', u'prefix']

  def _get_no_advertise(self):
    """
    Getter method for no_advertise, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/no_advertise (empty)
    """
    return self.__no_advertise
      
  def _set_no_advertise(self, v, load=False):
    """
    Setter method for no_advertise, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/no_advertise (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_advertise is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_advertise() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="no-advertise", rest_name="no-advertise", parent=self, choice=(u'ch-valid-type', u'ca-no-advertise'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not advertise prefix', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_advertise must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-advertise", rest_name="no-advertise", parent=self, choice=(u'ch-valid-type', u'ca-no-advertise'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not advertise prefix', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__no_advertise = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_advertise(self):
    self.__no_advertise = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-advertise", rest_name="no-advertise", parent=self, choice=(u'ch-valid-type', u'ca-no-advertise'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not advertise prefix', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_valid_lifetime(self):
    """
    Getter method for valid_lifetime, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/valid_lifetime (common-def:time-interval-sec)
    """
    return self.__valid_lifetime
      
  def _set_valid_lifetime(self, v, load=False):
    """
    Setter method for valid_lifetime, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/valid_lifetime (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_valid_lifetime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_valid_lifetime() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="valid-lifetime", rest_name="", parent=self, choice=(u'ch-valid-type', u'ca-valid-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures valid lifetime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """valid_lifetime must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="valid-lifetime", rest_name="", parent=self, choice=(u'ch-valid-type', u'ca-valid-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures valid lifetime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__valid_lifetime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_valid_lifetime(self):
    self.__valid_lifetime = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="valid-lifetime", rest_name="", parent=self, choice=(u'ch-valid-type', u'ca-valid-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures valid lifetime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_valid_infinite(self):
    """
    Getter method for valid_infinite, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/valid_infinite (empty)
    """
    return self.__valid_infinite
      
  def _set_valid_infinite(self, v, load=False):
    """
    Setter method for valid_infinite, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/valid_infinite (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_valid_infinite is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_valid_infinite() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="valid-infinite", rest_name="infinite", parent=self, choice=(u'ch-valid-type', u'ca-valid-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite valid lifetime', u'alt-name': u'infinite', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """valid_infinite must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="valid-infinite", rest_name="infinite", parent=self, choice=(u'ch-valid-type', u'ca-valid-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite valid lifetime', u'alt-name': u'infinite', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__valid_infinite = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_valid_infinite(self):
    self.__valid_infinite = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="valid-infinite", rest_name="infinite", parent=self, choice=(u'ch-valid-type', u'ca-valid-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite valid lifetime', u'alt-name': u'infinite', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_preferred(self):
    """
    Getter method for preferred, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred (container)
    """
    return self.__preferred
      
  def _set_preferred(self, v, load=False):
    """
    Setter method for preferred, mapped from YANG variable /interface/tengigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_preferred is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_preferred() directly.
    """
    try:
      t = YANGDynClass(v,base=preferred.preferred, is_container='container', yang_name="preferred", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """preferred must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=preferred.preferred, is_container='container', yang_name="preferred", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)""",
        })

    self.__preferred = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_preferred(self):
    self.__preferred = YANGDynClass(base=preferred.preferred, is_container='container', yang_name="preferred", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)

  no_advertise = __builtin__.property(_get_no_advertise, _set_no_advertise)
  valid_lifetime = __builtin__.property(_get_valid_lifetime, _set_valid_lifetime)
  valid_infinite = __builtin__.property(_get_valid_infinite, _set_valid_infinite)
  preferred = __builtin__.property(_get_preferred, _set_preferred)

  __choices__ = {u'ch-valid-type': {u'ca-valid-lifetime': [u'valid_lifetime'], u'ca-no-advertise': [u'no_advertise'], u'ca-valid-infinite': [u'valid_infinite']}}
  _pyangbind_elements = {'no_advertise': no_advertise, 'valid_lifetime': valid_lifetime, 'valid_infinite': valid_infinite, 'preferred': preferred, }


