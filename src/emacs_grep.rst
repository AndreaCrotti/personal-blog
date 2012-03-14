emacs_grep
==========

.. TODO: find out what is the precise syntax for the sources

In this post I will try to explain a simple elisp function, to see how little we need to create something already very useful with Emacs.

This function 


.. parsed-literal::

    (defun ca-find-ocaml-declaration (&optional value)
      "Show the ocaml declarations for the given function"
      (interactive)
      (let*
          ((to_lookup
            (or value (read-from-minibuffer "symbol:" (thing-at-point 'symbol))))
           (grep_cmd
            (format "grep -nH -e \"val %s\" %s/*.mli" to_lookup typerex-library-path)))
    
        (grep grep_cmd)))

