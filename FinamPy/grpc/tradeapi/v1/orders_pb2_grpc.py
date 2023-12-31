# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from FinamPy.proto.tradeapi.v1 import orders_pb2 as proto_dot_tradeapi_dot_v1_dot_orders__pb2


class OrdersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NewOrder = channel.unary_unary(
                '/grpc.tradeapi.v1.Orders/NewOrder',
                request_serializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.NewOrderRequest.SerializeToString,
                response_deserializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.NewOrderResult.FromString,
                )
        self.CancelOrder = channel.unary_unary(
                '/grpc.tradeapi.v1.Orders/CancelOrder',
                request_serializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.CancelOrderRequest.SerializeToString,
                response_deserializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.CancelOrderResult.FromString,
                )
        self.GetOrders = channel.unary_unary(
                '/grpc.tradeapi.v1.Orders/GetOrders',
                request_serializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.GetOrdersRequest.SerializeToString,
                response_deserializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.GetOrdersResult.FromString,
                )


class OrdersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NewOrder(self, request, context):
        """Creates new order.
        Order placement in OrderBook takes some time due to processing speed,
        that is why this method returns transaction_id, which can be used
        to find corresponding order in GetOrdersRequest or in OrderEvent message
        of Events service (EventResponse.event.order).
        Создать новую заявку.
        На обработку нового поручения по размещению заявки в биржевой стакан
        требуется некоторое время, поэтому этот метод возвращает структуру с
        transaction_id, которая может быть использована для поиска соответствующей
        заявки через GetOrdersRequest или в сообщении OrderEvent от сервиса событий
        (EventResponse.event.order).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOrder(self, request, context):
        """Cancels order.
        Отменяет заявку.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrders(self, request, context):
        """Returns the list of orders.
        Возвращает список заявок.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrdersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NewOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.NewOrder,
                    request_deserializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.NewOrderRequest.FromString,
                    response_serializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.NewOrderResult.SerializeToString,
            ),
            'CancelOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOrder,
                    request_deserializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.CancelOrderRequest.FromString,
                    response_serializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.CancelOrderResult.SerializeToString,
            ),
            'GetOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrders,
                    request_deserializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.GetOrdersRequest.FromString,
                    response_serializer=proto_dot_tradeapi_dot_v1_dot_orders__pb2.GetOrdersResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.tradeapi.v1.Orders', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Orders(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NewOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.tradeapi.v1.Orders/NewOrder',
            proto_dot_tradeapi_dot_v1_dot_orders__pb2.NewOrderRequest.SerializeToString,
            proto_dot_tradeapi_dot_v1_dot_orders__pb2.NewOrderResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.tradeapi.v1.Orders/CancelOrder',
            proto_dot_tradeapi_dot_v1_dot_orders__pb2.CancelOrderRequest.SerializeToString,
            proto_dot_tradeapi_dot_v1_dot_orders__pb2.CancelOrderResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.tradeapi.v1.Orders/GetOrders',
            proto_dot_tradeapi_dot_v1_dot_orders__pb2.GetOrdersRequest.SerializeToString,
            proto_dot_tradeapi_dot_v1_dot_orders__pb2.GetOrdersResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
