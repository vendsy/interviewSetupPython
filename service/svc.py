from abc import ABC, abstractmethod
from typing import Mapping, Any

class MyService:
    def configure(self, config: Mapping) -> None:
        print("This test is working")
        return

class MyServiceFactory:

    def create_service(self) -> MyService:
        svc: MyService = MyService()
        return svc

class ServiceFactory(ABC):

    @staticmethod
    def create_factory(config: Mapping[str, Any]) -> MyServiceFactory:
        factory: MyServiceFactory = MyServiceFactory()
        return factory





