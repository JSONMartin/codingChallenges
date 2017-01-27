# Recursive
def nb_year(population, percent, aug, target, years = 0):
    if population < target:
        return nb_year( (population + int(population * percent/100) + aug), percent, aug, target, years + 1)
    return years

# Non - Recursive
def nb_year(p0, percent, aug, p):
    def calc_year(cur, percent, aug):
        return cur + (cur * percent/100) + aug

    population = p0
    years = 0

    while population < p:
        population = calc_year(population, percent, aug)
        years+=1

    return years

