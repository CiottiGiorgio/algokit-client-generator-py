# flake8: noqa
# fmt: off
# mypy: disable-error-code="no-any-return, no-untyped-call, misc, type-arg"
# This file was automatically generated by algokit-client-generator.
# DO NOT MODIFY IT BY HAND.
# requires: algokit-utils@^3.0.0

# common
import dataclasses
import typing
# core algosdk
import algosdk
from algosdk.transaction import OnComplete
from algosdk.atomic_transaction_composer import TransactionSigner
from algosdk.source_map import SourceMap
from algosdk.transaction import Transaction
from algosdk.v2client.models import SimulateTraceConfig
# utils
from algokit_utils import applications, models, protocols, transactions, clients
from algokit_utils.applications import abi as applications_abi
from algokit_utils import AlgorandClient as _AlgoKitAlgorandClient

_APP_SPEC_JSON = r"""{"arcs": [], "bareActions": {"call": [], "create": ["NoOp"]}, "methods": [{"actions": {"call": ["NoOp"], "create": []}, "args": [], "name": "method_a_that_uses_struct", "returns": {"type": "(uint64,uint64)", "struct": "SomeStruct"}, "events": []}, {"actions": {"call": ["NoOp"], "create": []}, "args": [], "name": "method_b_that_uses_same_struct", "returns": {"type": "(uint64,uint64)", "struct": "SomeStruct"}, "events": []}], "name": "DuplicateStructsContract", "state": {"keys": {"box": {}, "global": {}, "local": {}}, "maps": {"box": {}, "global": {}, "local": {}}, "schema": {"global": {"bytes": 0, "ints": 0}, "local": {"bytes": 0, "ints": 0}}}, "structs": {"SomeStruct": [{"name": "a", "type": "uint64"}, {"name": "b", "type": "uint64"}]}, "desc": "\n        This contract is to be used as a test artifact to verify behavior around struct generation to ensure that \n        the scenarios similar to whats outlined in this contract can not result in a typed client with duplicate struct \n        definitions.\n    ", "source": {"approval": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuZGVsZWdhdG9yX2NvbnRyYWN0LmNvbnRyYWN0LkR1cGxpY2F0ZVN0cnVjdHNDb250cmFjdC5hcHByb3ZhbF9wcm9ncmFtOgogICAgLy8gY29udHJhY3QucHk6MTIKICAgIC8vIGNsYXNzIER1cGxpY2F0ZVN0cnVjdHNDb250cmFjdChBUkM0Q29udHJhY3QpOgogICAgdHhuIE51bUFwcEFyZ3MKICAgIGJ6IG1haW5fYmFyZV9yb3V0aW5nQDYKICAgIG1ldGhvZCAibWV0aG9kX2FfdGhhdF91c2VzX3N0cnVjdCgpKHVpbnQ2NCx1aW50NjQpIgogICAgbWV0aG9kICJtZXRob2RfYl90aGF0X3VzZXNfc2FtZV9zdHJ1Y3QoKSh1aW50NjQsdWludDY0KSIKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDAKICAgIG1hdGNoIG1haW5fbWV0aG9kX2FfdGhhdF91c2VzX3N0cnVjdF9yb3V0ZUAyIG1haW5fbWV0aG9kX2JfdGhhdF91c2VzX3NhbWVfc3RydWN0X3JvdXRlQDMKICAgIGVyciAvLyByZWplY3QgdHJhbnNhY3Rpb24KCm1haW5fbWV0aG9kX2FfdGhhdF91c2VzX3N0cnVjdF9yb3V0ZUAyOgogICAgLy8gY29udHJhY3QucHk6MTkKICAgIC8vIEBhcmM0LmFiaW1ldGhvZCgpCiAgICB0eG4gT25Db21wbGV0aW9uCiAgICAhCiAgICBhc3NlcnQgLy8gT25Db21wbGV0aW9uIGlzIE5vT3AKICAgIHR4biBBcHBsaWNhdGlvbklECiAgICBhc3NlcnQgLy8gaXMgbm90IGNyZWF0aW5nCiAgICBjYWxsc3ViIG1ldGhvZF9hX3RoYXRfdXNlc19zdHJ1Y3QKICAgIGJ5dGUgMHgxNTFmN2M3NQogICAgc3dhcAogICAgY29uY2F0CiAgICBsb2cKICAgIGludCAxCiAgICByZXR1cm4KCm1haW5fbWV0aG9kX2JfdGhhdF91c2VzX3NhbWVfc3RydWN0X3JvdXRlQDM6CiAgICAvLyBjb250cmFjdC5weToyNgogICAgLy8gQGFyYzQuYWJpbWV0aG9kKCkKICAgIHR4biBPbkNvbXBsZXRpb24KICAgICEKICAgIGFzc2VydCAvLyBPbkNvbXBsZXRpb24gaXMgTm9PcAogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgIGFzc2VydCAvLyBpcyBub3QgY3JlYXRpbmcKICAgIGNhbGxzdWIgbWV0aG9kX2JfdGhhdF91c2VzX3NhbWVfc3RydWN0CiAgICBieXRlIDB4MTUxZjdjNzUKICAgIHN3YXAKICAgIGNvbmNhdAogICAgbG9nCiAgICBpbnQgMQogICAgcmV0dXJuCgptYWluX2JhcmVfcm91dGluZ0A2OgogICAgLy8gY29udHJhY3QucHk6MTIKICAgIC8vIGNsYXNzIER1cGxpY2F0ZVN0cnVjdHNDb250cmFjdChBUkM0Q29udHJhY3QpOgogICAgdHhuIE9uQ29tcGxldGlvbgogICAgIQogICAgYXNzZXJ0IC8vIHJlamVjdCB0cmFuc2FjdGlvbgogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgICEKICAgIGFzc2VydCAvLyBpcyBjcmVhdGluZwogICAgaW50IDEKICAgIHJldHVybgoKCi8vIHNtYXJ0X2NvbnRyYWN0cy5kZWxlZ2F0b3JfY29udHJhY3QuY29udHJhY3QuRHVwbGljYXRlU3RydWN0c0NvbnRyYWN0Lm1ldGhvZF9hX3RoYXRfdXNlc19zdHJ1Y3QoKSAtPiBieXRlczoKbWV0aG9kX2FfdGhhdF91c2VzX3N0cnVjdDoKICAgIC8vIGNvbnRyYWN0LnB5OjE5LTIwCiAgICAvLyBAYXJjNC5hYmltZXRob2QoKQogICAgLy8gZGVmIG1ldGhvZF9hX3RoYXRfdXNlc19zdHJ1Y3Qoc2VsZikgLT4gU29tZVN0cnVjdDoKICAgIHByb3RvIDAgMQogICAgLy8gY29udHJhY3QucHk6MjEtMjQKICAgIC8vIHJldHVybiBTb21lU3RydWN0KAogICAgLy8gICAgIGFyYzQuVUludDY0KDEpLAogICAgLy8gICAgIGFyYzQuVUludDY0KDIpLAogICAgLy8gKQogICAgYnl0ZSAweDAwMDAwMDAwMDAwMDAwMDEwMDAwMDAwMDAwMDAwMDAyCiAgICByZXRzdWIKCgovLyBzbWFydF9jb250cmFjdHMuZGVsZWdhdG9yX2NvbnRyYWN0LmNvbnRyYWN0LkR1cGxpY2F0ZVN0cnVjdHNDb250cmFjdC5tZXRob2RfYl90aGF0X3VzZXNfc2FtZV9zdHJ1Y3QoKSAtPiBieXRlczoKbWV0aG9kX2JfdGhhdF91c2VzX3NhbWVfc3RydWN0OgogICAgLy8gY29udHJhY3QucHk6MjYtMjcKICAgIC8vIEBhcmM0LmFiaW1ldGhvZCgpCiAgICAvLyBkZWYgbWV0aG9kX2JfdGhhdF91c2VzX3NhbWVfc3RydWN0KHNlbGYpIC0+IFNvbWVTdHJ1Y3Q6CiAgICBwcm90byAwIDEKICAgIC8vIGNvbnRyYWN0LnB5OjI4LTMxCiAgICAvLyByZXR1cm4gU29tZVN0cnVjdCgKICAgIC8vICAgICBhcmM0LlVJbnQ2NCgzKSwKICAgIC8vICAgICBhcmM0LlVJbnQ2NCg0KSwKICAgIC8vICkKICAgIGJ5dGUgMHgwMDAwMDAwMDAwMDAwMDAzMDAwMDAwMDAwMDAwMDAwNAogICAgcmV0c3ViCg==", "clear": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuZGVsZWdhdG9yX2NvbnRyYWN0LmNvbnRyYWN0LkR1cGxpY2F0ZVN0cnVjdHNDb250cmFjdC5jbGVhcl9zdGF0ZV9wcm9ncmFtOgogICAgLy8gY29udHJhY3QucHk6MTIKICAgIC8vIGNsYXNzIER1cGxpY2F0ZVN0cnVjdHNDb250cmFjdChBUkM0Q29udHJhY3QpOgogICAgaW50IDEKICAgIHJldHVybgo="}}"""
APP_SPEC = applications.Arc56Contract.from_json(_APP_SPEC_JSON)

