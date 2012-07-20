Configuration magic
###################

:status: draft

I write a lot of utilities and scripts, that needs to be configurable and as smart as possible.

Finally I found a solution which I think is very powerful and simple to implement, which allows me to have:

- a default configuration file in a python module, which contains simply variables.

.. parsed-literal::
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
  
.. parsed-literal::
   python myscript.py -D database.user:newuser

   will override the settings but is not allowed to create new settings (both to simplify the implementation and to avoid simple typos)


All this is done using Python white magic.
