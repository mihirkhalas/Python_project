import pandas as pd

df = pd.read_csv('marks.csv')

df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

top_student = df.loc[df['Average'].idxmax()]

print("All Students:\n", df)
print("\nTop Performer:\n", top_student)

df.to_csv('updated_marks_report.csv', index=False)