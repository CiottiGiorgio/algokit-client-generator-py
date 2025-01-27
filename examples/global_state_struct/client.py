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
import algokit_utils
from algokit_utils import AlgorandClient as _AlgoKitAlgorandClient

_APP_SPEC_JSON = r"""{"arcs": [22, 28], "bareActions": {"call": [], "create": ["NoOp"]}, "methods": [{"actions": {"call": ["NoOp"], "create": []}, "args": [{"type": "string", "name": "name"}], "name": "hello", "returns": {"type": "string"}, "events": [], "readonly": false, "recommendations": {}}], "name": "HelloWorld", "state": {"keys": {"box": {}, "global": {"my_struct": {"key": "bXlfc3RydWN0", "keyType": "AVMString", "valueType": "Vector"}}, "local": {}}, "maps": {"box": {}, "global": {}, "local": {}}, "schema": {"global": {"bytes": 1, "ints": 0}, "local": {"bytes": 0, "ints": 0}}}, "structs": {"Vector": [{"name": "x", "type": "string"}, {"name": "y", "type": "string"}]}, "byteCode": {"approval": "CjEYQAAYggIJbXlfc3RydWN0CgAEAAcAATEAATJnMRtBADSABAK+zhE2GgCOAQADgQBDMRkURDEYRDYaAVcCAIgAIEkVFlcGAkxQgAQVH3x1TFCwgQFDMRlA/9QxGBREgQFDigEBgAdIZWxsbywgi/9QiQ==", "clear": "CoEBQw=="}, "compilerInfo": {"compiler": "puya", "compilerVersion": {"major": 4, "minor": 2, "patch": 0}}, "events": [], "networks": {}, "source": {"approval": "I3ByYWdtYSB2ZXJzaW9uIDEwCiNwcmFnbWEgdHlwZXRyYWNrIGZhbHNlCgovLyBzbWFydF9jb250cmFjdHMuaGVsbG9fd29ybGQuY29udHJhY3QuSGVsbG9Xb3JsZC5fX2FsZ29weV9lbnRyeXBvaW50X3dpdGhfaW5pdCgpIC0+IHVpbnQ2NDoKbWFpbjoKICAgIHR4biBBcHBsaWNhdGlvbklECiAgICBibnogbWFpbl9hZnRlcl9pZl9lbHNlQDIKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9oZWxsb193b3JsZC9jb250cmFjdC5weToxMwogICAgLy8gc2VsZi5teV9zdHJ1Y3QgPSBHbG9iYWxTdGF0ZShWZWN0b3IoeD1hcmM0LlN0cmluZygiMSIpLCB5PWFyYzQuU3RyaW5nKCIyIikpKQogICAgcHVzaGJ5dGVzcyAibXlfc3RydWN0IiAweDAwMDQwMDA3MDAwMTMxMDAwMTMyIC8vICJteV9zdHJ1Y3QiLCAweDAwMDQwMDA3MDAwMTMxMDAwMTMyCiAgICBhcHBfZ2xvYmFsX3B1dAoKbWFpbl9hZnRlcl9pZl9lbHNlQDI6CiAgICAvLyBzbWFydF9jb250cmFjdHMvaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTAKICAgIC8vIGNsYXNzIEhlbGxvV29ybGQoQVJDNENvbnRyYWN0KToKICAgIHR4biBOdW1BcHBBcmdzCiAgICBieiBtYWluX2JhcmVfcm91dGluZ0A2CiAgICBwdXNoYnl0ZXMgMHgwMmJlY2UxMSAvLyBtZXRob2QgImhlbGxvKHN0cmluZylzdHJpbmciCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAwCiAgICBtYXRjaCBtYWluX2hlbGxvX3JvdXRlQDUKCm1haW5fYWZ0ZXJfaWZfZWxzZUA4OgogICAgLy8gc21hcnRfY29udHJhY3RzL2hlbGxvX3dvcmxkL2NvbnRyYWN0LnB5OjEwCiAgICAvLyBjbGFzcyBIZWxsb1dvcmxkKEFSQzRDb250cmFjdCk6CiAgICBwdXNoaW50IDAgLy8gMAogICAgcmV0dXJuCgptYWluX2hlbGxvX3JvdXRlQDU6CiAgICAvLyBzbWFydF9jb250cmFjdHMvaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTUKICAgIC8vIEBhYmltZXRob2QoKQogICAgdHhuIE9uQ29tcGxldGlvbgogICAgIQogICAgYXNzZXJ0IC8vIE9uQ29tcGxldGlvbiBpcyBub3QgTm9PcAogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgIGFzc2VydCAvLyBjYW4gb25seSBjYWxsIHdoZW4gbm90IGNyZWF0aW5nCiAgICAvLyBzbWFydF9jb250cmFjdHMvaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTAKICAgIC8vIGNsYXNzIEhlbGxvV29ybGQoQVJDNENvbnRyYWN0KToKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDEKICAgIGV4dHJhY3QgMiAwCiAgICAvLyBzbWFydF9jb250cmFjdHMvaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTUKICAgIC8vIEBhYmltZXRob2QoKQogICAgY2FsbHN1YiBoZWxsbwogICAgZHVwCiAgICBsZW4KICAgIGl0b2IKICAgIGV4dHJhY3QgNiAyCiAgICBzd2FwCiAgICBjb25jYXQKICAgIHB1c2hieXRlcyAweDE1MWY3Yzc1CiAgICBzd2FwCiAgICBjb25jYXQKICAgIGxvZwogICAgcHVzaGludCAxIC8vIDEKICAgIHJldHVybgoKbWFpbl9iYXJlX3JvdXRpbmdANjoKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9oZWxsb193b3JsZC9jb250cmFjdC5weToxMAogICAgLy8gY2xhc3MgSGVsbG9Xb3JsZChBUkM0Q29udHJhY3QpOgogICAgdHhuIE9uQ29tcGxldGlvbgogICAgYm56IG1haW5fYWZ0ZXJfaWZfZWxzZUA4CiAgICB0eG4gQXBwbGljYXRpb25JRAogICAgIQogICAgYXNzZXJ0IC8vIGNhbiBvbmx5IGNhbGwgd2hlbiBjcmVhdGluZwogICAgcHVzaGludCAxIC8vIDEKICAgIHJldHVybgoKCi8vIHNtYXJ0X2NvbnRyYWN0cy5oZWxsb193b3JsZC5jb250cmFjdC5IZWxsb1dvcmxkLmhlbGxvKG5hbWU6IGJ5dGVzKSAtPiBieXRlczoKaGVsbG86CiAgICAvLyBzbWFydF9jb250cmFjdHMvaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTUtMTYKICAgIC8vIEBhYmltZXRob2QoKQogICAgLy8gZGVmIGhlbGxvKHNlbGYsIG5hbWU6IFN0cmluZykgLT4gU3RyaW5nOgogICAgcHJvdG8gMSAxCiAgICAvLyBzbWFydF9jb250cmFjdHMvaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTcKICAgIC8vIHJldHVybiAiSGVsbG8sICIgKyBuYW1lCiAgICBwdXNoYnl0ZXMgIkhlbGxvLCAiCiAgICBmcmFtZV9kaWcgLTEKICAgIGNvbmNhdAogICAgcmV0c3ViCg==", "clear": "I3ByYWdtYSB2ZXJzaW9uIDEwCiNwcmFnbWEgdHlwZXRyYWNrIGZhbHNlCgovLyBhbGdvcHkuYXJjNC5BUkM0Q29udHJhY3QuY2xlYXJfc3RhdGVfcHJvZ3JhbSgpIC0+IHVpbnQ2NDoKbWFpbjoKICAgIHB1c2hpbnQgMSAvLyAxCiAgICByZXR1cm4K"}, "sourceInfo": {"approval": {"pcOffsetMethod": "none", "sourceInfo": [{"pc": [54], "errorMessage": "OnCompletion is not NoOp"}, {"pc": [95], "errorMessage": "can only call when creating"}, {"pc": [57], "errorMessage": "can only call when not creating"}]}, "clear": {"pcOffsetMethod": "none", "sourceInfo": []}}, "templateVariables": {}}"""
APP_SPEC = algokit_utils.Arc56Contract.from_json(_APP_SPEC_JSON)

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
        convert_dataclass(arg) if not isinstance(arg, algokit_utils.AppMethodCallTransactionArgument) else arg
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
class Vector:
    """Struct for Vector"""
    x: str
    y: str