def _parse_abi_args(args: typing.Any | None = None) -> list[typing.Any] | None:
    """Helper to parse ABI args into the format expected by underlying client"""
    if args is None:
        return None

    def convert_dataclass(value: typing.Any) -> typing.Any:
        if dataclasses.is_dataclass(value):
            return tuple(convert_dataclass(getattr(value, field.name)) for field in dataclasses.fields(value))
        elif isinstance(value, (list, tuple)):
            return type(value)(convert_dataclass(item) for item in value)
        return value

    match args:
        case tuple():
            method_args = list(args)
        case _ if dataclasses.is_dataclass(args):
            method_args = [getattr(args, field.name) for field in dataclasses.fields(args)]
        case _:
            raise ValueError("Invalid 'args' type. Expected 'tuple' or 'TypedDict' for respective typed arguments.")

    return [
        convert_dataclass(arg) if not isinstance(arg, transactions.AppMethodCallTransactionArgument) else arg
        for arg in method_args
    ] if method_args else None

ON_COMPLETE_TYPES = typing.Literal[
    OnComplete.NoOpOC,
    OnComplete.UpdateApplicationOC,
    OnComplete.DeleteApplicationOC,
    OnComplete.OptInOC,
    OnComplete.CloseOutOC,
]


@dataclasses.dataclass(frozen=True)
class SomeStruct:
    """Struct for SomeStruct"""
    a: int
    b: int


