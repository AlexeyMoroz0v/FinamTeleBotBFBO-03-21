# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from FinamPy.proto.tradeapi.v1 import portfolios_pb2 as proto_dot_tradeapi_dot_v1_dot_portfolios__pb2


class PortfoliosStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPortfolio = channel.unary_unary(
                '/grpc.tradeapi.v1.Portfolios/GetPortfolio',
                request_serializer=proto_dot_tradeapi_dot_v1_dot_portfolios__pb2.GetPortfolioRequest.SerializeToString,
                response_deserializer=proto_dot_tradeapi_dot_v1_dot_portfolios__pb2.GetPortfolioResult.FromString,
                )


class PortfoliosServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPortfolio(self, request, context):
        """Returns portfolio.
        Возвращает портфель.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PortfoliosServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPortfolio': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPortfolio,
                    request_deserializer=proto_dot_tradeapi_dot_v1_dot_portfolios__pb2.GetPortfolioRequest.FromString,
                    response_serializer=proto_dot_tradeapi_dot_v1_dot_portfolios__pb2.GetPortfolioResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.tradeapi.v1.Portfolios', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Portfolios(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPortfolio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.tradeapi.v1.Portfolios/GetPortfolio',
            proto_dot_tradeapi_dot_v1_dot_portfolios__pb2.GetPortfolioRequest.SerializeToString,
            proto_dot_tradeapi_dot_v1_dot_portfolios__pb2.GetPortfolioResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
