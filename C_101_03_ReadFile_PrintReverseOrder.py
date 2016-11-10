# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 6ο ΔΙΑΧΕΙΡΙΣΗ ΑΡΧΕΙΩΝ
Δραστηριότητα 3 / σελίδα 101
Να γράψετε πρόγραμμα στη γλώσσα Python, το οποίο θα δέχεται ως είσοδο το όνο-
μα ενός αρχείου, θα εμφανίζει τα περιεχόμενά του κατά γραμμή και στη συνέχεια θα
γράφει σε ένα άλλο αρχείο, τις γραμμές του αρχείου στην αντίστροφη σειρά.  
      
'''

# Δημιουργία αναφοράς σε αρχείο
f = open ('testFile.txt', 'r')

# pythonic way
for line in reversed(open("testFile.txt").readlines()):
    print line

# Αλγοριθμικη προσέγγιση
lines = []
for line in f :
    lines.append(line)

# Χωρίς μέθοδο αναστροφής
for i in range(len(lines)-1,0,-1):
    print lines[i]

# Με χρήση μεθόδου αναστροφής    
lines.reverse()
for line in lines :
    print line
    
f.close()
