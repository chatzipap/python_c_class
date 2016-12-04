# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @TasosChatz

'''

ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 8 / σελίδα 89
Το πρόβλημα της ολλανδικής σημαίας αναφέρεται στην αναδιάταξη μιας λίστας
γραμμάτων, η οποία περιέχει μόνο τους χαρακτήρες R, W, B. (Red, White, Blue),
έτσι ώστε όλα τα R να βρίσκονται πριν από τα W και όλα τα W να βρίσκονται πριν
από B. Να τροποποιήσετε έναν από τους αλγορίθμους ταξινόμησης που 
παρουσιάστηκαν σε αυτήν την ενότητα, ώστε να επιλύει αυτό το πρόβλημα.      

'''

# Συνάρτηση Υλοποίησης αλγορίθμου Dutch Flag Problem
def orderFlagColors(aList):
        i, j, n = 0, 0, len(aList) - 1
        while j <= n:
            if aList[j] < 1:
                aList[i], aList[j] = aList[j], aList[i]
                i += 1
                j += 1
            elif aList[j] > 1:
                aList[j], aList[n] = aList[n], aList[j]
                n -= 1
            else:
                j += 1


#----------------------------------------------------------
# Δοκιμαστικές κλήσεις και αποτελέσματα
# Red <--> 0, White <--> 1, Blue <--> 2
dic = {0:'R', 1:'W', 2:'B'} # Δημιουργία λεξικού για αντιστοίχιση χρώματος/αριθ.
import random
start = 0
end = 21
alist = []
for i in range(start, end):
    alist.append(random.choice([0, 1, 2]))
print 'Original List =', alist

orderFlagColors(alist)
print 'Ordered numbered List =', alist
print 'Ordered Flag Color List=', [dic[i] for i  in alist]
#----------------------------------------------------------
