max_term_value : int = 10000

def fibonacci():
    curr_term = 0
    next_term = 1
    while curr_term <= max_term_value:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

fibonacci()        