@dataclasses.dataclass(frozen=True, kw_only=True)
class HelloArgs:
    """Dataclass for hello arguments"""
    name: str


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
    box_references: list[algokit_utils.BoxReference | algokit_utils.BoxIdentifier] | None = None
    extra_fee: algokit_utils.AlgoAmount | None = None
    lease: bytes | None = None
    max_fee: algokit_utils.AlgoAmount | None = None
    note: bytes | None = None
    rekey_to: str | None = None
    sender: str | None = None
    signer: TransactionSigner | None = None
    static_fee: algokit_utils.AlgoAmount | None = None
    validity_window: int | None = None
    first_valid_round: int | None = None
    last_valid_round: int | None = None

@dataclasses.dataclass(frozen=True, kw_only=True)
class CommonAppFactoryCallParams(CommonAppCallParams):
    """Common configuration for app factory call related transaction parameters"""
    on_complete: ON_COMPLETE_TYPES | None = None


class HelloWorldParams:
    def __init__(self, app_client: algokit_utils.AppClient):
        self.app_client = app_client

    def hello(
        self,
        args: tuple[str] | HelloArgs,
        params: CommonAppCallParams | None = None
    ) -> algokit_utils.AppCallMethodCallParams:
        method_args = _parse_abi_args(args)
        params = params or CommonAppCallParams()
        return self.app_client.params.call(algokit_utils.AppClientMethodCallParams(**{
            **dataclasses.asdict(params),
            "method": "hello(string)string",
            "args": method_args,
        }))

    def clear_state(
        self,
        params: algokit_utils.AppClientBareCallParams | None = None,
        
    ) -> algokit_utils.AppCallParams:
        return self.app_client.params.bare.clear_state(
            params,
            
        )


