# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_inventory.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import steammessages_unified_base_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_inventory.proto',
  package='',
  serialized_pb='\n\x1dsteammessages_inventory.proto\x1a steammessages_unified_base.proto\"A\n\x1f\x43Inventory_GetInventory_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\"t\n\x13\x43Inventory_Response\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x16\n\x0eremoveditemids\x18\x02 \x03(\x04\x12\x11\n\titem_json\x18\x03 \x01(\t\x12\x14\n\x0citemdef_json\x18\x04 \x01(\t\x12\x0e\n\x06ticket\x18\x05 \x01(\x0c\"\x8e\x01\n\x1f\x43Inventory_ExchangeItem_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\x12\x17\n\x0fmaterialsitemid\x18\x03 \x03(\x04\x12\x19\n\x11materialsquantity\x18\x04 \x03(\r\x12\x17\n\x0foutputitemdefid\x18\x05 \x01(\x04\"f\n\x1a\x43Inventory_AddItem_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\titemdefid\x18\x02 \x03(\x04\x12\x15\n\ritempropsjson\x18\x03 \x03(\t\x12\x0f\n\x07steamid\x18\x04 \x01(\x04\"i\n!CInventory_SafeModifyItem_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0e\n\x06\x61\x63\x63tid\x18\x02 \x01(\x04\x12\x0e\n\x06itemid\x18\x03 \x01(\x04\x12\x15\n\ritempropsjson\x18\x04 \x01(\t\"F\n\"CInventory_ConsumePlaytime_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\titemdefid\x18\x02 \x01(\x04\"\xdb\x01\n\x1e\x43Inventory_GetItemDefs_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x15\n\rmodifiedsince\x18\x02 \x01(\t\x12\x12\n\nitemdefids\x18\x04 \x03(\x04\x12\x13\n\x0bworkshopids\x18\x05 \x03(\x04\x12j\n\x15\x63\x61\x63he_max_age_seconds\x18\x07 \x01(\r:\x01\x30\x42H\x82\xb5\x18\x44\x41llow stale data to be returned for the specified number of seconds.\"d\n\x1e\x43Inventory_ConsumeItem_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0e\n\x06itemid\x18\x02 \x01(\x04\x12\x10\n\x08quantity\x18\x03 \x01(\r\x12\x11\n\ttimestamp\x18\x04 \x01(\t\"W\n!CInventory_DevSetNextDrop_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\titemdefid\x18\x02 \x01(\x04\x12\x10\n\x08\x64roptime\x18\x03 \x01(\t\"g\n!CInventory_SplitItemStack_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0e\n\x06itemid\x18\x02 \x01(\x04\x12\x10\n\x08quantity\x18\x03 \x01(\r\x12\x11\n\ttimestamp\x18\x04 \x01(\t\"\x9d\x01\n$CInventory_CombineItemStacks_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x12\n\nfromitemid\x18\x02 \x01(\x04\x12\x12\n\ndestitemid\x18\x03 \x01(\x04\x12\x10\n\x08quantity\x18\x04 \x01(\r\x12\x15\n\rfromtimestamp\x18\x05 \x01(\t\x12\x15\n\rdesttimestamp\x18\x06 \x01(\t2\xa5\n\n\tInventory\x12z\n\x0cGetInventory\x12 .CInventory_GetInventory_Request\x1a\x14.CInventory_Response\"2\x82\xb5\x18.Retrieves a users inventory as a big JSON blob\x12o\n\x0c\x45xchangeItem\x12 .CInventory_ExchangeItem_Request\x1a\x14.CInventory_Response\"\'\x82\xb5\x18#Craft an item in a user\'s inventory\x12n\n\x0c\x41\x64\x64PromoItem\x12\x1b.CInventory_AddItem_Request\x1a\x14.CInventory_Response\"+\x82\xb5\x18\'Adds a promo item to a user\'s inventory\x12\x8b\x01\n\x0eSafeModifyItem\x12\".CInventory_SafeModifyItem_Request\x1a\x14.CInventory_Response\"?\x82\xb5\x18;Modify an item in a user\'s inventory (safe properties only)\x12\x87\x01\n\x0f\x43onsumePlaytime\x12#.CInventory_ConsumePlaytime_Request\x1a\x14.CInventory_Response\"9\x82\xb5\x18\x35\x43onsumes playtime and possibly returns a granted item\x12^\n\x0bGetItemDefs\x12\x1f.CInventory_GetItemDefs_Request\x1a\x14.CInventory_Response\"\x18\x82\xb5\x18\x14Get item definitions\x12Y\n\x0b\x43onsumeItem\x12\x1f.CInventory_ConsumeItem_Request\x1a\x14.CInventory_Response\"\x13\x82\xb5\x18\x0f\x43onsume an item\x12n\n\x0f\x44\x65vGenerateItem\x12\x1b.CInventory_AddItem_Request\x1a\x14.CInventory_Response\"(\x82\xb5\x18$Grant an item when in developer mode\x12_\n\x0e\x44\x65vSetNextDrop\x12\".CInventory_DevSetNextDrop_Request\x1a\x14.CInventory_Response\"\x13\x82\xb5\x18\x0f\x43onsume an item\x12s\n\x0eSplitItemStack\x12\".CInventory_SplitItemStack_Request\x1a\x14.CInventory_Response\"\'\x82\xb5\x18#Split an item stack into two stacks\x12q\n\x11\x43ombineItemStacks\x12%.CInventory_CombineItemStacks_Request\x1a\x14.CInventory_Response\"\x1f\x82\xb5\x18\x1b\x43ombine two stacks of items\x1a/\x82\xb5\x18+A service that provides access to inventoryB\x03\x90\x01\x01')




