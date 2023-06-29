class Node:
    # Contructor 
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):  
        self.head = None
        self.tail = None
    def addFirst(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            newNode.next = current
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
    def addLast(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            last_node = self.tail
            last_node.next = newnode
            self.tail = newnode
    def addPos(self, pos, data):
        if pos <=0 : return
        if pos == 1:
            # print("xxx")
            self.addFirst(data)
        id = 0
        newNode = Node(data)
        current = self.head
        # print(current.next)
        while id < pos-2:
            current = current.next
            id+=1
        # id-=1
        next_node = current.next
        current.next = newNode
        newNode.next = next_node
    def addMany(self, arr):
        for i in arr:
            self.addFirst(i)
            
    def isEmpty(self):
        if self.head == None: return True
       
        else: return False
        
    def size(self):
        xp = self.head
        cnt = 0
        while xp != None:
            xp = xp.next
            cnt+=1
        return cnt
    def get(self, pos):
        pos-=1
        px = self.head
        if pos >= 0 and self.size() > pos:
            i = 0
            while i < pos:
                px = px.next
                i+=1
            return px.data
        else:
            return "Pos khong hop le!"
    def indexOf(self, el):
        px = self.head
        i = 0 
        while px != None:
            if px.data is el:
                return i+1
            px = px.next
            i+=1
        return "Khong ton tai"
    def removeFirst(self):
        px = self.head
        n = self.size()
        if n == 1:
            self.head = None
            self.tail = None
        if self.head:
            self.head =px.next
            px = None
    def  removeLast(self):
        px = self.head
        n = self.size()
        if n == 1:
            self.head = None
            self.tail = None
        if px:
            i = 0
            # print(n)
            while i < n-2:
                px = px.next
                i+=1
            # print(i)
            px.next = None
            self.tail = None
            self.tail = px
    def removeAll(self):

        n = self.size()
        i = 0
        while i < n:
            self.removeFirst()
            i+=1
                
        
    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    sll = SLL()

    print('''
    BANG TINH NANG
    1. isEmpty
    2. addFirst
    3. addLast
    4. addPos
    5. addMany
    6. size
    7. get
    8. indexOf
    9. removeFirst
    10. removeLast
    11. removeAll
    12. Print ALL
    0. EXIT
    ''')
    while True:
        n = int(input("Nhap select: "))
        if n == 0 : break
        if n == 1:
            if sll.isEmpty():
                print("Not node exit !")
            else : print("Node exit !")
        if n == 2:
            x = int(input("Nhap phan tu: "));
            sll.addFirst(x)
        if n == 3:
            x = int(input("Nhap phan tu: "));
            sll.addLast(x)
        if n == 4:
            x = int(input("Nhap phan tu: "));
            pos  = int(input("Nhap vi tri phan tu: "));
            sll.addPos(pos, x)
        if n == 5:
            arr = [1, 5, 6, 2, 3]
            sll.addMany(arr)
        if n == 6:
            x = sll.size()
            print(f'Kich thuoc linklistL: {x}')
        if n == 7:
            pos  = int(input("Nhap vi tri phan tu: "));
            x = sll.get(pos)
            print(f'arr[{pos}] = {x}')
        if n == 8:
            x = int(input("Nhap phan tu: "));
            vl = sll.indexOf(x)
            print(f'Phan tu co gia tri {x} xuat hien o pos = {vl}')
        if n == 9:
            sll.removeFirst()
        if n == 10:
            sll.removeLast()
        if n == 11:
            sll.removeAll()
        if n == 12:
            sll.printLL()