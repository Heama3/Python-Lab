#feedback
feedback=input("Enter your feedback:")
feedback_lower=feedback.lower()
count_good=feedback_lower.split().count("good")
print(f"The word good appears {count_good} time(s).")
