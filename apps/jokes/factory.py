from apps.jokes.enums import TypeJokeEnum
from apps.jokes.provider import ChuckDataProvider, CanDataProvider
import random

"""
Factory class for joke provider
"""


class JokeFactory:

    def get_data_provider(self, job_type: str | None):
        """
        If the job_type is Chuck, return a ChuckDataProvider. If the job_type is Dad, return a CanDataProvider. If the
        job_type is None, return a random provider

        :param job_type: The type of joke to be returned
        :type job_type: str | None
        :return: A data provider
        """
        if job_type == TypeJokeEnum.Chuck:
            return ChuckDataProvider()
        if job_type == TypeJokeEnum.Dad:
            return CanDataProvider()
        if job_type is None:
            providers = [ChuckDataProvider(), CanDataProvider()]
            provider = providers[random.randint(0, len(providers) - 1)]
            return provider
