# SlotLevel Object

```text
Slot level object for order priority values. This was mean if
you implement this slot level object to attribute on your class
and update level to an instance when it has some action, it will
be make the level more than another instance.

:param level: a level number of this slot instance.
:type level: int

Attributes:
    * level: int
        A number of level that represent n-layer of this instance.
    * slot: List[bool]
        A list of boolean that have index equal the level attribute.
    * count: int
        A counting number of True value in the slot.
    * value: int
        A sum of weighted value from a True value in any slot position.

Methods:
    * update: [Optional[Union[int, TupleInt]]] -> SlotLevel
        Self that was updated level
    * checker: [Union[int, TupleInt]] -> bool
        A True if all values in ``self.slot`` that match with index numbers
        are True.

Static-methods:
    * make_tuple: [Union[int, TupleInt]] -> TupleInt
        A tuple of integer value that was created from input.
```
