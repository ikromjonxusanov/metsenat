def parse_phone_number(number: str) -> str:
    return f"+998{number[:2]} {number[2:5]}-{number[5:7]}-{number[7:9]}"
