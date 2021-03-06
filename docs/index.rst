.. rlberry documentation master file, created by
   sphinx-quickstart on Sat Jan 16 00:20:04 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. image:: ../assets/logo_wide.svg
    :width: 50%
    :alt: rlberry logo

.. _rlberry: https://github.com/rlberry-py/rlberry


An RL Library for Research and Education
========================================

.. image:: https://api.codacy.com/project/badge/Grade/27e91674d18a4ac49edf91c339af1502
    :alt: codacy

.. image:: https://codecov.io/gh/rlberry-py/rlberry/branch/main/graph/badge.svg?token=TIFP7RUD75
    :alt: codecov

.. image:: https://img.shields.io/pypi/pyversions/rlberry
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/pypi/status/rlberry
    :alt: PyPI - Status

.. image:: https://github.com/rlberry-py/rlberry/workflows/test/badge.svg
    :alt: tests

**Writing reinforcement learning algorithms is fun!** *But after the fun, we have
lots of boring things to implement*: run our agents in parallel, average and plot results, 
optimize hyperparameters, compare to baselines, create tricky environments etc etc!

rlberry_ **is here to make your life easier** by doing all these things with a few lines of code,
so that you can spend most of your time developing agents!


In **a few minutes of reading**, you will learn how to:

- :ref:`Install rlberry <installation>`;
- :ref:`Create an agent <create_agent>`;
- :ref:`Evaluate an agent and optimize its hyperparameters <evaluate_agent>`;
- :ref:`Compare different agents <compare_agents>`;
- :ref:`Setup and run experiments using yaml config files <experiment_setup>`.

In addition, rlberry_: 

* Provides **implementations of several RL agents** for you to use as a starting point or as baselines;
* Provides a set of **benchmark environments**, very useful to debug and challenge your algorithms;
* Handles all random seeds for you, ensuring **reproducibility** of your results;
* Is **fully compatible with** several commonly used RL libraries like `OpenAI gym <https://gym.openai.com/>`_ and `Stable Baselines <https://stable-baselines.readthedocs.io/en/master/>`_.


Compatibility with External Libraries
=====================================

We provide examples to show you how to use rlberry_ with:

- :ref:`OpenAI Gym <gym>`;
- :ref:`Stable Baselines <stable_baselines>`.


Seeding & Reproducibility
==========================

In rlberry_, only one global seed is defined, and all the random number generators used
in the library inherit from this seed, ensuring reproducibility and 
independence between the generators 
(see `NumPy SeedSequence <https://numpy.org/doc/stable/reference/random/parallel.html>`_).

It works as follows:


.. code-block:: python

   import rlberry.seeding as seeding

   seeding.set_global_seed(seed=123)

   # From now on, no more seeds are defined by the user, and all the results are reproducible.
   ...

   # If you need a random number generator (rng), call:
   rng = seeding.get_rng()   

   # which gives a numpy Generator (https://numpy.org/doc/stable/reference/random/generator.html) 
   # that is independent of all the previous generators created by seeding.get_rng()
   rng.integers(5)
   rng.normal()
   # etc


.. note:: 

   The :meth:`optimize_hyperparams` method of 
   :class:`~rlberry.stats.agent_stats.AgentStats` uses the `Optuna <https://optuna.org/>`_ 
   library for hyperparameter optimization and is **inherently non-deterministic**
   (see `Optuna FAQ <https://optuna.readthedocs.io/en/stable/faq.html#how-can-i-obtain-reproducible-optimization-results>`_).
   After using this method and fixing the hyperparameter, you can obtain deterministic 
   ouputs with rlberry_ by calling :func:`set_global_seed` available in :mod:`rlberry.seeding`.


Citing rlberry_
===============

If you use rlberry in scientific publications, we would appreciate citations using the following Bibtex entry:

.. code-block:: bibtex

   @misc{rlberry,
   author = {Domingues, Omar Darwiche and ‪Flet-Berliac, Yannis and Leurent, Edouard and M{\'e}nard, Pierre and Shang, Xuedong and Valko, Michal},
   title = {{rlberry - A Reinforcement Learning Library for Research and Education}},
   year = {2021},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/rlberry-py/rlberry}},
   }


Documentation Contents
======================

.. toctree::
  :maxdepth: 2

  installation
  quickstart
  external
  source/modules


Indices and Tables
==================

* :ref:`modindex`
* :ref:`search`
