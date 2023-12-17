"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import FinamPy.proto.tradeapi.v1.common_pb2 as common
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _StopStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StopStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StopStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STOP_STATUS_UNSPECIFIED: _StopStatus.ValueType  # 0
    """Value is not specified. Do not use.
    Значение не указано. Не использовать.
    """
    STOP_STATUS_NONE: _StopStatus.ValueType  # 1
    """Order is not in OrderBook.
    Заявка не выставлена.
    """
    STOP_STATUS_ACTIVE: _StopStatus.ValueType  # 2
    """Order is in OrderBook.
    Заявка выставлена.
    """
    STOP_STATUS_CANCELLED: _StopStatus.ValueType  # 3
    """Order is cancelled.
    Заявка отменена.
    """
    STOP_STATUS_EXECUTED: _StopStatus.ValueType  # 4
    """Order is executed.
    Заявка выполнена.
    """

class StopStatus(_StopStatus, metaclass=_StopStatusEnumTypeWrapper):
    """Stop order status.
    Состояние заявки.
    """

STOP_STATUS_UNSPECIFIED: StopStatus.ValueType  # 0
"""Value is not specified. Do not use.
Значение не указано. Не использовать.
"""
STOP_STATUS_NONE: StopStatus.ValueType  # 1
"""Order is not in OrderBook.
Заявка не выставлена.
"""
STOP_STATUS_ACTIVE: StopStatus.ValueType  # 2
"""Order is in OrderBook.
Заявка выставлена.
"""
STOP_STATUS_CANCELLED: StopStatus.ValueType  # 3
"""Order is cancelled.
Заявка отменена.
"""
STOP_STATUS_EXECUTED: StopStatus.ValueType  # 4
"""Order is executed.
Заявка выполнена.
"""
global___StopStatus = StopStatus

class _StopQuantityUnits:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StopQuantityUnitsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StopQuantityUnits.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STOP_QUANTITY_UNITS_UNSPECIFIED: _StopQuantityUnits.ValueType  # 0
    """Value is not specified. Do not use.
    Значение не указано. Не использовать.
    """
    STOP_QUANTITY_UNITS_PERCENT: _StopQuantityUnits.ValueType  # 1
    """Percent.
    Значение а процентах.
    """
    STOP_QUANTITY_UNITS_LOTS: _StopQuantityUnits.ValueType  # 2
    """Lots.
    Значение в лотах.
    """

class StopQuantityUnits(_StopQuantityUnits, metaclass=_StopQuantityUnitsEnumTypeWrapper):
    """Stop quantity units.
    Единицы объема стоп-заявки.
    """

STOP_QUANTITY_UNITS_UNSPECIFIED: StopQuantityUnits.ValueType  # 0
"""Value is not specified. Do not use.
Значение не указано. Не использовать.
"""
STOP_QUANTITY_UNITS_PERCENT: StopQuantityUnits.ValueType  # 1
"""Percent.
Значение а процентах.
"""
STOP_QUANTITY_UNITS_LOTS: StopQuantityUnits.ValueType  # 2
"""Lots.
Значение в лотах.
"""
global___StopQuantityUnits = StopQuantityUnits

class _StopPriceUnits:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StopPriceUnitsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StopPriceUnits.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STOP_PRICE_UNITS_UNSPECIFIED: _StopPriceUnits.ValueType  # 0
    """Value is not specified. Do not use.
    Значение не указано. Не использовать.
    """
    STOP_PRICE_UNITS_PERCENT: _StopPriceUnits.ValueType  # 1
    """Percent.
    Значение а процентах.
    """
    STOP_PRICE_UNITS_PIPS: _StopPriceUnits.ValueType  # 2
    """Lots.
    Значение в лотах.
    """

class StopPriceUnits(_StopPriceUnits, metaclass=_StopPriceUnitsEnumTypeWrapper):
    """Stop price units.
    Единицы цены стоп-заявки.
    """

STOP_PRICE_UNITS_UNSPECIFIED: StopPriceUnits.ValueType  # 0
"""Value is not specified. Do not use.
Значение не указано. Не использовать.
"""
STOP_PRICE_UNITS_PERCENT: StopPriceUnits.ValueType  # 1
"""Percent.
Значение а процентах.
"""
STOP_PRICE_UNITS_PIPS: StopPriceUnits.ValueType  # 2
"""Lots.
Значение в лотах.
"""
global___StopPriceUnits = StopPriceUnits

