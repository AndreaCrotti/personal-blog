Configuration magic
###################

I write a lot of utilities and scripts, that needs to be configurable and as smart as possible.

Finally I found a solution which I think is very powerful and simple to implement, which allows me to have:

- a default configuration file in a python module, which contains simply variables.

.. code:: python

   database = {
       'user': 'user',
       'host': 'dbserver',
       'port': 1000,
   }

- a simple ini file, for example:
   
.. code:: ini

   [database]
   user = user
   host = dbserver
   port = 1000


Which can extend the default configuration or override some values.

- a way to pass from the command line extra settings, passing for example
  
.. code:: bash

   python myscript.py -D database.user:newuser

Will override the settings but is not allowed to create new settings (both to simplify the implementation and to avoid simple typos).


All this is very simple and can be implemented with some Python white magic.

The final parsed configuration is just a dictionary and can is loaded only once, and accessed from every module via *get_conf*.

.. code:: python

    GLOBAL_CONF = None

    def get_conf():
        """Return the global configuration, loading it first if necessary
        """
        if GLOBAL_CONF is None:
            global GLOBAL_CONF
            GLOBAL_CONF = load_conf()
    
        return GLOBAL_CONF


And the load_conf function is very simple, it takes an optional ini file path and a dictionary with extra settings, and

- parses the default python configuration to dictionary
- creates a configuration object passing these default values
- updates the configuration with the extra settings


.. code:: python

    def load_conf(conf_file=DEFAULT_INI_CONF, extra=None):
        default_conf = module_to_dict(DEFAULT_CONF_MODULE)
        conf = Conf(conf_file, default_conf)
        if extra:
            conf.update_from_vars(extra)

        return conf


The configuration object does

- set the internal dictionary to the default values.
- create a ConfigParser object to parse the given ini file.
- iterates over the ConfigParser object writing on the internal dictionary with *_conf_to_dict*. In this implementation a configuration file is allowed to create sections and options which didn't exist, this might be made easily configurable. (For example suppose we want to enable type checking it would make sense to only allow options that are also in the global Python configuration.)

.. code:: python

    class Conf:
        def __init__(self, conf_file, default=None):
            self.conf_dict = default or {}
            self.conf = ConfigParser()
            self.conf.read(conf_file)
            self._conf_to_dict()
    
        def _conf_to_dict(self):
            for sec in self.conf.sections():
                if sec not in self.conf_dict:
                    self.conf_dict[sec] = {}
    
                for k, v in self.conf.items(sec):
                    self.conf_dict[sec][k] = v
    

These two methods are just added for convenience, so that the configuration can be accessed in the same way as a dictionary and as a namespace:

.. code:: python

        def __getitem__(self, item):
            return self.conf_dict[item]
    
        def __getattr__(self, attr):
            return self.__getitem__(attr)


These two methods instead are used to convert the configuration to and from a list of arguments, very useful to be able to override settings from the command line.

    
.. code:: python

        def to_args(self):
            return list(dict_to_args(self.conf_dict))
    
        def update_from_vars(self, varargs):
            tmp_dic = args_to_dict(varargs, self.conf_dict)
            self.conf_dict.update(tmp_dic)
    


.. code:: python
    
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


.. code:: python

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

