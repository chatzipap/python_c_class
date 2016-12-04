# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @TasosChatz
'''

ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 6 / σελίδα 89
Να γράψετε ένα πρόγραμμα σε Python το οποίο θα δέχεται μια λίστα με λογικές
τιμές True/False και στη συνέχεια θα καλεί την συνάρτηση του προηγούμενου 
ερωτήματος, ώστε να τοποθετηθούν τα True πριν από τα False. Στη συνέχεια θα 
τοποθετεί τις τιμές αυτές εναλλάξ, δηλαδή True, False, True, False, κλπ, 
εκτελώντας τιςλιγότερες δυνατές συγκρίσεις.

'''

# Διάταξη λογικών τιμών βλ Δρ.5. σελ.89
def orderBooleans(alist):
        i, j, n = 0, 0, len(alist) - 1
        while j <= n:
            if alist[j] > False:
                alist[i], alist[j] = alist[j], alist[i] 
                i += 1
                j += 1
            else:
                j += 1			

# -----------Uncomment for manual input---------------------
### Εισαγωγή λογικών τιμών σε λίστα
##alist = []
##item = input('Enter Values 1=True, 0=False =')
##while item != None :
##    alist.append(item)
##    item = input('Enter Values 1=True, 0=False, None=Stop =')
##print 'Original List=', alist
##----------------------------------------------------------

# ------------------AuTo values-------------------------------
# Δοκιμαστικές κλήσεις και αποτελέσματα
import random
start = 0
end = 21
alist = []
for i in range(start, end):
    alist.append(random.choice([1, 0]))
print 'Original List =', alist
##----------------------------------------------------------

orderBooleans(alist)
print 'Ones(1) before Zeros(0) List=', alist

# Βρες τη θέση εμφάνισης του 1ου False
pos = 0
for item in alist:
    if item == 1 :
        pos += 1
    else :
        break
print 'Change 1-->0 position=', pos, 'Values length=',len(alist)

# Βάλε ενναλάξ τα στοιχεία 0 & 1
j = 1
if alist.count(1) == alist.count(0):
    print 'Equal number of True(s) & False(s)'
    # Όταν ο αριθμός των True & False είναι ίδιος μπορούμε
    # να χρησιμοποιήσουμε την παρακάτω δομή με for
    for i in range(pos, len(alist)):
        alist[j], alist[i] = alist[i], alist[j]
        j += 2
else:
    print 'Different number of True(s) & False(s)'
    # Για να λειτουργεί ο αλγόριθμος και με διαφορετικό αριθμό True & False
    # πρέπει να χρησιμοποιήσουμε την while
    j = 1
    i=pos
    while i<len(alist) and j<len(alist):
        alist[i], alist[j] = alist[j], alist[i]
        j += 2
        i=i+1

#----------------------------------------------------------
# Εμφάνιση αποτελεσμάτων
print '1 & 0 alternately=', alist
#----------------------------------------------------------




