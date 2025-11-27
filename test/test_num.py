from num import evn

def test_evn():
    assert evn(2) == 1    # 2 is even → 1
    assert evn(4) == 1    # even number
    assert evn(1) == 0    # odd number → 0
    assert evn(7) == 0    # odd number
