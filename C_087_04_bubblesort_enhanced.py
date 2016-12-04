# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @TasosChatz

'''

ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 4 / Σελίδα 87 (βελτιωμένη φυσαλίδα)
Να δώσετε τη βελτιωμένη έκδοση του αλγορίθμου ταξινόμησης ευθείας ανταλλαγής
η οποία τερματίζει, όταν διαπιστώσει ότι η λίστα είναι ταξινομημένη, ώστε 
να αποφεύγονται περιττές συγκρίσεις.
Υπόδειξη: Χρησιμοποιήστε μια λογική μεταβλητή η οποία θα αλλάζει τιμή, 
αν υπάρχουν τουλάχιστον δύο στοιχεία τα οποία δεν βρίσκονται στην 
επιθυμητή σειρά, καθώς η “φυσαλίδα ανεβαίνει στην επιφάνεια”.

'''

# Κλασική Φυσαλίδα
def bubblesort(aList):
    for i in range(len(aList)):
        for j in range(len(aList) - 1, i-1 , -1):
            if aList[j] < aList[j-1] :
                aList[j], aList[j-1] = aList[j-1], aList[j]
                

# Βελτιωμένη Φυσαλίδα
def shortBubblesort(aList):
        done = False
        i = 0
        # Σταματά η επανάληψη όταν ταξινομηθεί η λίστα
        while i < len(aList) - 1  and done == False :
            done = True
            for j in range(len(aList) - 1, i , -1):
                if aList[j] < aList[j-1] :
                    aList[j], aList[j-1] = aList[j-1], aList[j]
                    done = False

#----------------------------------------------------------                    
# Δοκιμαστικές κλήσεις και αποτελέσματα
import random
start = 0
end = 21
alist = []
for i in range(start, end):
    alist.append(random.randint(1,100))
print 'Original List =', alist
shortBubblesort(alist)
print 'Sorted list=', alist                 
#----------------------------------------------------------