Python regexp
#############

:status: draft

In this article I want to show a quick story on parsing and the beauty
of Python.

.. code:: python

    _REGEX_CONSTRUCTOR = {
        'batchid': int,
        'create_hours': float,
        'date': time_string_to_obj,
        'jobid': int,
        'prior': float,
        'queue': int,
        'pid': int,
    }
    
    # by default the regex return the string, and converts to the right field otherwise
    REGEX_CONSTRUCTOR = defaultdict(lambda: str)
    REGEX_CONSTRUCTOR.update(_REGEX_CONSTRUCTOR)
