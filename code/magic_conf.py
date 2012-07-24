"""
Configuration is read from a default configuration file, from an
optional ini file which overrides it and optionally from a key/value
entries passed from the command line
"""

from importlib import import_module
from inspect import getmembers
from os import path

from ConfigParser import ConfigParser

KEY_VAL_SEP = ':'

DEFAULT_CONF_MODULE = 'auto_tester.default_conf'
DEFAULT_INI_CONF = path.join(path.dirname(__file__), 'autotest.conf')

GLOBAL_CONF = None


def get_conf():
    """Return the global configuration, loading it first if necessary
    """
    if GLOBAL_CONF is None:
        load_conf()

    return GLOBAL_CONF


class Conf:
    def __init__(self, conf_file, default=None):
        # TODO: check if the allowEmpty flag is really needed
        self.conf = ConfigParser()
        self.conf_dict = default or {}
        self.conf.read(conf_file)
        self._conf_to_dict()

    def _conf_to_dict(self):
        # TODO: add type checking
        for sec in self.conf.sections():
            if sec not in self.conf_dict:
                self.conf_dict[sec] = {}

            for k, v in self.conf.items(sec):
                self.conf_dict[sec][k] = v

    def __getitem__(self, item):
        return self.conf_dict[item]

    def __getattr__(self, attr):
        return self.__getitem__(attr)

    def to_args(self):
        return list(dict_to_args(self.conf_dict))

    def update_from_vars(self, varargs):
        # the update adds new entries if they don't exist, but
        # args_to_dict would fail if there are entries which were not
        # in the original dictionary, so using update it's safe in
        # this case
        tmp_dic = args_to_dict(varargs, self.conf_dict)
        self.conf_dict.update(tmp_dic)


def load_conf(conf_file=DEFAULT_INI_CONF, extra=None):
    """Load the configuration, first reading the default configuration
    and merging it with the given ini file
    """
    default_conf = module_to_dict(DEFAULT_CONF_MODULE)
    conf = Conf(conf_file, default_conf)
    if extra:
        conf.update_from_vars(extra)

    # TODO: check for multiple configuration settings
    global GLOBAL_CONF
    GLOBAL_CONF = conf
    return conf


def module_to_dict(conf_module):
    """Take a module and return a dictionary with all the public
    variables and their values
    """
    m = import_module(conf_module)
    return dict([x for x in getmembers(m) if not x[0].startswith('_')])


def args_to_dict(var_args, current_dict):
    """Take a list of variable settings and construct a dictionary
    [x1.x2:val] -> {'x1': {'x2': val}}
    """
    tmp = dict(current_dict)
    sub = tmp
    for v in var_args:
        key, val = v.split(KEY_VAL_SEP)
        full = key.split('.')
        for k in full[:-1]:
            sub = tmp[k]

        assert full[-1] in sub, "the settings must already contain the variable"
        sub[full[-1]] = val

    return tmp


def dict_to_args(d, prefix=()):
    """Return a list of valid arguments that can be passed, in the form
    [k1.k2:val1, k1.k3:val3, k2.k3:val2]
    """
    for k, v in d.iteritems():
        if isinstance(v, dict):
            for x in dict_to_args(v, prefix + (k,)):
                yield x
        else:
            yield ".".join(prefix + (k,)) + ":" + str(v)