_CINVENTORY_GETINVENTORY_REQUEST = _descriptor.Descriptor(
  name='CInventory_GetInventory_Request',
  full_name='CInventory_GetInventory_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_GetInventory_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CInventory_GetInventory_Request.steamid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=67,
  serialized_end=132,
)


_CINVENTORY_RESPONSE = _descriptor.Descriptor(
  name='CInventory_Response',
  full_name='CInventory_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='etag', full_name='CInventory_Response.etag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='removeditemids', full_name='CInventory_Response.removeditemids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_json', full_name='CInventory_Response.item_json', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemdef_json', full_name='CInventory_Response.itemdef_json', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ticket', full_name='CInventory_Response.ticket', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=134,
  serialized_end=250,
)


_CINVENTORY_EXCHANGEITEM_REQUEST = _descriptor.Descriptor(
  name='CInventory_ExchangeItem_Request',
  full_name='CInventory_ExchangeItem_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_ExchangeItem_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CInventory_ExchangeItem_Request.steamid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='materialsitemid', full_name='CInventory_ExchangeItem_Request.materialsitemid', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='materialsquantity', full_name='CInventory_ExchangeItem_Request.materialsquantity', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputitemdefid', full_name='CInventory_ExchangeItem_Request.outputitemdefid', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=253,
  serialized_end=395,
)


_CINVENTORY_ADDITEM_REQUEST = _descriptor.Descriptor(
  name='CInventory_AddItem_Request',
  full_name='CInventory_AddItem_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_AddItem_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemdefid', full_name='CInventory_AddItem_Request.itemdefid', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itempropsjson', full_name='CInventory_AddItem_Request.itempropsjson', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CInventory_AddItem_Request.steamid', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=397,
  serialized_end=499,
)


_CINVENTORY_SAFEMODIFYITEM_REQUEST = _descriptor.Descriptor(
  name='CInventory_SafeModifyItem_Request',
  full_name='CInventory_SafeModifyItem_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_SafeModifyItem_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acctid', full_name='CInventory_SafeModifyItem_Request.acctid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemid', full_name='CInventory_SafeModifyItem_Request.itemid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itempropsjson', full_name='CInventory_SafeModifyItem_Request.itempropsjson', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=501,
  serialized_end=606,
)


_CINVENTORY_CONSUMEPLAYTIME_REQUEST = _descriptor.Descriptor(
  name='CInventory_ConsumePlaytime_Request',
  full_name='CInventory_ConsumePlaytime_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_ConsumePlaytime_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemdefid', full_name='CInventory_ConsumePlaytime_Request.itemdefid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=608,
  serialized_end=678,
)


