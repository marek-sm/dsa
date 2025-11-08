from data_structures.stack import Stack

def test_stack():
    s = Stack()

    # 1️⃣ Empty stack
    assert s.is_empty()
    assert s.head is None

    # 2️⃣ Push into empty stack → [10]
    s.push(10)
    assert not s.is_empty()
    assert s.peek() == 10
    assert s.head.data == 10
    assert s.head.next is None

    # 3️⃣ Push multiple → [30, 20, 10] (top = 30)
    s.push(20)
    s.push(30)
    assert s.peek() == 30
    assert s.head.data == 30
    assert s.head.next.data == 20
    assert s.head.next.next.data == 10
    assert s.head.next.next.next is None

    # 4️⃣ Pop top → [20, 10]
    popped = s.pop()
    assert popped == 30
    assert s.peek() == 20
    assert s.head.data == 20

    # 5️⃣ Pop again → [10]
    popped = s.pop()
    assert popped == 20
    assert s.peek() == 10

    # 6️⃣ Pop last element → []
    popped = s.pop()
    assert popped == 10
    assert s.is_empty()
    assert s.peek() is None

    # 7️⃣ Pop on empty (no crash)
    popped = s.pop()
    assert popped is None
    assert s.is_empty()

    # 8️⃣ Push again after empty → [99]
    s.push(99)
    assert s.peek() == 99
    assert not s.is_empty()

    print("✅ All Stack tests passed successfully!")

if __name__ == "__main__":
    test_stack()