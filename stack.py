class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def gettop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.stack[-1]

    def push(self, link):
        self.stack.append(link)

    def stack_pop(self):
        if self.isEmpty():
            print("Stack is Empty.")
            print("Can't Delete.")
        else:
            deleted_ele = self.stack.pop()
            print(deleted_ele, "got deleted")
            if not self.isEmpty():
                print("redirected to", self.gettop())

    def display(self):
        return self.stack

links_stacks = Stack()

while True:
    print("-" * 60)

    choice = input("Please enter the choice\n1. Visit another link.\n2. Back.\n3. History\n4. Gets latest visited.\n5. Close the browser.\nEnter your choice here: ")

    print("-" * 60)
    try:
        choice = int(choice)

        if choice == 1:
            link = input("Enter the link:")
            if link.startswith("http://") or link.startswith("https://"):
                links_stacks.push(link)
            else:
                print("Please enter a valid link.")
        elif choice == 2:
            links_stacks.stack_pop()
        elif choice == 3:
            history = links_stacks.display()
            print("History:")
            for link in history:
                print(link)
        elif choice == 4:
            visited_latest = links_stacks.gettop()
            print("Latest Visited link:", visited_latest)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a valid choice (1-5) or a website URL.")