class HelloWorldCreateTransactionParams:
    def __init__(self, app_client: algokit_utils.AppClient):
        self.app_client = app_client

    def hello(
        self,
        args: tuple[str] | HelloArgs,
        params: CommonAppCallParams | None = None
    ) -> algokit_utils.BuiltTransactions:
        method_args = _parse_abi_args(args)
        params = params or CommonAppCallParams()
        return self.app_client.create_transaction.call(algokit_utils.AppClientMethodCallParams(**{
            **dataclasses.asdict(params),
            "method": "hello(string)string",
            "args": method_args,
        }))

    def clear_state(
        self,
        params: algokit_utils.AppClientBareCallParams | None = None,
        
    ) -> Transaction:
        return self.app_client.create_transaction.bare.clear_state(
            params,
            
        )


class HelloWorldSend:
    def __init__(self, app_client: algokit_utils.AppClient):
        self.app_client = app_client

    def hello(
        self,
        args: tuple[str] | HelloArgs,
        params: CommonAppCallParams | None = None,
        send_params: algokit_utils.SendParams | None = None
    ) -> algokit_utils.SendAppTransactionResult[str]:
        method_args = _parse_abi_args(args)
        params = params or CommonAppCallParams()
        response = self.app_client.send.call(algokit_utils.AppClientMethodCallParams(**{
            **dataclasses.asdict(params),
            "method": "hello(string)string",
            "args": method_args,
        }), send_params=send_params)
        parsed_response = response
        return typing.cast(algokit_utils.SendAppTransactionResult[str], parsed_response)

    def clear_state(
        self,
        params: algokit_utils.AppClientBareCallParams | None = None,
        send_params: algokit_utils.SendParams | None = None
    ) -> algokit_utils.SendAppTransactionResult[algokit_utils.ABIReturn]:
        return self.app_client.send.bare.clear_state(
            params,
            send_params=send_params,
        )


class GlobalStateValue(typing.TypedDict):
    """Shape of global_state state key values"""
    my_struct: Vector

class HelloWorldState:
    """Methods to access state for the current HelloWorld app"""

    def __init__(self, app_client: algokit_utils.AppClient):
        self.app_client = app_client

    @property
    def global_state(
        self
    ) -> "_GlobalState":
            """Methods to access global_state for the current app"""
            return _GlobalState(self.app_client)