@typing_extensions.final
class Stop(google.protobuf.message.Message):
    """Stop Order.
    Стоп-заявка.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STOP_ID_FIELD_NUMBER: builtins.int
    SECURITY_CODE_FIELD_NUMBER: builtins.int
    SECURITY_BOARD_FIELD_NUMBER: builtins.int
    MARKET_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    BUY_SELL_FIELD_NUMBER: builtins.int
    EXPIRATION_DATE_FIELD_NUMBER: builtins.int
    LINK_ORDER_FIELD_NUMBER: builtins.int
    VALID_BEFORE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    ORDER_NO_FIELD_NUMBER: builtins.int
    TRADE_NO_FIELD_NUMBER: builtins.int
    ACCEPTED_AT_FIELD_NUMBER: builtins.int
    CANCELED_AT_FIELD_NUMBER: builtins.int
    CURRENCY_FIELD_NUMBER: builtins.int
    TAKE_PROFIT_EXTREMUM_FIELD_NUMBER: builtins.int
    TAKE_PROFIT_LEVEL_FIELD_NUMBER: builtins.int
    STOP_LOSS_FIELD_NUMBER: builtins.int
    TAKE_PROFIT_FIELD_NUMBER: builtins.int
    stop_id: builtins.int
    """Stop Order Id.
    Идентификатор стоп-заявки.
    """
    security_code: builtins.str
    """Security Code.
    Тикер инструмента.
    """
    security_board: builtins.str
    """Security Board.
    Основной режим торгов инструмента.
    """
    market: common.Market.ValueType
    """Market.
    Рынок.
    """
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    buy_sell: common.BuySell.ValueType
    """Transaction direction.
    Направление сделки.
    """
    @property
    def expiration_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Expiration date for FORTS order.
        Дата экспирации заявки FORTS.
        """
    link_order: builtins.int
    """Linked order ID.
    Биржевой номер связанной (активной) заявки.
    """
    @property
    def valid_before(self) -> common.OrderValidBefore:
        """Order lifetime.
        Время действия заявки.
        """
    status: global___StopStatus.ValueType
    """Order status.
    Состояние заявки.
    """
    message: builtins.str
    """Rejection reason or conditional order resolution.
    Причина отказа или вердикт по условной заявке.
    """
    order_no: builtins.int
    """Order No.
    Номер заявки, полученной в результате исполнения стопа.
    """
    trade_no: builtins.int
    """Trade No.
    Номер сделки, которая привела к исполнению стопа.
    """
    @property
    def accepted_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of order registration on the server in UTC.
        Время, когда заявка была зарегистрирована на сервере. В UTC.
        """
    @property
    def canceled_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of order canceled on the server in UTC.
        Время, когда заявка была отменена на сервере. В UTC.
        """
    currency: builtins.str
    """Price currency.
    Валюта цены.
    """
    take_profit_extremum: builtins.float
    """Take profit: local extremum.
    Тейк профит: текущий локальный экстремум.
    """
    take_profit_level: builtins.float
    """Take profit: correction level.
    Тейк профит: текущий уровень коррекции.
    """
    @property
    def stop_loss(self) -> global___StopLoss:
        """Stop loss.
        Стоп лосс.
        """
    @property
    def take_profit(self) -> global___TakeProfit:
        """Take profit.
        Тейк профит.
        """
    def __init__(
        self,
        *,
        stop_id: builtins.int = ...,
        security_code: builtins.str = ...,
        security_board: builtins.str = ...,
        market: common.Market.ValueType = ...,
        client_id: builtins.str = ...,
        buy_sell: common.BuySell.ValueType = ...,
        expiration_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        link_order: builtins.int = ...,
        valid_before: common.OrderValidBefore | None = ...,
        status: global___StopStatus.ValueType = ...,
        message: builtins.str = ...,
        order_no: builtins.int = ...,
        trade_no: builtins.int = ...,
        accepted_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        canceled_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        currency: builtins.str = ...,
        take_profit_extremum: builtins.float = ...,
        take_profit_level: builtins.float = ...,
        stop_loss: global___StopLoss | None = ...,
        take_profit: global___TakeProfit | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accepted_at", b"accepted_at", "canceled_at", b"canceled_at", "expiration_date", b"expiration_date", "stop_loss", b"stop_loss", "take_profit", b"take_profit", "valid_before", b"valid_before"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accepted_at", b"accepted_at", "buy_sell", b"buy_sell", "canceled_at", b"canceled_at", "client_id", b"client_id", "currency", b"currency", "expiration_date", b"expiration_date", "link_order", b"link_order", "market", b"market", "message", b"message", "order_no", b"order_no", "security_board", b"security_board", "security_code", b"security_code", "status", b"status", "stop_id", b"stop_id", "stop_loss", b"stop_loss", "take_profit", b"take_profit", "take_profit_extremum", b"take_profit_extremum", "take_profit_level", b"take_profit_level", "trade_no", b"trade_no", "valid_before", b"valid_before"]) -> None: ...

global___Stop = Stop

