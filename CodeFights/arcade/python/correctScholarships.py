def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) and set(scholarships) <= set(allStudents) and len(scholarships) != len(allStudents)

# Improved version


def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)
