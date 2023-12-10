from pydantic import validate_call


@validate_call
def soma(x: int, y: int) -> int:
    return x + y


if __name__ == '__main__':
    print(soma(3, 2)) #5
    print(soma(3, ''))

# ValidationError: 2 validation errors for soma
# 0
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.5/v/int_parsing
# 1
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.5/v/int_parsing