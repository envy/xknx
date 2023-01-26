"""Module for XKNX Exception handling."""
# flake8: noqa
from .exception import (
    CommunicationError,
    ConfirmationError,
    ConversionError,
    CouldNotParseAddress,
    CouldNotParseKNXIP,
    CouldNotParseTelegram,
    DataSecureException,
    DeviceIllegalValue,
    IncompleteKNXIPFrame,
    InvalidSecureConfiguration,
    KNXSecureValidationError,
    ManagementConnectionError,
    ManagementConnectionRefused,
    ManagementConnectionTimeout,
    SecureException,
    TunnellingAckError,
    UnsupportedCEMIMessage,
    XKNXException,
)

__all__ = [
    "CommunicationError",
    "ConfirmationError",
    "ConversionError",
    "CouldNotParseAddress",
    "CouldNotParseKNXIP",
    "CouldNotParseTelegram",
    "DataSecureException",
    "DeviceIllegalValue",
    "ManagementConnectionError",
    "ManagementConnectionRefused",
    "ManagementConnectionTimeout",
    "IncompleteKNXIPFrame",
    "InvalidSecureConfiguration",
    "KNXSecureValidationError",
    "SecureException",
    "TunnellingAckError",
    "UnsupportedCEMIMessage",
    "XKNXException",
]
