# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 5 /σελίδα 151
Να γράψετε ένα πρόγραμμα το οποίο θα διαβάζει αριθμούς από το πληκτρολόγιο,
μέχρι να δοθεί ο αριθμός 0. Κάθε φορά που θα διαβάζει έναν θετικό αριθμό, θα τον
προσθέτει σε μια στοίβα. Όταν διαβάζει έναν αρνητικό αριθμό θα αφαιρεί τόσους
αριθμούς από τη στοίβα, όσο είναι η τιμή του αριθμού. Ο αλγόριθμος θα τερματίζει
όταν αδειάσει η στοίβα.

'''
# ή όταν δοθεί ο αριθμός 0 μηδέν

stack = []

# Βασικές λειτουργίες στοίβας
def push(stack, item) :
    stack.append(item)
    return stack

def pop(stack) :
    return stack.pop()

def isEmpty(stack) :
    return len(stack) == 0

# Εισαγωγή 1ου θετικού ακέραιου με έλεγχο δεδομένων
num = int(input('Δώσε έναν θετικό ακέραιο αριθμό='))
while num <=0 :
    num = int(input('Δώσε έναν θετικό ακέραιο αριθμό='))
push(stack,num)


# Εισαγωγή υπολοίπων ακεραίων
while num != 0 and len(stack) != 0:
    num = int(input('Δώσε έναν ακέραιο αριθμό=')    )
	# εάν είναι θετικός τότε push
    if num > 0 :
        push(stack,num)
	# εάν είναι αρνητικός 
    elif num < 0 :
		# κάνε έλεγχο εάν έχει στοιχεία η στοίβα
        if len(stack) >= abs(num):
			# και κάνε pop
            for i in range(abs(num)):
                item = pop(stack)
                print item,
        else :
			# Δεν επαρκούν τα στοιχεία που ζητήθηκαν
            print 'Not enough items in stack poping the items left'
			# Κάνε pop μόνο αυτά που έμειναν
            for i in range(len(stack)):
                item = pop(stack)
                print item,
        print  
    print stack

