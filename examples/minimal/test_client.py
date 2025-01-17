import algokit_utils
import pytest
from algokit_utils.models import AlgoAmount
from algokit_utils.protocols import AlgorandClientProtocol

from examples.minimal.client import MinimalAppFactory


@pytest.fixture
def default_deployer(algorand: AlgorandClientProtocol) -> algokit_utils.Account:
    account = algorand.account.random()
    algorand.account.ensure_funded_from_environment(account, AlgoAmount.from_algo(100))
    return account


@pytest.fixture
def minimal_factory(algorand: AlgorandClientProtocol, default_deployer: algokit_utils.Account) -> MinimalAppFactory:
    return algorand.client.get_typed_app_factory(MinimalAppFactory, default_sender=default_deployer.address)


def test_delete(minimal_factory: MinimalAppFactory) -> None:
    client, _ = minimal_factory.deploy()
    
    client.send.delete_bare()
