# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/tradeapi/v1/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from FinamPy.proto.tradeapi.v1 import common_pb2 as proto_dot_tradeapi_dot_v1_dot_common__pb2
from FinamPy.proto.tradeapi.v1 import orders_pb2 as proto_dot_tradeapi_dot_v1_dot_orders__pb2
from FinamPy.proto.tradeapi.v1 import portfolios_pb2 as proto_dot_tradeapi_dot_v1_dot_portfolios__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/tradeapi/v1/events.proto\x12\x11proto.tradeapi.v1\x1a\x1eproto/tradeapi/v1/common.proto\x1a\x1eproto/tradeapi/v1/orders.proto\x1a\"proto/tradeapi/v1/portfolios.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xce\x01\n\tTimeFrame\x12\x34\n\ttime_unit\x18\x01 \x01(\x0e\x32!.proto.tradeapi.v1.TimeFrame.Unit\"\x8a\x01\n\x04Unit\x12\x14\n\x10UNIT_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUNIT_MINUTE\x10\x01\x12\r\n\tUNIT_HOUR\x10\x02\x12\x0c\n\x08UNIT_DAY\x10\x03\x12\r\n\tUNIT_WEEK\x10\x04\x12\x0e\n\nUNIT_MONTH\x10\x05\x12\x10\n\x0cUNIT_QUARTER\x10\x06\x12\r\n\tUNIT_YEAR\x10\x07\"\x84\x03\n\x13SubscriptionRequest\x12T\n\x1corder_book_subscribe_request\x18\x01 \x01(\x0b\x32,.proto.tradeapi.v1.OrderBookSubscribeRequestH\x00\x12X\n\x1eorder_book_unsubscribe_request\x18\x02 \x01(\x0b\x32..proto.tradeapi.v1.OrderBookUnsubscribeRequestH\x00\x12V\n\x1dorder_trade_subscribe_request\x18\x03 \x01(\x0b\x32-.proto.tradeapi.v1.OrderTradeSubscribeRequestH\x00\x12Z\n\x1forder_trade_unsubscribe_request\x18\x04 \x01(\x0b\x32/.proto.tradeapi.v1.OrderTradeUnsubscribeRequestH\x00\x42\t\n\x07payload\"\x99\x02\n\x05\x45vent\x12.\n\x05order\x18\x01 \x01(\x0b\x32\x1d.proto.tradeapi.v1.OrderEventH\x00\x12.\n\x05trade\x18\x02 \x01(\x0b\x32\x1d.proto.tradeapi.v1.TradeEventH\x00\x12\x37\n\norder_book\x18\x03 \x01(\x0b\x32!.proto.tradeapi.v1.OrderBookEventH\x00\x12\x36\n\tportfolio\x18\x05 \x01(\x0b\x32!.proto.tradeapi.v1.PortfolioEventH\x00\x12\x34\n\x08response\x18\n \x01(\x0b\x32 .proto.tradeapi.v1.ResponseEventH\x00\x42\t\n\x07payload\"^\n\x19OrderBookSubscribeRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x15\n\rsecurity_code\x18\x02 \x01(\t\x12\x16\n\x0esecurity_board\x18\x03 \x01(\t\"`\n\x1bOrderBookUnsubscribeRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x15\n\rsecurity_code\x18\x02 \x01(\t\x12\x16\n\x0esecurity_board\x18\x03 \x01(\t\"t\n\x1aOrderTradeSubscribeRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x16\n\x0einclude_trades\x18\x02 \x01(\x08\x12\x16\n\x0einclude_orders\x18\x03 \x01(\x08\x12\x12\n\nclient_ids\x18\x04 \x03(\t\"2\n\x1cOrderTradeUnsubscribeRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\"`\n\x15PortfolioSubscription\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x34\n\x07\x63ontent\x18\x02 \x01(\x0b\x32#.proto.tradeapi.v1.PortfolioContent\"\xe5\x03\n\nOrderEvent\x12\x10\n\x08order_no\x18\x01 \x01(\x03\x12\x16\n\x0etransaction_id\x18\x02 \x01(\x05\x12\x15\n\rsecurity_code\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12.\n\x06status\x18\x05 \x01(\x0e\x32\x1e.proto.tradeapi.v1.OrderStatus\x12,\n\x08\x62uy_sell\x18\x06 \x01(\x0e\x32\x1a.proto.tradeapi.v1.BuySell\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05price\x18\x08 \x01(\x01\x12\x10\n\x08quantity\x18\t \x01(\x05\x12\x0f\n\x07\x62\x61lance\x18\n \x01(\x05\x12\x0f\n\x07message\x18\x0b \x01(\t\x12\x10\n\x08\x63urrency\x18\x0c \x01(\t\x12\x34\n\tcondition\x18\r \x01(\x0b\x32!.proto.tradeapi.v1.OrderCondition\x12\x39\n\x0cvalid_before\x18\x0e \x01(\x0b\x32#.proto.tradeapi.v1.OrderValidBefore\x12/\n\x0b\x61\x63\x63\x65pted_at\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa8\x02\n\nTradeEvent\x12\x15\n\rsecurity_code\x18\x01 \x01(\t\x12\x10\n\x08trade_no\x18\x02 \x01(\x03\x12\x10\n\x08order_no\x18\x03 \x01(\x03\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08quantity\x18\x06 \x01(\x03\x12\r\n\x05price\x18\x07 \x01(\x01\x12\r\n\x05value\x18\x08 \x01(\x01\x12,\n\x08\x62uy_sell\x18\t \x01(\x0e\x32\x1a.proto.tradeapi.v1.BuySell\x12\x12\n\ncommission\x18\n \x01(\x01\x12\x10\n\x08\x63urrency\x18\x0b \x01(\t\x12\x18\n\x10\x61\x63\x63rued_interest\x18\x0c \x01(\x01\"5\n\x0cOrderBookRow\x12\x10\n\x05price\x18\x01 \x01(\x01R\x01p\x12\x13\n\x08quantity\x18\x02 \x01(\x03R\x01q\"\x9d\x01\n\x0eOrderBookEvent\x12\x15\n\rsecurity_code\x18\x01 \x01(\t\x12\x16\n\x0esecurity_board\x18\x02 \x01(\t\x12-\n\x04\x61sks\x18\x03 \x03(\x0b\x32\x1f.proto.tradeapi.v1.OrderBookRow\x12-\n\x04\x62ids\x18\x04 \x03(\x0b\x32\x1f.proto.tradeapi.v1.OrderBookRow\"\x8d\x02\n\x0ePortfolioEvent\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x34\n\x07\x63ontent\x18\x02 \x01(\x0b\x32#.proto.tradeapi.v1.PortfolioContent\x12\x0e\n\x06\x65quity\x18\x03 \x01(\x01\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x01\x12\x31\n\tpositions\x18\x05 \x03(\x0b\x32\x1e.proto.tradeapi.v1.PositionRow\x12\x32\n\ncurrencies\x18\x06 \x03(\x0b\x32\x1e.proto.tradeapi.v1.CurrencyRow\x12*\n\x05money\x18\x07 \x03(\x0b\x32\x1b.proto.tradeapi.v1.MoneyRowB\x1a\xaa\x02\x17\x46inam.TradeApi.Proto.V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.tradeapi.v1.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\027Finam.TradeApi.Proto.V1'
  _TIMEFRAME._serialized_start=187
  _TIMEFRAME._serialized_end=393
  _TIMEFRAME_UNIT._serialized_start=255
  _TIMEFRAME_UNIT._serialized_end=393
  _SUBSCRIPTIONREQUEST._serialized_start=396
  _SUBSCRIPTIONREQUEST._serialized_end=784
  _EVENT._serialized_start=787
  _EVENT._serialized_end=1068
  _ORDERBOOKSUBSCRIBEREQUEST._serialized_start=1070
  _ORDERBOOKSUBSCRIBEREQUEST._serialized_end=1164
  _ORDERBOOKUNSUBSCRIBEREQUEST._serialized_start=1166
  _ORDERBOOKUNSUBSCRIBEREQUEST._serialized_end=1262
  _ORDERTRADESUBSCRIBEREQUEST._serialized_start=1264
  _ORDERTRADESUBSCRIBEREQUEST._serialized_end=1380
  _ORDERTRADEUNSUBSCRIBEREQUEST._serialized_start=1382
  _ORDERTRADEUNSUBSCRIBEREQUEST._serialized_end=1432
  _PORTFOLIOSUBSCRIPTION._serialized_start=1434
  _PORTFOLIOSUBSCRIPTION._serialized_end=1530
  _ORDEREVENT._serialized_start=1533
  _ORDEREVENT._serialized_end=2018
  _TRADEEVENT._serialized_start=2021
  _TRADEEVENT._serialized_end=2317
  _ORDERBOOKROW._serialized_start=2319
  _ORDERBOOKROW._serialized_end=2372
  _ORDERBOOKEVENT._serialized_start=2375
  _ORDERBOOKEVENT._serialized_end=2532
  _PORTFOLIOEVENT._serialized_start=2535
  _PORTFOLIOEVENT._serialized_end=2804
# @@protoc_insertion_point(module_scope)
