from data_structures.queue import Queue

def test_queue():
    q = Queue()

    # 1️⃣ Empty queue
    assert q.is_empty()
    assert q.peek_front() is None
    assert q.head is None
    assert q.tail is None

    # 2️⃣ Enqueue into empty → [10]
    q.enqueue(10)
    assert not q.is_empty()
    assert q.peek_front() == 10
    assert q.head.data == 10
    assert q.tail.data == 10
    assert q.head.next is None

    # 3️⃣ Enqueue more → [10, 20, 30]
    q.enqueue(20)
    q.enqueue(30)
    assert q.peek_front() == 10
    assert q.head.data == 10
    assert q.head.next.data == 20
    assert q.tail.data == 30
    assert q.tail.next is None

    # 4️⃣ Dequeue → removes 10 → [20, 30]
    removed = q.dequeue()
    assert removed == 10
    assert q.peek_front() == 20
    assert not q.is_empty()

    # 5️⃣ Dequeue again → removes 20 → [30]
    removed = q.dequeue()
    assert removed == 20
    assert q.peek_front() == 30
    assert not q.is_empty()

    # 6️⃣ Dequeue last → removes 30 → []
    removed = q.dequeue()
    assert removed == 30
    assert q.is_empty()
    assert q.peek_front() is None

    # 7️⃣ Dequeue on empty (no crash)
    removed = q.dequeue()
    assert removed is None
    assert q.is_empty()

    # 8️⃣ Enqueue again after empty → [99]
    q.enqueue(99)
    assert not q.is_empty()
    assert q.peek_front() == 99
    assert q.head.data == 99
    assert q.tail.data == 99
    assert q.head.next is None

    print("✅ All Queue tests passed successfully!")

if __name__ == "__main__":
    test_queue()