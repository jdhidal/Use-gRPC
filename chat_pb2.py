# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chat.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'chat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\",\n\x0b\x43hatMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\" \n\x0c\x43hatResponse\x12\x10\n\x08response\x18\x01 \x01(\t29\n\x0b\x43hatService\x12*\n\x0bSendMessage\x12\x0c.ChatMessage\x1a\r.ChatResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHATMESSAGE']._serialized_start=14
  _globals['_CHATMESSAGE']._serialized_end=58
  _globals['_CHATRESPONSE']._serialized_start=60
  _globals['_CHATRESPONSE']._serialized_end=92
  _globals['_CHATSERVICE']._serialized_start=94
  _globals['_CHATSERVICE']._serialized_end=151
# @@protoc_insertion_point(module_scope)
