# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/audio/rational_factor_resample_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEmediapipe/calculators/audio/rational_factor_resample_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xac\x03\n\'RationalFactorResampleCalculatorOptions\x12\x1a\n\x12target_sample_rate\x18\x01 \x01(\x01\x12|\n!resampler_rational_factor_options\x18\x02 \x01(\x0b\x32Q.mediapipe.RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions\x12+\n\x1d\x63heck_inconsistent_timestamps\x18\x03 \x01(\x08:\x04true\x1aX\n\x1eResamplerRationalFactorOptions\x12\x0e\n\x06radius\x18\x01 \x01(\x01\x12\x0e\n\x06\x63utoff\x18\x02 \x01(\x01\x12\x16\n\x0bkaiser_beta\x18\x03 \x01(\x01:\x01\x36\x32`\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xca\xbf\xee{ \x01(\x0b\x32\x32.mediapipe.RationalFactorResampleCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.audio.rational_factor_resample_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_RATIONALFACTORRESAMPLECALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _globals['_RATIONALFACTORRESAMPLECALCULATOROPTIONS']._serialized_start=123
  _globals['_RATIONALFACTORRESAMPLECALCULATOROPTIONS']._serialized_end=551
  _globals['_RATIONALFACTORRESAMPLECALCULATOROPTIONS_RESAMPLERRATIONALFACTOROPTIONS']._serialized_start=365
  _globals['_RATIONALFACTORRESAMPLECALCULATOROPTIONS_RESAMPLERRATIONALFACTOROPTIONS']._serialized_end=453
# @@protoc_insertion_point(module_scope)