@typing_extensions.final
class StopLoss(google.protobuf.message.Message):
    """StopLoss order.
    Стоп лосс заявка.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVATION_PRICE_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    MARKET_PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    USE_CREDIT_FIELD_NUMBER: builtins.int
    activation_price: builtins.float
    """Activation price.
    Цена активации.
    """
    price: builtins.float
    """Price.
    Цена заявки.
    """
    market_price: builtins.bool
    """Market price.
    По рынку.
    """
    @property
    def quantity(self) -> global___StopQuantity:
        """Quantity.
        Количество.
        """
    time: builtins.int
    """Time, seconds.
    Защитное время, сек.
    """
    use_credit: builtins.bool
    """Use credit.
    Использовать кредит.
    """
    def __init__(
        self,
        *,
        activation_price: builtins.float = ...,
        price: builtins.float = ...,
        market_price: builtins.bool = ...,
        quantity: global___StopQuantity | None = ...,
        time: builtins.int = ...,
        use_credit: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["quantity", b"quantity"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activation_price", b"activation_price", "market_price", b"market_price", "price", b"price", "quantity", b"quantity", "time", b"time", "use_credit", b"use_credit"]) -> None: ...

global___StopLoss = StopLoss

@typing_extensions.final
class TakeProfit(google.protobuf.message.Message):
    """TakeProfit order.
    Тейк профит заявка.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVATION_PRICE_FIELD_NUMBER: builtins.int
    CORRECTION_PRICE_FIELD_NUMBER: builtins.int
    SPREAD_PRICE_FIELD_NUMBER: builtins.int
    MARKET_PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    USE_CREDIT_FIELD_NUMBER: builtins.int
    activation_price: builtins.float
    """Activation price.
    Цена активации.
    """
    @property
    def correction_price(self) -> global___StopPrice:
        """Correction.
        Коррекция.
        """
    @property
    def spread_price(self) -> global___StopPrice:
        """Spread price.
        Защитный спрэд.
        """
    market_price: builtins.bool
    """Market price.
    По рынку.
    """
    @property
    def quantity(self) -> global___StopQuantity:
        """Quantity.
        Количество.
        """
    time: builtins.int
    """Time, seconds.
    Защитное время, сек.
    """
    use_credit: builtins.bool
    """Use credit.
    Использовать кредит.
    """
    def __init__(
        self,
        *,
        activation_price: builtins.float = ...,
        correction_price: global___StopPrice | None = ...,
        spread_price: global___StopPrice | None = ...,
        market_price: builtins.bool = ...,
        quantity: global___StopQuantity | None = ...,
        time: builtins.int = ...,
        use_credit: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["correction_price", b"correction_price", "quantity", b"quantity", "spread_price", b"spread_price"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activation_price", b"activation_price", "correction_price", b"correction_price", "market_price", b"market_price", "quantity", b"quantity", "spread_price", b"spread_price", "time", b"time", "use_credit", b"use_credit"]) -> None: ...

global___TakeProfit = TakeProfit

@typing_extensions.final
class StopQuantity(google.protobuf.message.Message):
    """Stop quantity.
    Объем стоп-заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    UNITS_FIELD_NUMBER: builtins.int
    value: builtins.float
    """Value.
    Значение объема.
    """
    units: global___StopQuantityUnits.ValueType
    """Units.
    Единицы объема.
    """
    def __init__(
        self,
        *,
        value: builtins.float = ...,
        units: global___StopQuantityUnits.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["units", b"units", "value", b"value"]) -> None: ...

global___StopQuantity = StopQuantity

@typing_extensions.final
class StopPrice(google.protobuf.message.Message):
    """Stop price.
    Цена стоп-заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    UNITS_FIELD_NUMBER: builtins.int
    value: builtins.float
    """Value.
    Значение цены.
    """
    units: global___StopPriceUnits.ValueType
    """Units.
    Единицы цены.
    """
    def __init__(
        self,
        *,
        value: builtins.float = ...,
        units: global___StopPriceUnits.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["units", b"units", "value", b"value"]) -> None: ...

global___StopPrice = StopPrice

@typing_extensions.final
class CancelStopRequest(google.protobuf.message.Message):
    """Request for Stop Order cancellation.
    Запрос на снятие стоп-заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    STOP_ID_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    stop_id: builtins.int
    """Stop Order Id.
    Идентификатор стоп-заявки.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        stop_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "stop_id", b"stop_id"]) -> None: ...

global___CancelStopRequest = CancelStopRequest

@typing_extensions.final
class CancelStopResult(google.protobuf.message.Message):
    """Result of Stop Order cancellation.
    Результат отмены стоп-заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    STOP_ID_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    stop_id: builtins.int
    """Stop Order Id.
    Идентификатор стоп-заявки.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        stop_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "stop_id", b"stop_id"]) -> None: ...

