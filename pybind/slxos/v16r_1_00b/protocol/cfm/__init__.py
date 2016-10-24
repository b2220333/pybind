
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import domain_name
class cfm(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/cfm. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__domain_name',)

  _yang_name = 'cfm'
  _rest_name = 'cfm'

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
    self.__domain_name = YANGDynClass(base=YANGListType("domain_name",domain_name.domain_name, yang_name="domain-name", rest_name="domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name', extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}), is_container='list', yang_name="domain-name", rest_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

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
      return [u'protocol', u'cfm']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'cfm']

  def _get_domain_name(self):
    """
    Getter method for domain_name, mapped from YANG variable /protocol/cfm/domain_name (list)
    """
    return self.__domain_name
      
  def _set_domain_name(self, v, load=False):
    """
    Setter method for domain_name, mapped from YANG variable /protocol/cfm/domain_name (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_name() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("domain_name",domain_name.domain_name, yang_name="domain-name", rest_name="domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name', extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}), is_container='list', yang_name="domain-name", rest_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_name must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("domain_name",domain_name.domain_name, yang_name="domain-name", rest_name="domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name', extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}), is_container='list', yang_name="domain-name", rest_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)""",
        })

    self.__domain_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_name(self):
    self.__domain_name = YANGDynClass(base=YANGListType("domain_name",domain_name.domain_name, yang_name="domain-name", rest_name="domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name', extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}), is_container='list', yang_name="domain-name", rest_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance Domain', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agDomain', u'cli-mode-name': u'config-cfm-md-$(domain-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

  domain_name = __builtin__.property(_get_domain_name, _set_domain_name)


  _pyangbind_elements = {'domain_name': domain_name, }


