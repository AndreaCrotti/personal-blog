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
   
   [database]
   user = user
   host = dbserver
   port = 1000

   which can extend the default configuration or override some values.

- a way to pass from the command line extra settings, passing for example
  
.. code:: bash

   python myscript.py -D database.user:newuser

Will override the settings but is not allowed to create new settings (both to simplify the implementation and to avoid simple typos)


All this is done using Python white magic.
(use *vars* to read from the variable)


First of all we create a singleton object that will store the configuration.

.. code:: python

    GLOBAL_CONF = None

    def get_conf():
        """Return the global configuration, loading it first if necessary
        """
        if GLOBAL_CONF is None:
            load_conf()
    
        return GLOBAL_CONF


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


.. code:: python

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