@dataclasses.dataclass(frozen=True, kw_only=True)
class CommonAppCallParams:
    """Common configuration for app call transaction parameters

    :ivar account_references: List of account addresses to reference
    :ivar app_references: List of app IDs to reference
    :ivar asset_references: List of asset IDs to reference
    :ivar box_references: List of box references to include
    :ivar extra_fee: Additional fee to add to transaction
    :ivar lease: Transaction lease value
    :ivar max_fee: Maximum fee allowed for transaction
    :ivar note: Arbitrary note for the transaction
    :ivar rekey_to: Address to rekey account to
    :ivar sender: Sender address override
    :ivar signer: Custom transaction signer
    :ivar static_fee: Fixed fee for transaction
    :ivar validity_window: Number of rounds valid
    :ivar first_valid_round: First valid round number
    :ivar last_valid_round: Last valid round number"""

    account_references: list[str] | None = None
    app_references: list[int] | None = None
    asset_references: list[int] | None = None
    box_references: list[models.BoxReference | models.BoxIdentifier] | None = None
    extra_fee: models.AlgoAmount | None = None
    lease: bytes | None = None
    max_fee: models.AlgoAmount | None = None
    note: bytes | None = None
    rekey_to: str | None = None
    sender: str | None = None
    signer: TransactionSigner | None = None
    static_fee: models.AlgoAmount | None = None
    validity_window: int | None = None
    first_valid_round: int | None = None
    last_valid_round: int | None = None

@dataclasses.dataclass(frozen=True, kw_only=True)
class CommonAppFactoryCallParams(CommonAppCallParams):
    """Common configuration for app factory call related transaction parameters"""
    on_complete: ON_COMPLETE_TYPES | None = None


