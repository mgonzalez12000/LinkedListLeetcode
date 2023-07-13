def mergeTwoLists(lst1 , lst2):
    dummy = ListNode()
    tail = dummy

    while lst1 != None and lst2 != None:
        if lst1.val < lst2.val:
            tail.next = lst1
            lst1 = lst1.next
        else:
            tail.next = lst2
            lst2 = lst2.next
    if lst1 != None:
        lst1 = lst1.next
    elif lst2 != None:
        lst2 = lst2.next
    return dummy.next