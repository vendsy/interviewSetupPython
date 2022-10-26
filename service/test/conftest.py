import pytest

from service.svc import ServiceFactory
from service.svc import MyServiceFactory

factory = ServiceFactory.create_factory({})


@pytest.fixture(scope="session")
def create_service():
    return factory.create_service()
