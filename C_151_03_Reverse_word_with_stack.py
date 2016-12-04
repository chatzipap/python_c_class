# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @TasosChatz

'''

ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 3 /σελίδα 151
Να γράψετε ένα πρόγραμμα το οποίο θα διαβάζει μία λέξη και θα την εμφανίζει
αντεστραμμένη, με τη χρήση μιας στοίβας.

'''

word = raw_input('Δώσε μία λέξη να έρθουν τα πάνω κάτω =')

stack = []

# Βασικές λειτουργίες στοίβας
def push(stack, item) :
    stack.append(item)
    return stack

def pop(stack) :
    return stack.pop()

def isEmpty(stack) :
    return len(stack) == 0

# Fill Stack with Letters
for letter in word:
    push(stack, letter)

# Prepare reverse word
wordR =''
while isEmpty(stack) == False :
    letter = pop(stack)
    wordR += letter
print wordR

# Pythonic Way
print word[::-1]