class _GlobalState:
    def __init__(self, app_client: algokit_utils.AppClient):
        self.app_client = app_client
        
        # Pre-generated mapping of value types to their struct classes
        self._struct_classes: dict[str, typing.Type[typing.Any]] = {
            "Vector": Vector
        }

    def get_all(self) -> GlobalStateValue:
        """Get all current keyed values from global_state state"""
        result = self.app_client.state.global_state.get_all()
        if not result:
            return typing.cast(GlobalStateValue, {})

        converted = {}
        for key, value in result.items():
            key_info = self.app_client.app_spec.state.keys.global_state.get(key)
            struct_class = self._struct_classes.get(key_info.value_type) if key_info else None
            converted[key] = (
                struct_class(**value) if struct_class and isinstance(value, dict)
                else value
            )
        return typing.cast(GlobalStateValue, converted)

    def my_struct(self) -> Vector:
            """Get the current value of the my_struct key in global_state state"""
            value = self.app_client.state.global_state.get_value("my_struct")
            if isinstance(value, dict) and "Vector" in self._struct_classes:
                return self._struct_classes["Vector"](**value)  # type: ignore
            return typing.cast(Vector, value)

class HelloWorldClient:
    """Client for interacting with HelloWorld smart contract"""

    @typing.overload
    def __init__(self, app_client: algokit_utils.AppClient) -> None: ...
    
    @typing.overload
    def __init__(
        self,
        *,
        algorand: _AlgoKitAlgorandClient,
        app_id: int,
        app_name: str | None = None,
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> None: ...

    def __init__(
        self,
        app_client: algokit_utils.AppClient | None = None,
        *,
        algorand: _AlgoKitAlgorandClient | None = None,
        app_id: int | None = None,
        app_name: str | None = None,
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> None:
        if app_client:
            self.app_client = app_client
        elif algorand and app_id:
            self.app_client = algokit_utils.AppClient(
                algokit_utils.AppClientParams(
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
    
        self.params = HelloWorldParams(self.app_client)
        self.create_transaction = HelloWorldCreateTransactionParams(self.app_client)
        self.send = HelloWorldSend(self.app_client)
        self.state = HelloWorldState(self.app_client)

    @staticmethod
    def from_creator_and_name(
        creator_address: str,
        app_name: str,
        algorand: _AlgoKitAlgorandClient,
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
        ignore_cache: bool | None = None,
        app_lookup_cache: algokit_utils.ApplicationLookup | None = None,
    ) -> "HelloWorldClient":
        return HelloWorldClient(
            algokit_utils.AppClient.from_creator_and_name(
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
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> "HelloWorldClient":
        return HelloWorldClient(
            algokit_utils.AppClient.from_network(
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
    def app_spec(self) -> algokit_utils.Arc56Contract:
        return self.app_client.app_spec
    
    @property
    def algorand(self) -> _AlgoKitAlgorandClient:
        return self.app_client.algorand

    def clone(
        self,
        app_name: str | None = None,
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> "HelloWorldClient":
        return HelloWorldClient(
            self.app_client.clone(
                app_name=app_name,
                default_sender=default_sender,
                default_signer=default_signer,
                approval_source_map=approval_source_map,
                clear_source_map=clear_source_map,
            )
        )

    def new_group(self) -> "HelloWorldComposer":
        return HelloWorldComposer(self)

    @typing.overload
    def decode_return_value(
        self,
        method: typing.Literal["hello(string)string"],
        return_value: algokit_utils.ABIReturn | None
    ) -> str | None: ...
    @typing.overload
    def decode_return_value(
        self,
        method: str,
        return_value: algokit_utils.ABIReturn | None
    ) -> algokit_utils.ABIValue | algokit_utils.ABIStruct | None: ...

    def decode_return_value(
        self,
        method: str,
        return_value: algokit_utils.ABIReturn | None
    ) -> algokit_utils.ABIValue | algokit_utils.ABIStruct | None | str:
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
class HelloWorldBareCallCreateParams(algokit_utils.AppClientBareCallCreateParams):
    """Parameters for creating HelloWorld contract with bare calls"""
    on_complete: typing.Literal[OnComplete.NoOpOC] | None = None

    def to_algokit_utils_params(self) -> algokit_utils.AppClientBareCallCreateParams:
        return algokit_utils.AppClientBareCallCreateParams(**self.__dict__)

class HelloWorldFactory(algokit_utils.TypedAppFactoryProtocol[HelloWorldBareCallCreateParams, None, None]):
    """Factory for deploying and managing HelloWorldClient smart contracts"""

    def __init__(
        self,
        algorand: _AlgoKitAlgorandClient,
        *,
        app_name: str | None = None,
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        version: str | None = None,
        compilation_params: algokit_utils.AppClientCompilationParams | None = None,
    ):
        self.app_factory = algokit_utils.AppFactory(
            params=algokit_utils.AppFactoryParams(
                algorand=algorand,
                app_spec=APP_SPEC,
                app_name=app_name,
                default_sender=default_sender,
                default_signer=default_signer,
                version=version,
                compilation_params=compilation_params,
            )
        )
        self.params = HelloWorldFactoryParams(self.app_factory)
        self.create_transaction = HelloWorldFactoryCreateTransaction(self.app_factory)
        self.send = HelloWorldFactorySend(self.app_factory)

    @property
    def app_name(self) -> str:
        return self.app_factory.app_name
    
    @property
    def app_spec(self) -> algokit_utils.Arc56Contract:
        return self.app_factory.app_spec
    
    @property
    def algorand(self) -> _AlgoKitAlgorandClient:
        return self.app_factory.algorand

    def deploy(
        self,
        *,
        on_update: algokit_utils.OnUpdate | None = None,
        on_schema_break: algokit_utils.OnSchemaBreak | None = None,
        create_params: HelloWorldBareCallCreateParams | None = None,
        update_params: None = None,
        delete_params: None = None,
        existing_deployments: algokit_utils.ApplicationLookup | None = None,
        ignore_cache: bool = False,
        app_name: str | None = None,
        compilation_params: algokit_utils.AppClientCompilationParams | None = None,
        send_params: algokit_utils.SendParams | None = None,
    ) -> tuple[HelloWorldClient, algokit_utils.AppFactoryDeployResult]:
        """Deploy the application"""
        deploy_response = self.app_factory.deploy(
            on_update=on_update,
            on_schema_break=on_schema_break,
            create_params=create_params.to_algokit_utils_params() if create_params else None,
            update_params=update_params,
            delete_params=delete_params,
            existing_deployments=existing_deployments,
            ignore_cache=ignore_cache,
            app_name=app_name,
            compilation_params=compilation_params,
            send_params=send_params,
        )

        return HelloWorldClient(deploy_response[0]), deploy_response[1]

    def get_app_client_by_creator_and_name(
        self,
        creator_address: str,
        app_name: str,
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        ignore_cache: bool | None = None,
        app_lookup_cache: algokit_utils.ApplicationLookup | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> HelloWorldClient:
        """Get an app client by creator address and name"""
        return HelloWorldClient(
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
        default_sender: str | None = None,
        default_signer: TransactionSigner | None = None,
        approval_source_map: SourceMap | None = None,
        clear_source_map: SourceMap | None = None,
    ) -> HelloWorldClient:
        """Get an app client by app ID"""
        return HelloWorldClient(
            self.app_factory.get_app_client_by_id(
                app_id,
                app_name,
                default_sender,
                default_signer,
                approval_source_map,
                clear_source_map,
            )
        )


class HelloWorldFactoryParams:
    """Parameters for creating transactions for HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory
        self.create = HelloWorldFactoryCreateParams(app_factory)
        self.update = HelloWorldFactoryUpdateParams(app_factory)
        self.delete = HelloWorldFactoryDeleteParams(app_factory)

class HelloWorldFactoryCreateParams:
    """Parameters for 'create' operations of HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        params: CommonAppFactoryCallParams | None = None,
        compilation_params: algokit_utils.AppClientCompilationParams | None = None
    ) -> algokit_utils.AppCreateParams:
        """Creates an instance using a bare call"""
        params = params or CommonAppFactoryCallParams()
        return self.app_factory.params.bare.create(
            algokit_utils.AppFactoryCreateParams(**dataclasses.asdict(params)),
            compilation_params=compilation_params)

    def hello(
        self,
        args: tuple[str] | HelloArgs,
        *,
        params: CommonAppFactoryCallParams | None = None,
        compilation_params: algokit_utils.AppClientCompilationParams | None = None
    ) -> algokit_utils.AppCreateMethodCallParams:
        """Creates a new instance using the hello(string)string ABI method"""
        params = params or CommonAppFactoryCallParams()
        return self.app_factory.params.create(
            algokit_utils.AppFactoryCreateMethodCallParams(
                **{
                **dataclasses.asdict(params),
                "method": "hello(string)string",
                "args": _parse_abi_args(args),
                }
            ),
            compilation_params=compilation_params
        )

class HelloWorldFactoryUpdateParams:
    """Parameters for 'update' operations of HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        params: CommonAppFactoryCallParams | None = None,
        
    ) -> algokit_utils.AppUpdateParams:
        """Updates an instance using a bare call"""
        params = params or CommonAppFactoryCallParams()
        return self.app_factory.params.bare.deploy_update(
            algokit_utils.AppFactoryCreateParams(**dataclasses.asdict(params)),
            )

class HelloWorldFactoryDeleteParams:
    """Parameters for 'delete' operations of HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        params: CommonAppFactoryCallParams | None = None,
        
    ) -> algokit_utils.AppDeleteParams:
        """Deletes an instance using a bare call"""
        params = params or CommonAppFactoryCallParams()
        return self.app_factory.params.bare.deploy_delete(
            algokit_utils.AppFactoryCreateParams(**dataclasses.asdict(params)),
            )


class HelloWorldFactoryCreateTransaction:
    """Create transactions for HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory
        self.create = HelloWorldFactoryCreateTransactionCreate(app_factory)


class HelloWorldFactoryCreateTransactionCreate:
    """Create new instances of HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        params: CommonAppFactoryCallParams | None = None,
    ) -> Transaction:
        """Creates a new instance using a bare call"""
        params = params or CommonAppFactoryCallParams()
        return self.app_factory.create_transaction.bare.create(
            algokit_utils.AppFactoryCreateParams(**dataclasses.asdict(params)),
        )


class HelloWorldFactorySend:
    """Send calls to HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory
        self.create = HelloWorldFactorySendCreate(app_factory)


class HelloWorldFactorySendCreate:
    """Send create calls to HelloWorld contract"""

    def __init__(self, app_factory: algokit_utils.AppFactory):
        self.app_factory = app_factory

    def bare(
        self,
        *,
        params: CommonAppFactoryCallParams | None = None,
        send_params: algokit_utils.SendParams | None = None,
        compilation_params: algokit_utils.AppClientCompilationParams | None = None,
    ) -> tuple[HelloWorldClient, algokit_utils.SendAppCreateTransactionResult]:
        """Creates a new instance using a bare call"""
        params = params or CommonAppFactoryCallParams()
        result = self.app_factory.send.bare.create(
            algokit_utils.AppFactoryCreateParams(**dataclasses.asdict(params)),
            send_params=send_params,
            compilation_params=compilation_params
        )
        return HelloWorldClient(result[0]), result[1]


class HelloWorldComposer:
    """Composer for creating transaction groups for HelloWorld contract calls"""

    def __init__(self, client: "HelloWorldClient"):
        self.client = client
        self._composer = client.algorand.new_group()
        self._result_mappers: list[typing.Callable[[algokit_utils.ABIReturn | None], typing.Any] | None] = []

    def hello(
        self,
        args: tuple[str] | HelloArgs,
        params: CommonAppCallParams | None = None
    ) -> "HelloWorldComposer":
        self._composer.add_app_call_method_call(
            self.client.params.hello(
                args=args,
                params=params,
            )
        )
        self._result_mappers.append(
            lambda v: self.client.decode_return_value(
                "hello(string)string", v
            )
        )
        return self

    def clear_state(
        self,
        *,
        args: list[bytes] | None = None,
        params: CommonAppCallParams | None = None,
    ) -> "HelloWorldComposer":
        params=params or CommonAppCallParams()
        self._composer.add_app_call(
            self.client.params.clear_state(
                algokit_utils.AppClientBareCallParams(
                    **{
                        **dataclasses.asdict(params),
                        "args": args
                    }
                )
            )
        )
        return self
    
    def add_transaction(
        self, txn: Transaction, signer: TransactionSigner | None = None
    ) -> "HelloWorldComposer":
        self._composer.add_transaction(txn, signer)
        return self
    
    def composer(self) -> algokit_utils.TransactionComposer:
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
    ) -> algokit_utils.SendAtomicTransactionComposerResults:
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
        send_params: algokit_utils.SendParams | None = None
    ) -> algokit_utils.SendAtomicTransactionComposerResults:
        return self._composer.send(send_params)