class DuplicateStructsContractParams:
    def __init__(self, app_client: applications.AppClient):
        self.app_client = app_client

    def method_a_that_uses_struct(
        self,
        common_params: CommonAppCallParams | None = None
    ) -> transactions.AppCallMethodCallParams:
    
        common_params = common_params or CommonAppCallParams()
        return self.app_client.params.call(applications.AppClientMethodCallParams(**{
            **dataclasses.asdict(common_params),
            "method": "method_a_that_uses_struct()(uint64,uint64)",
        }))

    def method_b_that_uses_same_struct(
        self,
        common_params: CommonAppCallParams | None = None
    ) -> transactions.AppCallMethodCallParams:
    
        common_params = common_params or CommonAppCallParams()
        return self.app_client.params.call(applications.AppClientMethodCallParams(**{
            **dataclasses.asdict(common_params),
            "method": "method_b_that_uses_same_struct()(uint64,uint64)",
        }))

    def clear_state(
        self,
        params: applications.AppClientBareCallParams | None = None,
        
    ) -> transactions.AppCallParams:
        return self.app_client.params.bare.clear_state(
            params,
            
        )


class DuplicateStructsContractCreateTransactionParams:
    def __init__(self, app_client: applications.AppClient):
        self.app_client = app_client

    def method_a_that_uses_struct(
        self,
        common_params: CommonAppCallParams | None = None
    ) -> transactions.BuiltTransactions:
    
        common_params = common_params or CommonAppCallParams()
        return self.app_client.create_transaction.call(applications.AppClientMethodCallParams(**{
            **dataclasses.asdict(common_params),
            "method": "method_a_that_uses_struct()(uint64,uint64)",
        }))

    def method_b_that_uses_same_struct(
        self,
        common_params: CommonAppCallParams | None = None
    ) -> transactions.BuiltTransactions:
    
        common_params = common_params or CommonAppCallParams()
        return self.app_client.create_transaction.call(applications.AppClientMethodCallParams(**{
            **dataclasses.asdict(common_params),
            "method": "method_b_that_uses_same_struct()(uint64,uint64)",
        }))

    def clear_state(
        self,
        params: applications.AppClientBareCallParams | None = None,
        
    ) -> Transaction:
        return self.app_client.create_transaction.bare.clear_state(
            params,
            
        )


class DuplicateStructsContractSend:
    def __init__(self, app_client: applications.AppClient):
        self.app_client = app_client

    def method_a_that_uses_struct(
        self,
        common_params: CommonAppCallParams | None = None,
        send_params: models.SendParams | None = None
    ) -> transactions.SendAppTransactionResult[SomeStruct]:
    
        common_params = common_params or CommonAppCallParams()
        response = self.app_client.send.call(applications.AppClientMethodCallParams(**{
            **dataclasses.asdict(common_params),
            "method": "method_a_that_uses_struct()(uint64,uint64)",
        }), send_params=send_params)
        parsed_response = dataclasses.replace(response, abi_return=SomeStruct(**typing.cast(dict, response.abi_return))) # type: ignore
        return typing.cast(transactions.SendAppTransactionResult[SomeStruct], parsed_response)

    def method_b_that_uses_same_struct(
        self,
        common_params: CommonAppCallParams | None = None,
        send_params: models.SendParams | None = None
    ) -> transactions.SendAppTransactionResult[SomeStruct]:
    
        common_params = common_params or CommonAppCallParams()
        response = self.app_client.send.call(applications.AppClientMethodCallParams(**{
            **dataclasses.asdict(common_params),
            "method": "method_b_that_uses_same_struct()(uint64,uint64)",
        }), send_params=send_params)
        parsed_response = dataclasses.replace(response, abi_return=SomeStruct(**typing.cast(dict, response.abi_return))) # type: ignore
        return typing.cast(transactions.SendAppTransactionResult[SomeStruct], parsed_response)

    def clear_state(
        self,
        params: applications.AppClientBareCallParams | None = None,
        send_params: models.SendParams | None = None
    ) -> transactions.SendAppTransactionResult[applications_abi.ABIReturn]:
        return self.app_client.send.bare.clear_state(
            params,
            send_params=send_params,
        )


class DuplicateStructsContractState:
    """Methods to access state for the current DuplicateStructsContract app"""

    def __init__(self, app_client: applications.AppClient):
        self.app_client = app_client