_CINVENTORY_GETITEMDEFS_REQUEST = _descriptor.Descriptor(
  name='CInventory_GetItemDefs_Request',
  full_name='CInventory_GetItemDefs_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_GetItemDefs_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modifiedsince', full_name='CInventory_GetItemDefs_Request.modifiedsince', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemdefids', full_name='CInventory_GetItemDefs_Request.itemdefids', index=2,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workshopids', full_name='CInventory_GetItemDefs_Request.workshopids', index=3,
      number=5, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cache_max_age_seconds', full_name='CInventory_GetItemDefs_Request.cache_max_age_seconds', index=4,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030DAllow stale data to be returned for the specified number of seconds.')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=681,
  serialized_end=900,
)


_CINVENTORY_CONSUMEITEM_REQUEST = _descriptor.Descriptor(
  name='CInventory_ConsumeItem_Request',
  full_name='CInventory_ConsumeItem_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_ConsumeItem_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemid', full_name='CInventory_ConsumeItem_Request.itemid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='CInventory_ConsumeItem_Request.quantity', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='CInventory_ConsumeItem_Request.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=902,
  serialized_end=1002,
)


_CINVENTORY_DEVSETNEXTDROP_REQUEST = _descriptor.Descriptor(
  name='CInventory_DevSetNextDrop_Request',
  full_name='CInventory_DevSetNextDrop_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_DevSetNextDrop_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemdefid', full_name='CInventory_DevSetNextDrop_Request.itemdefid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='droptime', full_name='CInventory_DevSetNextDrop_Request.droptime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1004,
  serialized_end=1091,
)


_CINVENTORY_SPLITITEMSTACK_REQUEST = _descriptor.Descriptor(
  name='CInventory_SplitItemStack_Request',
  full_name='CInventory_SplitItemStack_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_SplitItemStack_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemid', full_name='CInventory_SplitItemStack_Request.itemid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='CInventory_SplitItemStack_Request.quantity', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='CInventory_SplitItemStack_Request.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1093,
  serialized_end=1196,
)


_CINVENTORY_COMBINEITEMSTACKS_REQUEST = _descriptor.Descriptor(
  name='CInventory_CombineItemStacks_Request',
  full_name='CInventory_CombineItemStacks_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CInventory_CombineItemStacks_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromitemid', full_name='CInventory_CombineItemStacks_Request.fromitemid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destitemid', full_name='CInventory_CombineItemStacks_Request.destitemid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='CInventory_CombineItemStacks_Request.quantity', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromtimestamp', full_name='CInventory_CombineItemStacks_Request.fromtimestamp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desttimestamp', full_name='CInventory_CombineItemStacks_Request.desttimestamp', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1199,
  serialized_end=1356,
)

DESCRIPTOR.message_types_by_name['CInventory_GetInventory_Request'] = _CINVENTORY_GETINVENTORY_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_Response'] = _CINVENTORY_RESPONSE
DESCRIPTOR.message_types_by_name['CInventory_ExchangeItem_Request'] = _CINVENTORY_EXCHANGEITEM_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_AddItem_Request'] = _CINVENTORY_ADDITEM_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_SafeModifyItem_Request'] = _CINVENTORY_SAFEMODIFYITEM_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_ConsumePlaytime_Request'] = _CINVENTORY_CONSUMEPLAYTIME_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_GetItemDefs_Request'] = _CINVENTORY_GETITEMDEFS_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_ConsumeItem_Request'] = _CINVENTORY_CONSUMEITEM_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_DevSetNextDrop_Request'] = _CINVENTORY_DEVSETNEXTDROP_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_SplitItemStack_Request'] = _CINVENTORY_SPLITITEMSTACK_REQUEST
DESCRIPTOR.message_types_by_name['CInventory_CombineItemStacks_Request'] = _CINVENTORY_COMBINEITEMSTACKS_REQUEST

class CInventory_GetInventory_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_GETINVENTORY_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_GetInventory_Request)

class CInventory_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_RESPONSE

  # @@protoc_insertion_point(class_scope:CInventory_Response)

class CInventory_ExchangeItem_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_EXCHANGEITEM_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_ExchangeItem_Request)

class CInventory_AddItem_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_ADDITEM_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_AddItem_Request)

class CInventory_SafeModifyItem_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_SAFEMODIFYITEM_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_SafeModifyItem_Request)

class CInventory_ConsumePlaytime_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_CONSUMEPLAYTIME_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_ConsumePlaytime_Request)

class CInventory_GetItemDefs_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_GETITEMDEFS_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_GetItemDefs_Request)

