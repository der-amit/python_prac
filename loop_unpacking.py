def best_student(scores):
    best_score, best_student = 0, ""
    for student, score in scores:   #ensure you follow the order here as per input
        if score > best_score:
            best_score, best_student = score, student
    return best_student

print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))