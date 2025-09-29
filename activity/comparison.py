# add your get_student_with_more_classes function here!
def get_student_with_more_classes(student1, student2):
    """
    Compares two students and returns the one with more classes.
    If they have the same number, it returns None.
    """
    if student1.get_num_classes() > student2.get_num_classes():
        return student1
    elif student2.get_num_classes() > student1.get_num_classes():
        return student2
    else:
        return None
