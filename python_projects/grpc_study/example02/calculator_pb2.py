# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calculator.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'calculator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"I\n\x0e\x43omputeRequest\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\x12!\n\x02op\x18\x03 \x01(\x0e\x32\x15.calculator.Operation\"\x1e\n\x0c\x43omputeReply\x12\x0e\n\x06result\x18\x01 \x01(\x05*\"\n\tOperation\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\x0c\n\x08MULTIPLY\x10\x01\x32O\n\nCalculator\x12\x41\n\x07\x43ompute\x12\x1a.calculator.ComputeRequest\x1a\x18.calculator.ComputeReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OPERATION']._serialized_start=139
  _globals['_OPERATION']._serialized_end=173
  _globals['_COMPUTEREQUEST']._serialized_start=32
  _globals['_COMPUTEREQUEST']._serialized_end=105
  _globals['_COMPUTEREPLY']._serialized_start=107
  _globals['_COMPUTEREPLY']._serialized_end=137
  _globals['_CALCULATOR']._serialized_start=175
  _globals['_CALCULATOR']._serialized_end=254
# @@protoc_insertion_point(module_scope)
