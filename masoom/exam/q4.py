######### Q4

def results(outcome):
    if outcome>=1:
        return "Good!"
    elif outcome<0:
        return "Bad!"
    else:
        return "Valid!"

print(results(5))
print(results(-5))
print(results(0))