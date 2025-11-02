from data_structures.linked_list import LinkedList

def test_linked_list():
    ll = LinkedList()

    # 1️⃣ Empty list
    assert ll.head is None

    # 2️⃣ Prepend into empty list → [10]
    ll.prepend(10)
    assert ll.head.data == 10
    assert ll.head.next is None

    # 3️⃣ Multiple prepends → [30, 20, 10]
    ll.prepend(20)
    ll.prepend(30)
    assert ll.head.data == 30
    assert ll.head.next.data == 20
    assert ll.head.next.next.data == 10
    assert ll.head.next.next.next is None

    # 4️⃣ Append to end → [30, 20, 10, 40]
    ll.append(40)
    assert ll.head.next.next.next.data == 40
    assert ll.head.next.next.next.next is None

    # 5️⃣ Delete head → [20, 10, 40]
    ll.delete(30)
    assert ll.head.data == 20
    assert ll.head.next.data == 10

    # 6️⃣ Delete middle → [20, 40]
    ll.delete(10)
    assert ll.head.data == 20
    assert ll.head.next.data == 40
    assert ll.head.next.next is None

    # 7️⃣ Delete tail → [20]
    ll.delete(40)
    assert ll.head.data == 20
    assert ll.head.next is None

    # 8️⃣ Delete non-existent value (no crash) → [20]
    ll.delete(999)
    assert ll.head.data == 20
    assert ll.head.next is None

    # 9️⃣ Delete last remaining node → []
    ll.delete(20)
    assert ll.head is None

    # 🔟 Mix prepend + append again → [1, 2, 3]
    ll.prepend(1)
    ll.append(2)
    ll.append(3)
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 3
    assert ll.head.next.next.next is None

    print("✅ All LinkedList tests passed successfully!")



if __name__ == "__main__":
    test_linked_list()