class DuplicateStructsContractClient:
    """Client for interacting with DuplicateStructsContract smart contract"""

    @typing.overload
    def __init__(self, app_client: applications.AppClient) -> None: ...
    
    @typing.overload
    def __init__(
        self,
        *,
        algorand: _AlgoKitAlgorandClient,
        app_id: int,
        app_name: str | None = None,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> None: ...

    def __init__(
        self,
        app_client: applications.AppClient | None = None,
        *,
        algorand: _AlgoKitAlgorandClient | None = None,
        app_id: int | None = None,
        app_name: str | None = None,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> None:
        if app_client:
            self.app_client = app_client
        elif algorand and app_id:
            self.app_client = applications.AppClient(
                applications.AppClientParams(
                    algorand=algorand,
                    app_spec=APP_SPEC,
                    app_id=app_id,
                    app_name=app_name,
                    default_sender=default_sender,
                    default_signer=default_signer,
                    approval_source_map=approval_source_map,
                    clear_source_map=clear_source_map,
                )
            )
        else:
            raise ValueError("Either app_client or algorand and app_id must be provided")
    
        self.params = DuplicateStructsContractParams(self.app_client)
        self.create_transaction = DuplicateStructsContractCreateTransactionParams(self.app_client)
        self.send = DuplicateStructsContractSend(self.app_client)
        self.state = DuplicateStructsContractState(self.app_client)

    @staticmethod
    def from_creator_and_name(
        creator_address: str,
        app_name: str,
        algorand: _AlgoKitAlgorandClient,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
        ignore_cache: bool | None = None,
        app_lookup_cache: applications.AppLookup | None = None,
    ) -> "DuplicateStructsContractClient":
        return DuplicateStructsContractClient(
            applications.AppClient.from_creator_and_name(
                creator_address=creator_address,
                app_name=app_name,
                app_spec=APP_SPEC,
                algorand=algorand,
                default_sender=default_sender,
                default_signer=default_signer,
                approval_source_map=approval_source_map,
                clear_source_map=clear_source_map,
                ignore_cache=ignore_cache,
                app_lookup_cache=app_lookup_cache,
            )
        )
    
    @staticmethod
    def from_network(
        algorand: _AlgoKitAlgorandClient,
        app_name: str | None = None,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> "DuplicateStructsContractClient":
        return DuplicateStructsContractClient(
            applications.AppClient.from_network(
                app_spec=APP_SPEC,
                algorand=algorand,
                app_name=app_name,
                default_sender=default_sender,
                default_signer=default_signer,
                approval_source_map=approval_source_map,
                clear_source_map=clear_source_map,
            )
        )

    @property
    def app_id(self) -> int:
        return self.app_client.app_id
    
    @property
    def app_address(self) -> str:
        return self.app_client.app_address
    
    @property
    def app_name(self) -> str:
        return self.app_client.app_name
    
    @property
    def app_spec(self) -> applications.Arc56Contract:
        return self.app_client.app_spec
    
    @property
    def algorand(self) -> _AlgoKitAlgorandClient:
        return self.app_client.algorand

    def clone(
        self,
        app_name: str | None = None,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> "DuplicateStructsContractClient":
        return DuplicateStructsContractClient(
            self.app_client.clone(
                app_name=app_name,
                default_sender=default_sender,
                default_signer=default_signer,
                approval_source_map=approval_source_map,
                clear_source_map=clear_source_map,
            )
        )

    def new_group(self) -> "DuplicateStructsContractComposer":
        return DuplicateStructsContractComposer(self)

    @typing.overload
    def decode_return_value(
        self,
        method: typing.Literal["method_a_that_uses_struct()(uint64,uint64)"],
        return_value: applications_abi.ABIReturn | None
    ) -> SomeStruct | None: ...
    @typing.overload
    def decode_return_value(
        self,
        method: typing.Literal["method_b_that_uses_same_struct()(uint64,uint64)"],
        return_value: applications_abi.ABIReturn | None
    ) -> SomeStruct | None: ...
    @typing.overload
    def decode_return_value(
        self,
        method: str,
        return_value: applications_abi.ABIReturn | None
    ) -> applications_abi.ABIValue | applications_abi.ABIStruct | None: ...

    def decode_return_value(
        self,
        method: str,
        return_value: applications_abi.ABIReturn | None
    ) -> applications_abi.ABIValue | applications_abi.ABIStruct | None | SomeStruct:
        """Decode ABI return value for the given method."""
        if return_value is None:
            return None
    
        arc56_method = self.app_spec.get_arc56_method(method)
        decoded = return_value.get_arc56_value(arc56_method, self.app_spec.structs)
    
        # If method returns a struct, convert the dict to appropriate dataclass
        if (arc56_method and
            arc56_method.returns and
            arc56_method.returns.struct and
            isinstance(decoded, dict)):
            struct_class = globals().get(arc56_method.returns.struct)
            if struct_class:
                return struct_class(**typing.cast(dict, decoded))
        return decoded


@dataclasses.dataclass(frozen=True)
class DuplicateStructsContractBareCallCreateParams(applications.AppClientBareCallCreateParams):
    """Parameters for creating DuplicateStructsContract contract with bare calls"""
    on_complete: typing.Literal[OnComplete.NoOpOC] | None = None

    def to_algokit_utils_params(self) -> applications.AppClientBareCallCreateParams:
        return applications.AppClientBareCallCreateParams(**self.__dict__)

class DuplicateStructsContractFactory(protocols.TypedAppFactoryProtocol[DuplicateStructsContractBareCallCreateParams, None, None]):
    """Factory for deploying and managing DuplicateStructsContractClient smart contracts"""

    def __init__(
        self,
        algorand: _AlgoKitAlgorandClient,
        *,
        app_name: str | None = None,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        version: str | None = None,
        updatable: bool | None = None,
        deletable: bool | None = None,
        deploy_time_params: models.TealTemplateParams | None = None,
    ):
        self.app_factory = applications.AppFactory(
            params=applications.AppFactoryParams(
                algorand=algorand,
                app_spec=APP_SPEC,
                app_name=app_name,
                default_sender=default_sender,
                default_signer=default_signer,
                version=version,
                updatable=updatable,
                deletable=deletable,
                deploy_time_params=deploy_time_params,
            )
        )
        self.params = DuplicateStructsContractFactoryParams(self.app_factory)
        self.create_transaction = DuplicateStructsContractFactoryCreateTransaction(self.app_factory)
        self.send = DuplicateStructsContractFactorySend(self.app_factory)

    @property
    def app_name(self) -> str:
        return self.app_factory.app_name
    
    @property
    def app_spec(self) -> applications.Arc56Contract:
        return self.app_factory.app_spec
    
    @property
    def algorand(self) -> _AlgoKitAlgorandClient:
        return self.app_factory.algorand

    def deploy(
        self,
        *,
        deploy_time_params: models.TealTemplateParams | None = None,
        on_update: applications.OnUpdate = applications.OnUpdate.Fail,
        on_schema_break: applications.OnSchemaBreak = applications.OnSchemaBreak.Fail,
        create_params: DuplicateStructsContractBareCallCreateParams | None = None,
        update_params: None = None,
        delete_params: None = None,
        existing_deployments: applications.AppLookup | None = None,
        ignore_cache: bool = False,
        updatable: bool | None = None,
        deletable: bool | None = None,
        app_name: str | None = None,
        max_rounds_to_wait: int | None = None,
        suppress_log: bool = False,
        populate_app_call_resources: bool | None = None,
        cover_app_call_inner_txn_fees: bool | None = None,
    ) -> tuple[DuplicateStructsContractClient, applications.AppFactoryDeployResponse]:
        """Deploy the application"""
        deploy_response = self.app_factory.deploy(
            deploy_time_params=deploy_time_params,
            on_update=on_update,
            on_schema_break=on_schema_break,
            create_params=create_params.to_algokit_utils_params() if create_params else None,
            update_params=update_params,
            delete_params=delete_params,
            existing_deployments=existing_deployments,
            ignore_cache=ignore_cache,
            updatable=updatable,
            deletable=deletable,
            app_name=app_name,
            max_rounds_to_wait=max_rounds_to_wait,
            suppress_log=suppress_log,
            populate_app_call_resources=populate_app_call_resources,
            cover_app_call_inner_txn_fees=cover_app_call_inner_txn_fees,
        )

        return DuplicateStructsContractClient(deploy_response[0]), deploy_response[1]

    def get_app_client_by_creator_and_name(
        self,
        creator_address: str,
        app_name: str,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        ignore_cache: bool | None = None,
        app_lookup_cache: applications.AppLookup | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> DuplicateStructsContractClient:
        """Get an app client by creator address and name"""
        return DuplicateStructsContractClient(
            self.app_factory.get_app_client_by_creator_and_name(
                creator_address,
                app_name,
                default_sender,
                default_signer,
                ignore_cache,
                app_lookup_cache,
                approval_source_map,
                clear_source_map,
            )
        )

    def get_app_client_by_id(
        self,
        app_id: int,
        app_name: str | None = None,
        default_sender: str | bytes | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> DuplicateStructsContractClient:
        """Get an app client by app ID"""
        return DuplicateStructsContractClient(
            self.app_factory.get_app_client_by_id(
                app_id,
                app_name,
                default_sender,
                default_signer,
                approval_source_map,
                clear_source_map,
            )
        )


class DuplicateStructsContractFactoryParams:
    """Parameters for creating transactions for DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory
        self.create = DuplicateStructsContractFactoryCreateParams(app_factory)
        self.update = DuplicateStructsContractFactoryUpdateParams(app_factory)
        self.delete = DuplicateStructsContractFactoryDeleteParams(app_factory)

class DuplicateStructsContractFactoryCreateParams:
    """Parameters for 'create' operations of DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        common_params: CommonAppFactoryCallParams | None = None,
        compilation_params: applications.AppClientCompilationParams | None = None
    ) -> transactions.AppCreateParams:
        """Creates an instance using a bare call"""
        common_params = common_params or CommonAppFactoryCallParams()
        return self.app_factory.params.bare.create(
            applications.AppFactoryCreateParams(**dataclasses.asdict(common_params)),
            compilation_params=compilation_params)

    def method_a_that_uses_struct(
        self,
        *,
        common_params: CommonAppFactoryCallParams | None = None,
        compilation_params: applications.AppClientCompilationParams | None = None
    ) -> transactions.AppCreateMethodCallParams:
        """Creates a new instance using the method_a_that_uses_struct()(uint64,uint64) ABI method"""
        common_params = common_params or CommonAppFactoryCallParams()
        return self.app_factory.params.create(
            applications.AppFactoryCreateMethodCallParams(
                **{
                **dataclasses.asdict(common_params),
                "method": "method_a_that_uses_struct()(uint64,uint64)",
                "args": None,
                }
            ),
            compilation_params=compilation_params
        )

    def method_b_that_uses_same_struct(
        self,
        *,
        common_params: CommonAppFactoryCallParams | None = None,
        compilation_params: applications.AppClientCompilationParams | None = None
    ) -> transactions.AppCreateMethodCallParams:
        """Creates a new instance using the method_b_that_uses_same_struct()(uint64,uint64) ABI method"""
        common_params = common_params or CommonAppFactoryCallParams()
        return self.app_factory.params.create(
            applications.AppFactoryCreateMethodCallParams(
                **{
                **dataclasses.asdict(common_params),
                "method": "method_b_that_uses_same_struct()(uint64,uint64)",
                "args": None,
                }
            ),
            compilation_params=compilation_params
        )

class DuplicateStructsContractFactoryUpdateParams:
    """Parameters for 'update' operations of DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        common_params: CommonAppFactoryCallParams | None = None,
        
    ) -> transactions.AppUpdateParams:
        """Updates an instance using a bare call"""
        common_params = common_params or CommonAppFactoryCallParams()
        return self.app_factory.params.bare.deploy_update(
            applications.AppFactoryCreateParams(**dataclasses.asdict(common_params)),
            )

class DuplicateStructsContractFactoryDeleteParams:
    """Parameters for 'delete' operations of DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        common_params: CommonAppFactoryCallParams | None = None,
        
    ) -> transactions.AppDeleteParams:
        """Deletes an instance using a bare call"""
        common_params = common_params or CommonAppFactoryCallParams()
        return self.app_factory.params.bare.deploy_delete(
            applications.AppFactoryCreateParams(**dataclasses.asdict(common_params)),
            )


class DuplicateStructsContractFactoryCreateTransaction:
    """Create transactions for DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory
        self.create = DuplicateStructsContractFactoryCreateTransactionCreate(app_factory)


class DuplicateStructsContractFactoryCreateTransactionCreate:
    """Create new instances of DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        common_params: CommonAppFactoryCallParams | None = None,
    ) -> Transaction:
        """Creates a new instance using a bare call"""
        common_params = common_params or CommonAppFactoryCallParams()
        return self.app_factory.create_transaction.bare.create(
            applications.AppFactoryCreateParams(**dataclasses.asdict(common_params)),
        )


class DuplicateStructsContractFactorySend:
    """Send calls to DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory
        self.create = DuplicateStructsContractFactorySendCreate(app_factory)


class DuplicateStructsContractFactorySendCreate:
    """Send create calls to DuplicateStructsContract contract"""

    def __init__(self, app_factory: applications.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        common_params: CommonAppFactoryCallParams | None = None,
        send_params: models.SendParams | None = None,
        compilation_params: applications.AppClientCompilationParams | None = None,
    ) -> tuple[DuplicateStructsContractClient, transactions.SendAppCreateTransactionResult]:
        """Creates a new instance using a bare call"""
        common_params = common_params or CommonAppFactoryCallParams()
        result = self.app_factory.send.bare.create(
            applications.AppFactoryCreateParams(**dataclasses.asdict(common_params)),
            send_params=send_params,
            compilation_params=compilation_params
        )
        return DuplicateStructsContractClient(result[0]), result[1]


class DuplicateStructsContractComposer:
    """Composer for creating transaction groups for DuplicateStructsContract contract calls"""

    def __init__(self, client: "DuplicateStructsContractClient"):
        self.client = client
        self._composer = client.algorand.new_group()
        self._result_mappers: list[typing.Callable[[applications_abi.ABIReturn | None], typing.Any] | None] = []

    def method_a_that_uses_struct(
        self,
        common_params: CommonAppCallParams | None = None
    ) -> "DuplicateStructsContractComposer":
        self._composer.add_app_call_method_call(
            self.client.params.method_a_that_uses_struct(
                
                common_params=common_params,
            )
        )
        self._result_mappers.append(
            lambda v: self.client.decode_return_value(
                "method_a_that_uses_struct()(uint64,uint64)", v
            )
        )
        return self

    def method_b_that_uses_same_struct(
        self,
        common_params: CommonAppCallParams | None = None
    ) -> "DuplicateStructsContractComposer":
        self._composer.add_app_call_method_call(
            self.client.params.method_b_that_uses_same_struct(
                
                common_params=common_params,
            )
        )
        self._result_mappers.append(
            lambda v: self.client.decode_return_value(
                "method_b_that_uses_same_struct()(uint64,uint64)", v
            )
        )
        return self

    def clear_state(
        self,
        *,
        args: list[bytes] | None = None,
        common_params: CommonAppCallParams | None = None,
    ) -> "DuplicateStructsContractComposer":
        common_params=common_params or CommonAppCallParams()
        self._composer.add_app_call(
            self.client.params.clear_state(
                applications.AppClientBareCallParams(
                    **{
                        **dataclasses.asdict(common_params),
                        "args": args
                    }
                )
            )
        )
        return self
    
    def add_transaction(
        self, txn: Transaction, signer: TransactionSigner | None = None
    ) -> "DuplicateStructsContractComposer":
        self._composer.add_transaction(txn, signer)
        return self
    
    def composer(self) -> transactions.TransactionComposer:
        return self._composer
    
    def simulate(
        self,
        allow_more_logs: bool | None = None,
        allow_empty_signatures: bool | None = None,
        allow_unnamed_resources: bool | None = None,
        extra_opcode_budget: int | None = None,
        exec_trace_config: SimulateTraceConfig | None = None,
        simulation_round: int | None = None,
        skip_signatures: bool | None = None,
    ) -> transactions.SendAtomicTransactionComposerResults:
        return self._composer.simulate(
            allow_more_logs=allow_more_logs,
            allow_empty_signatures=allow_empty_signatures,
            allow_unnamed_resources=allow_unnamed_resources,
            extra_opcode_budget=extra_opcode_budget,
            exec_trace_config=exec_trace_config,
            simulation_round=simulation_round,
            skip_signatures=skip_signatures,
        )
    
    def send(
        self,
        send_params: models.SendParams | None = None
    ) -> transactions.SendAtomicTransactionComposerResults:
        return self._composer.send(send_params)
