def database_print(student_id, student_info, format):

    print(f"{' ' * (9-len(student_id))}{student_id}  {student_info['name']:<20}", end = " ")

    if format == "test":
        for score in student_info["grades"]:
            print(f"{score:<5}", end = " ")
        print()
    elif format == "avg":
        count = 0
        total = 0

        if len(student_info["grades"]) == 0:
            print(f"{'N/A':>8}")
            return

        for score in student_info["grades"]:
            count += 1
            total += float(score)
        print(f"{total/count:.1f}")