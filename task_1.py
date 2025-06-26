from typing import Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Вставка на початок списку
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Вставка в кінець списку
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Вставка після заданого вузла
    def insert_after(self, prev_node: Optional[Node], data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Видалення вузла за значенням
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    # Пошук вузла за значенням
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Друк елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # ✅ 1. Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # ✅ 2. Допоміжна: пошук середини списку
    def _get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # ✅ 2. Допоміжна: злиття двох відсортованих списків
    def _sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)
        return result

    # ✅ 2. Сортування злиттям (merge sort)
    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return self._sorted_merge(left, right)

    # Основна функція сортування
    def sort(self):
        self.head = self._merge_sort(self.head)

    # ✅ 3. Об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy
        a = list1.head
        b = list2.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b

        merged = LinkedList()
        merged.head = dummy.next
        return merged


# Створюємо список
llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("📋 Початковий список:")
llist.print_list()

llist.reverse()
print("\n🔁 Реверсований список:")
llist.print_list()

# Сортування
llist.sort()
print("\n📊 Відсортований список:")
llist.print_list()

# Об'єднання двох відсортованих списків
list1 = LinkedList()
list2 = LinkedList()
for x in [1, 4, 7]:
    list1.insert_at_end(x)
for y in [2, 3, 6, 9]:
    list2.insert_at_end(y)

merged = LinkedList.merge_sorted_lists(list1, list2)
print("\n🔗 Об'єднаний відсортований список:")
merged.print_list()
