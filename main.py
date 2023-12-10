from flask import Flask, render_template, request

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_linked_list(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

app = Flask(__name__, static_folder='static')

def merge_sorted_lists(list1, list2):
    dummy = ListNode()  # Dummy node simplifies the code
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Append remaining nodes if one of the lists is not exhausted
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    result_list = LinkedList()
    result_list.head = dummy.next  # Skip the dummy node in the final result
    return result_list

# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def buttons():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle_area', methods=['GET', 'POST'])
def circle_area():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = 3.14159 * (radius**2)
    return render_template('circle_area.html', area=area)

@app.route('/triangle_area', methods=['GET', 'POST'])
def triangle_area():
    area = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area = 0.5 * base * height
    return render_template('triangle_area.html', area=area)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/merged_linked_list', methods=['GET', 'POST'])
def merged_linked_list():
    if request.method == 'POST':
        # Get user input for the linked lists
        input_list1 = request.form.get('inputList1', '')
        input_list2 = request.form.get('inputList2', '')

        # Convert user input to lists
        list1_values = [int(val) for val in input_list1.split(',')]
        list2_values = [int(val) for val in input_list2.split(',')]

        # Create linked lists
        list1 = LinkedList()
        list2 = LinkedList()

        for value in list1_values:
            list1.append(value)

        for value in list2_values:
            list2.append(value)

        # Merge the linked lists
        merged_list = merge_sorted_lists(list1.head, list2.head)

        return render_template('merged_linked_list.html', merged_list=merged_list)

    return render_template('merged_linked_list.html')

if __name__ == "__main__":
    app.run(debug=True)
