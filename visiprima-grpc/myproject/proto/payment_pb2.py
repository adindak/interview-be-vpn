# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payment.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpayment.proto\x12\x07payment\"\x1e\n\x0ePaymentRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\"E\n\x0fPaymentResponse\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x14\n\x0cpayment_date\x18\x03 \x01(\t\"A\n\x13PaymentListResponse\x12*\n\x08payments\x18\x01 \x03(\x0b\x32\x18.payment.PaymentResponse\"\x07\n\x05\x45mpty2\x98\x01\n\x0ePaymentService\x12\x46\n\x11GetPaymentDetails\x12\x17.payment.PaymentRequest\x1a\x18.payment.PaymentResponse\x12>\n\x0eGetAllPayments\x12\x0e.payment.Empty\x1a\x1c.payment.PaymentListResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'payment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PAYMENTREQUEST']._serialized_start=26
  _globals['_PAYMENTREQUEST']._serialized_end=56
  _globals['_PAYMENTRESPONSE']._serialized_start=58
  _globals['_PAYMENTRESPONSE']._serialized_end=127
  _globals['_PAYMENTLISTRESPONSE']._serialized_start=129
  _globals['_PAYMENTLISTRESPONSE']._serialized_end=194
  _globals['_EMPTY']._serialized_start=196
  _globals['_EMPTY']._serialized_end=203
  _globals['_PAYMENTSERVICE']._serialized_start=206
  _globals['_PAYMENTSERVICE']._serialized_end=358
# @@protoc_insertion_point(module_scope)