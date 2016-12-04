# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @TasosChatz

'''

ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 5 / σελίδα 89
Να γράψετε μια συνάρτηση σε Python η οποία θα δέχεται μια λίστα με λογικές τιμές
True/False και θα διαχωρίζει τις τιμές αυτές, τοποθετώντας τα True πριν από τα
False.   
             
'''

# Διάταξη λογικών τιμών
def orderBooleans(aList):
        i, j, n = 0, 0, len(aList) - 1
        while j <= n:
            if aList[j] > False:
                aList[i], aList[j] = aList[j], aList[i] 
                i += 1
                j += 1
            else:
                j += 1

#----------------------------------------------------------
# Δοκιμαστικές κλήσεις και αποτελέσματα
import random
start = 0
end = 21
alist = []
for i in range(start, end):
    alist.append(random.choice([True, False]))
print 'Original List =', alist
orderBooleans(alist)
print 'True Before False LIST=', alist
#----------------------------------------------------------