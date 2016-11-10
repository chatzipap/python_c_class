# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 3 / Σελίδα 87
Να γράψετε μια συνάρτηση σε Python, η οποία θα δέχεται μια λίστα, θα ελέγχει αν
τα στοιχεία της είναι σε αύξουσα σειρά και θα επιστρέφει αντίστοιχα true ή false.
Προτείνεται να χρησιμοποιήσετε μια λογική μεταβλητή

'''

# Αλγοριθμική λύση
def ascending(aList):
    ascend = True
    for i in range(len(aList) - 1):
        if aList[i+1] < aList[i] :
            ascend = False
    return ascend

# Pythonic Ways
def ascending2(aList) :
    return all(aList[i+1] > aList[i] for i in range(len(aList) - 1))
            
def ascending3(aList) :
    return sorted(aList) == aList
