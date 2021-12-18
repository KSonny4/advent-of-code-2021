from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Union, Any


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
    with open("input.txt", encoding="utf-8") as f:
        packet = f.read().strip()
    print(packet)

    bits = bin(int("1" + packet, 16))[3:]

    parsed_bites = parse_packet(bits, [])
    print(parsed_bites)

    print(VERSIONS_SUM)


if __name__ == "__main__":
    main()
