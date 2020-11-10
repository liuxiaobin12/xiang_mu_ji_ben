
from Base.data import Data

import pytest,logging


def value():
    """组装json数据"""
    # 存储测试数据列表
    data_list = []
    # 读取数据
    data = Data.get_json_data("sum.json")

    # 遍历数据
    for i in data:
        data_list.append((i.get("a"), i.get("b"), i.get("c"), i.get("desc")))

    return data_list


class TestSum:

    @pytest.mark.parametrize("a,b,c,desc", value())
    def test_sum(self, a, b, c, desc):
        """
        加法计算 a+b == c
        """
        logging.info("用例类型:{}".format(desc))
        logging.info("{}+{}=={}".format(a, b, c))
        # 断言
        assert a+b == c
