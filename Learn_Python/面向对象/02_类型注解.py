import random
from typing import Union

# 类型注解 编译器并不检查？？？奇怪 那还要干嘛
var_1: int = 1
var_2: float = 1.1
var_3: bool = True
var_4: str = "jjj"
# list tuple dict set 也可以是自定义类型
# dict[str, int] list[int] list[int, str]

var_5 = random.randint(1, 10)  # type: int

test_dict: dict[str, Union[str, int]] = {
	"name": "lll",
	"age": 18
}


def test(msg: str) -> None:
	print(msg)


test("hhh")
test("hhhhhh")
