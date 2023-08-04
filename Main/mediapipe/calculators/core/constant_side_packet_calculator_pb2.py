# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/constant_side_packet_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.framework.formats import classification_pb2 as mediapipe_dot_framework_dot_formats_dot_classification__pb2
from mediapipe.framework.formats import landmark_pb2 as mediapipe_dot_framework_dot_formats_dot_landmark__pb2
from mediapipe.framework.formats import time_series_header_pb2 as mediapipe_dot_framework_dot_formats_dot_time__series__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@mediapipe/calculators/core/constant_side_packet_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x30mediapipe/framework/formats/classification.proto\x1a*mediapipe/framework/formats/landmark.proto\x1a\x34mediapipe/framework/formats/time_series_header.proto\"\xbe\x04\n#ConstantSidePacketCalculatorOptions\x12Q\n\x06packet\x18\x01 \x03(\x0b\x32\x41.mediapipe.ConstantSidePacketCalculatorOptions.ConstantSidePacket\x1a\xe4\x02\n\x12\x43onstantSidePacket\x12\x13\n\tint_value\x18\x01 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x02 \x01(\x02H\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12\x16\n\x0cuint64_value\x18\x05 \x01(\x04H\x00\x12\x42\n\x19\x63lassification_list_value\x18\x06 \x01(\x0b\x32\x1d.mediapipe.ClassificationListH\x00\x12\x36\n\x13landmark_list_value\x18\x07 \x01(\x0b\x32\x17.mediapipe.LandmarkListH\x00\x12\x16\n\x0c\x64ouble_value\x18\t \x01(\x01H\x00\x12?\n\x18time_series_header_value\x18\n \x01(\x0b\x32\x1b.mediapipe.TimeSeriesHeaderH\x00\x42\x07\n\x05value2]\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x85\xaa\xee\x8a\x01 \x01(\x0b\x32..mediapipe.ConstantSidePacketCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.core.constant_side_packet_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_CONSTANTSIDEPACKETCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _globals['_CONSTANTSIDEPACKETCALCULATOROPTIONS']._serialized_start=266
  _globals['_CONSTANTSIDEPACKETCALCULATOROPTIONS']._serialized_end=840
  _globals['_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET']._serialized_start=389
  _globals['_CONSTANTSIDEPACKETCALCULATOROPTIONS_CONSTANTSIDEPACKET']._serialized_end=745
# @@protoc_insertion_point(module_scope)
