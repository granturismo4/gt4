from iconsdk.builder.call_builder import CallBuilder
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.wallet.wallet import KeyWallet
from iconsdk.signed_transaction import SignedTransaction


class RPC:

    TESTNET = "https://bicon.net.solidwallet.io/api/v3"
    LOCALHOST = "http://127.0.0.1:9000/api/v3"

    def __init__(self, to_contract="cx2dedff5f8e54152923b0d635280fb46f721fadf6"):
        self._to_contract = to_contract

    def rpc_call_band(self, method, params):
        icon_service = IconService(HTTPProvider(RPC.TESTNET))
        call_builder = CallBuilder() \
            .to("cx690c2ff7941a575e9ef52f02e7636f0a08b054f4") \
            .method(method) \
            .params(params) \
            .build()

        response = icon_service.call(call_builder)

        return response

    def rpc_call(self, method, params):
        icon_service = IconService(HTTPProvider(RPC.TESTNET))
        call_builder = CallBuilder() \
            .to(self._to_contract) \
            .method(method) \
            .params(params) \
            .build()

        response = icon_service.call(call_builder)

        return response

    def rpc_call_transaction(self, method, params):

        wallet = KeyWallet.load("/home/gt4/SCORE/y1keystore", "@icon123")        

        icon_service = IconService(HTTPProvider(RPC.TESTNET))
        transaction = CallTransactionBuilder() \
            .from_(wallet.get_address()) \
            .to(self._to_contract) \
            .step_limit(2000000) \
            .nid(3) \
            .nonce(100) \
            .method(method) \
            .params(params) \
            .build()

        signed_transaction = SignedTransaction(transaction, wallet)
        tx_hash = icon_service.send_transaction(signed_transaction)

        return tx_hash
