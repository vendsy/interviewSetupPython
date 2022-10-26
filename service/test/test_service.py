
from service.svc import ServiceFactory

FACTORY = ServiceFactory.create_factory({})
USER_SERVICE = FACTORY.create_service()

def test_add_user():

    USER_SERVICE.configure({})