class CInventory_ConsumeItem_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_CONSUMEITEM_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_ConsumeItem_Request)

class CInventory_DevSetNextDrop_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_DEVSETNEXTDROP_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_DevSetNextDrop_Request)

class CInventory_SplitItemStack_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_SPLITITEMSTACK_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_SplitItemStack_Request)

class CInventory_CombineItemStacks_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CINVENTORY_COMBINEITEMSTACKS_REQUEST

  # @@protoc_insertion_point(class_scope:CInventory_CombineItemStacks_Request)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')
_CINVENTORY_GETITEMDEFS_REQUEST.fields_by_name['cache_max_age_seconds'].has_options = True
_CINVENTORY_GETITEMDEFS_REQUEST.fields_by_name['cache_max_age_seconds']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030DAllow stale data to be returned for the specified number of seconds.')

_INVENTORY = _descriptor.ServiceDescriptor(
  name='Inventory',
  full_name='Inventory',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), '\202\265\030+A service that provides access to inventory'),
  serialized_start=1359,
  serialized_end=2676,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetInventory',
    full_name='Inventory.GetInventory',
    index=0,
    containing_service=None,
    input_type=_CINVENTORY_GETINVENTORY_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030.Retrieves a users inventory as a big JSON blob'),
  ),
  _descriptor.MethodDescriptor(
    name='ExchangeItem',
    full_name='Inventory.ExchangeItem',
    index=1,
    containing_service=None,
    input_type=_CINVENTORY_EXCHANGEITEM_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030#Craft an item in a user\'s inventory'),
  ),
  _descriptor.MethodDescriptor(
    name='AddPromoItem',
    full_name='Inventory.AddPromoItem',
    index=2,
    containing_service=None,
    input_type=_CINVENTORY_ADDITEM_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030\'Adds a promo item to a user\'s inventory'),
  ),
  _descriptor.MethodDescriptor(
    name='SafeModifyItem',
    full_name='Inventory.SafeModifyItem',
    index=3,
    containing_service=None,
    input_type=_CINVENTORY_SAFEMODIFYITEM_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030;Modify an item in a user\'s inventory (safe properties only)'),
  ),
  _descriptor.MethodDescriptor(
    name='ConsumePlaytime',
    full_name='Inventory.ConsumePlaytime',
    index=4,
    containing_service=None,
    input_type=_CINVENTORY_CONSUMEPLAYTIME_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\0305Consumes playtime and possibly returns a granted item'),
  ),
  _descriptor.MethodDescriptor(
    name='GetItemDefs',
    full_name='Inventory.GetItemDefs',
    index=5,
    containing_service=None,
    input_type=_CINVENTORY_GETITEMDEFS_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030\024Get item definitions'),
  ),
  _descriptor.MethodDescriptor(
    name='ConsumeItem',
    full_name='Inventory.ConsumeItem',
    index=6,
    containing_service=None,
    input_type=_CINVENTORY_CONSUMEITEM_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030\017Consume an item'),
  ),
  _descriptor.MethodDescriptor(
    name='DevGenerateItem',
    full_name='Inventory.DevGenerateItem',
    index=7,
    containing_service=None,
    input_type=_CINVENTORY_ADDITEM_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030$Grant an item when in developer mode'),
  ),
  _descriptor.MethodDescriptor(
    name='DevSetNextDrop',
    full_name='Inventory.DevSetNextDrop',
    index=8,
    containing_service=None,
    input_type=_CINVENTORY_DEVSETNEXTDROP_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030\017Consume an item'),
  ),
  _descriptor.MethodDescriptor(
    name='SplitItemStack',
    full_name='Inventory.SplitItemStack',
    index=9,
    containing_service=None,
    input_type=_CINVENTORY_SPLITITEMSTACK_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030#Split an item stack into two stacks'),
  ),
  _descriptor.MethodDescriptor(
    name='CombineItemStacks',
    full_name='Inventory.CombineItemStacks',
    index=10,
    containing_service=None,
    input_type=_CINVENTORY_COMBINEITEMSTACKS_REQUEST,
    output_type=_CINVENTORY_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030\033Combine two stacks of items'),
  ),
])

class Inventory(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _INVENTORY
class Inventory_Stub(Inventory):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _INVENTORY

# @@protoc_insertion_point(module_scope)
