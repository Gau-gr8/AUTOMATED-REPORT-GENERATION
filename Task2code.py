import csv
from statistics import mean
from fpdf import FPDF, XPos, YPos

# Step 1: Read data from file
filename = "data.csv"
data = []

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['Marks'] = int(row['Marks'])
        data.append(row)

# Step 2: Analyze data
total_students = len(data)
average_marks = mean(row['Marks'] for row in data)
highest = max(data, key=lambda x: x['Marks'])
lowest = min(data, key=lambda x: x['Marks'])

# Step 3: Create PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Helvetica", 'B', 14)
        self.cell(0, 10, "Student Marks Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", 'I', 10)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

pdf = PDFReport()
pdf.add_page()

# Student List
pdf.set_font("Helvetica", 'B', 12)
pdf.cell(0, 10, "Student Marks", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("Helvetica", '', 12)
for row in data:
    pdf.cell(0, 10, f"{row['Name']}: {row['Marks']} marks", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Summary Stats
pdf.ln(5)
pdf.set_font("Helvetica", 'B', 12)
pdf.cell(0, 10, "Summary", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("Helvetica", '', 12)
pdf.cell(0, 10, f"Total Students: {total_students}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 10, f"Average Marks: {average_marks:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 10, f"Highest Marks: {highest['Name']} - {highest['Marks']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 10, f"Lowest Marks: {lowest['Name']} - {lowest['Marks']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Output PDF
pdf.output("student_report.pdf")
