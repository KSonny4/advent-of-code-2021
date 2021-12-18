from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Union, Any
import math

from pprint import pprint

VERSIONS_SUM = 0


class TypeID(Enum):
    LITERAL_VALUE = 4


@dataclass
class LiteralValue:
    packet_version: int
    packet_type_id: int
    parts: List[str]
    decimal: int


@dataclass
class OperatorPacket:
    packet_version: int
    packet_type_id: int
    length_type_id: int
    length: int
    packets: List[Any]
    value: int


def parse_literal_value_recursive(bits: str, vals: List[str]) -> Tuple[List[str], str]:
    if bits[0] == "1":
        return parse_literal_value_recursive(bits[5:], vals + [bits[1:5]])
    vals += [bits[1:5]]
    return vals, bits[5:]


def parse_literal_value(bits: str) -> Tuple[LiteralValue, str]:
    global VERSIONS_SUM

    version = int(bits[0:3], 2)
    VERSIONS_SUM += version
    type_id = int(bits[3:6], 2)

    bits_without_header = bits[6:]
    parsed_literal_value, rest_bites = parse_literal_value_recursive(
        bits_without_header, []
    )
    return (
        LiteralValue(
            packet_version=version,
            packet_type_id=type_id,
            parts=parsed_literal_value,
            decimal=int("".join(parsed_literal_value), 2),
        ),
        rest_bites,
    )


def compute(val, type_id):
    if type_id == 0:
        return sum(val)
    elif type_id == 1:
        return math.prod(val)
    elif type_id == 2:
        return min(val)
    elif type_id == 3:
        return max(val)
    elif type_id == 5:
        return int(val[0] > val[1])
    elif type_id == 6:
        return int(val[0] < val[1])
    elif type_id == 7:
        return int(val[0] == val[1])
    else:
        raise Exception("Something went wrong.")


def calculate(packets, type_id, lst):

    literals = [x.decimal for x in packets if isinstance(x, LiteralValue)]
    operations = [x for x in packets if isinstance(x, OperatorPacket)]
    normal_vals = [x for x in lst if isinstance(x, int)] + [
        x.value for x in packets if isinstance(x, OperatorPacket)
    ]

    if operations:
        a = [calculate(x.packets, x.packet_type_id, lst) for x in operations]
        return compute(a + normal_vals, type_id)

    # Problem is reduced to only Ints, cmpute
    if literals and not operations:
        return compute(literals + normal_vals, type_id)
    # return calculate(operations,  type_id, 0,  lst + [normal_vals])

    return compute(normal_vals, type_id)

    # #return compute()
    #
    # if all(isinstance(x, LiteralValue) for x in packets):
    #     return compute([x.decimal for x in packets], type_id)
    # operations = []
    # for packet in packets:
    #     if isinstance(packet, OperatorPacket):
    #         operations.append(calculate(packet.packets, packet.packet_type_id, [])
    #     #elif isinstance(packet, LiteralValue):
    #     #    val.append(packet)
    #     else:
    #         raise Exception("Unknown object")


def parse_operator(bits):
    global VERSIONS_SUM
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)

    VERSIONS_SUM += version

    length = -1
    new_bits = ""
    if bits[6] == "0":
        length = int(bits[7:22], 2)
        new_bits = bits[22:]

    if bits[6] == "1":
        length = int(bits[7:18], 2)
        new_bits = bits[18:]

    if length == -1:
        raise Exception("Could not parse length properly.")

    parsed_packet = parse_packet(new_bits, [])

    return (
        OperatorPacket(
            packet_version=version,
            packet_type_id=type_id,
            length_type_id=int(bits[6]),
            length=length,
            packets=parsed_packet,
            value=calculate(parsed_packet, type_id, []),
        ),
        "",
    )


def parse_packet(bits, values):
    if len(bits) < 4 or set(x for x in bits) == {"0"}:
        return values

    type_id = int(bits[3:6], 2)

    if type_id == TypeID.LITERAL_VALUE.value:
        parsed_bites, rest = parse_literal_value(bits)
    else:
        parsed_bites, rest = parse_operator(bits)

    return parse_packet(rest, values + [parsed_bites])


def main():
    with open("input3.txt", encoding="utf-8") as f:
        packet = f.read().strip()
    print(packet)

    bits = bin(int("1" + packet, 16))[3:]

    parsed_bites = parse_packet(bits, [])
    pprint(parsed_bites)

    print(f"Part 1: {VERSIONS_SUM}")

    print(f"Part 2: {parsed_bites[0].value}")


if __name__ == "__main__":
    main()
