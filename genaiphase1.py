import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Construction_Data_PM_Tasks_All_Projects.csv")

#question 1
overdue_tasks = df[df["OverDue"] == True].shape[0]

print(f"The total number of overdue tasks is: {overdue_tasks}")

#question 2
task_groups = df.groupby(["Task Group", "Report Status"])["Report Status"].count().unstack(fill_value=0)

for task_group in task_groups.index:
    open_tasks = task_groups.loc[task_group, "Open"]
    closed_tasks = task_groups.loc[task_group, "Closed"]
    print(f"For task group '{task_group}', there are {open_tasks} tasks with 'Open' status and {closed_tasks} tasks with 'Closed' status.")

#question 3
task_groups = df.groupby(["Task Group", "Report Status"])["Report Status"].count().unstack(fill_value=0)

ax = task_groups.plot(kind="bar", stacked=True, figsize=(10, 5))
ax.set_xlabel("Task Group")
ax.set_ylabel("Number of Tasks")
ax.set_title("Total Number of Open and Closed Tasks by Each Task Group")

plt.show()
plt.savefig('total_number_of_open_and_closed_tasks_by_task_group.png')
plt.close()


#question 4
overdue_tasks = df.groupby('project')['OverDue'].sum()

# Create a bar chart of the total number of overdue tasks for each project
overdue_tasks.plot(kind='bar')

# Set the title and axis labels
plt.title('Total Number of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')

# Show the plot
plt.show()
plt.savefig('total_number_of_overdue_tasks_by_project.png')
plt.close()

#question 5
total_tasks = df.groupby('project')['OverDue'].count()

# Calculate the total number of overdue tasks for each project
overdue_tasks = df.groupby('project')['OverDue'].sum()

# Calculate the percentage of overdue tasks for each project
percent_overdue = (overdue_tasks / total_tasks) * 100

# Create a bar chart of the percentage of overdue tasks for each project
percent_overdue.plot(kind='bar')

# Set the title and axis labels
plt.title('Percentage of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Percentage of Overdue Tasks')

# Show the plot
plt.show()
plt.savefig('percentage_of_overdue_tasks_by_project.png')
plt.close()

#question 6
# Load the CSV file into a pandas DataFrame
data = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')

# Convert the "Created" column to datetime format
data['Created'] = pd.to_datetime(data['Created'], dayfirst=True)

# Calculate the difference between today's date and the "Created" column
diff = pd.Timestamp.now() - data['Created']

# Add the differences to the DataFrame
data['Days Elapsed'] = diff.dt.days

# Calculate the mean days elapsed by project and sort by project
mean_days_elapsed_by_project = data.groupby('Project')['Days Elapsed'].mean().sort_values()

print(f"{'Project':<30} {'Mean Days Elapsed':<20}")
for project, days in mean_days_elapsed_by_project.items():
    print(f"{project:<30} {int(days):<20}")

#question 7
# Filter for open forms
open_forms = data[data['Report Forms Status'] == 'Open']

# Group by Type and count the number of open forms
open_form_counts = open_forms.groupby('Type')['Report Forms Status'].count()

# Create a bar chart of the number of open forms by Type of form
open_form_counts.plot(kind='bar', title='Number of Open Forms by Type')
plt.xlabel('Type')
plt.ylabel('Number of Open Forms')
plt.show()
plt.savefig('number_of_open_forms_by_type_of_form.png')
plt.close()

#question 8
# Filter for open forms
open_forms = data[data['Report Forms Status'] == 'Open']

# Group by "Report Forms Group" and count the number of open forms
open_form_counts = open_forms.groupby('Report Forms Group')['Report Forms Status'].count()

# Create a time series plot of the number of open forms by "Report Forms Group"
open_form_counts.plot(kind='line', title='Number of Open Forms by Report Forms Group')
plt.xlabel('Report Forms Group')
plt.ylabel('Number of Open Forms')
plt.show()
plt.savefig('number_of_forms_opened_by_report_form_group.png')
plt.close()