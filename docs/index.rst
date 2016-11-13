.. trybenchmarks documentation master file, created by
   sphinx-quickstart on Sun Nov 13 15:16:09 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to trybenchmarks's documentation!
=========================================

This is an example of pygal chart:

.. pygal::

   chart = pygal.HorizontalBar(y_label_rotation=-25)
   chart.title = 'Horizontal Bar Chart with Rotated Y Labels'
   chart.x_labels = 'one', 'two', 'three', 'four', 'five'
   chart.add('alpha', [1, 2, 3, 1, 2])
   chart.add('beta', [4, 3, 0, 1, {
            'value': 3,
            #'ci': {
            #    'type': 'continuous',
            #    'sample_size': 4,
            #    'stddev': 0.1,
            #}
        }])

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

