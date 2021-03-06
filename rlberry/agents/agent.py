from abc import ABC, abstractmethod
from copy import deepcopy
import logging
from inspect import signature

from rlberry.seeding import seeding


logger = logging.getLogger(__name__)


class Agent(ABC):
    """ Basic interface for agents.

    Parameters
    ----------
    env : Model
        Environment used to fit the agent.
    copy_env : bool
        If true, makes a deep copy of the environment.
    reseed_env : bool
        If true, reseeds the environment.


    .. note::
        Classes that implement this interface should send ``**kwargs`` to :code:`Agent.__init__()`


    Attributes
    ----------
    name : string
        Agent identifier
    env : Model
        Environment on which to train the agent.
    writer : object, default: None
        Writer object (e.g. tensorboard SummaryWriter).
    """

    name = ""

    def __init__(self,
                 env,
                 copy_env=True,
                 reseed_env=True,
                 **kwargs):
        # Check if wrong parameters have been sent to an agent.
        assert kwargs == {}, \
            'Unknown parameters sent to agent:' + str(kwargs.keys())

        self.env = env

        if copy_env:
            try:
                self.env = deepcopy(env)
            except Exception as ex:
                logger.warning("[Agent] Not possible to deepcopy env: " + str(ex))

        if reseed_env:
            reseeded = seeding.safe_reseed(self.env)
            if not reseeded:
                logger.warning("[Agent] Not possible to reseed env, seed() and reseed() are not available.")

        self.writer = None

    @abstractmethod
    def fit(self, **kwargs):
        """Train the agent using the provided environment.

        Returns
        -------
        info: dict
            Dictionary with useful info.
        """
        pass

    @abstractmethod
    def policy(self, observation, **kwargs):
        """Returns an action, given an observation."""
        pass

    def reset(self, **kwargs):
        """Put the agent in default setup."""
        pass

    def save(self, filename, **kwargs):
        """Save agent object."""
        raise NotImplementedError("agent.save() not implemented.")

    def load(self, filename, **kwargs):
        """Load agent object."""
        raise NotImplementedError("agent.load() not implemented.")

    def set_writer(self, writer):
        self.writer = writer

        if self.writer:
            init_args = signature(self.__init__).parameters
            kwargs = [f"| {key} | {getattr(self, key, None)} |" for key in init_args]
            writer.add_text(
                "Hyperparameters",
                "| Parameter | Value |\n|-------|-------|\n" + "\n".join(kwargs),
            )

    @classmethod
    def sample_parameters(cls, trial):
        """
        Sample hyperparameters for hyperparam optimization using
        Optuna (https://optuna.org/)

        Note: only the kwargs sent to __init__ are optimized. Make sure to
        include in the Agent constructor all "optimizable" parameters.

        Parameters
        ----------
        trial: optuna.trial
        """
        raise NotImplementedError("agent.sample_parameters() not implemented.")
