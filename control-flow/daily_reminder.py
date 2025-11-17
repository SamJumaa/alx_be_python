# Ask the user to enter  single Task
task = input("Enter a task description: ")
priority = input("Enter task priority (high/medium/low): ") .lower()
# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes/no): ") .lower()
#Process the Task Based on Priority and Time Sensitivity:
match priority:
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"medium priority task: {task}"
    case "low":
        reminder = f"low piorirty task: {task}"
    case _:
        reminder = f"Task: {task} (Priority not recognized)"
# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
# Print the customized reminder
print(reminder)              
 
