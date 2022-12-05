from apps.jokes.enums import TypeJokeEnum
from apps.jokes.provider import ChuckDataProvider, CanDataProvider
import random


class JokeFactory:
    def get_data_provider(self, job_type: str | None):
        if job_type == TypeJokeEnum.Chuck:
            return ChuckDataProvider()
        if job_type == TypeJokeEnum.Dad:
            return CanDataProvider()
        if job_type == TypeJokeEnum.Random or job_type is None:
            providers = [ChuckDataProvider(), CanDataProvider()]
            provider = providers[random.randint(0, len(providers) - 1)]
            return provider