global___CancelStopResult = CancelStopResult

@typing_extensions.final
class GetStopsRequest(google.protobuf.message.Message):
    """Request for the list of Stop Orders.
    Запрос стоп-заявок.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    INCLUDE_EXECUTED_FIELD_NUMBER: builtins.int
    INCLUDE_CANCELED_FIELD_NUMBER: builtins.int
    INCLUDE_ACTIVE_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    include_executed: builtins.bool
    """Include executed stops in response.
    Вернуть исполненные стоп-заявки.
    """
    include_canceled: builtins.bool
    """Include canceled stops in response.
    Вернуть отмененные стоп-заявки.
    """
    include_active: builtins.bool
    """Include active stops in response.
    Вернуть активные стоп-заявки.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        include_executed: builtins.bool = ...,
        include_canceled: builtins.bool = ...,
        include_active: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "include_active", b"include_active", "include_canceled", b"include_canceled", "include_executed", b"include_executed"]) -> None: ...

global___GetStopsRequest = GetStopsRequest

@typing_extensions.final
class GetStopsResult(google.protobuf.message.Message):
    """Result of Stop Orders request.
    Результат запроса стоп-заявок.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    STOPS_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    @property
    def stops(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Stop]:
        """Stop Orders List.
        Список стоп-заявок.
        """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        stops: collections.abc.Iterable[global___Stop] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "stops", b"stops"]) -> None: ...

global___GetStopsResult = GetStopsResult

@typing_extensions.final
class NewStopRequest(google.protobuf.message.Message):
    """New Stop Order request.
    Запрос на выставление стоп заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    SECURITY_BOARD_FIELD_NUMBER: builtins.int
    SECURITY_CODE_FIELD_NUMBER: builtins.int
    BUY_SELL_FIELD_NUMBER: builtins.int
    STOP_LOSS_FIELD_NUMBER: builtins.int
    TAKE_PROFIT_FIELD_NUMBER: builtins.int
    EXPIRATION_DATE_FIELD_NUMBER: builtins.int
    LINK_ORDER_FIELD_NUMBER: builtins.int
    VALID_BEFORE_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    security_board: builtins.str
    """Trading Board.
    Режим торгов.
    """
    security_code: builtins.str
    """Security Code.
    Тикер инструмента.
    """
    buy_sell: common.BuySell.ValueType
    """Transaction direction.
    Направление сделки.
    """
    @property
    def stop_loss(self) -> global___StopLoss:
        """Stop loss.
        Стоп лосс.
        """
    @property
    def take_profit(self) -> global___TakeProfit:
        """Take profit.
        Тейк профит.
        """
    @property
    def expiration_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Expiration date for FORTS order.
        Дата экспирации заявки FORTS.
        """
    link_order: builtins.int
    """Linked order ID.
    Биржевой номер связанной (активной) заявки.
    """
    @property
    def valid_before(self) -> common.OrderValidBefore:
        """Order lifetime.
        Время действия заявки.
        """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        security_board: builtins.str = ...,
        security_code: builtins.str = ...,
        buy_sell: common.BuySell.ValueType = ...,
        stop_loss: global___StopLoss | None = ...,
        take_profit: global___TakeProfit | None = ...,
        expiration_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        link_order: builtins.int = ...,
        valid_before: common.OrderValidBefore | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expiration_date", b"expiration_date", "stop_loss", b"stop_loss", "take_profit", b"take_profit", "valid_before", b"valid_before"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["buy_sell", b"buy_sell", "client_id", b"client_id", "expiration_date", b"expiration_date", "link_order", b"link_order", "security_board", b"security_board", "security_code", b"security_code", "stop_loss", b"stop_loss", "take_profit", b"take_profit", "valid_before", b"valid_before"]) -> None: ...

global___NewStopRequest = NewStopRequest

@typing_extensions.final
class NewStopResult(google.protobuf.message.Message):
    """Result of new Stop Order request.
    Результат выставления стоп заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    STOP_ID_FIELD_NUMBER: builtins.int
    SECURITY_CODE_FIELD_NUMBER: builtins.int
    SECURITY_BOARD_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account Id.
    Идентификатор торгового счёта.
    """
    stop_id: builtins.int
    """Stop Order Id.
    Идентификатор стоп заявки.
    """
    security_code: builtins.str
    """Security Code.
    Тикер инструмента.
    """
    security_board: builtins.str
    """Trading Board.
    Режим торгов.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        stop_id: builtins.int = ...,
        security_code: builtins.str = ...,
        security_board: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "security_board", b"security_board", "security_code", b"security_code", "stop_id", b"stop_id"]) -> None: ...

global___NewStopResult = NewStopResult
