# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: GAURI AGARWAL

*INTERN ID*: CT06DF709

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTHOSH
                                          
*DESCRIPTION*:
This task involves reading student marks from a CSV file, analyzing the data to find useful statistics, and finally generating a well-formatted PDF report using Python. The task demonstrates how data can be programmatically extracted, processed, and transformed into a meaningful document that can be shared or stored.

TOOLS AND LIBRARIES USED:
1. PYTHON: The core programming language used. Python's built-in capabilities for file handling and list manipulation make it ideal for data analysis tasks like this.
2. CSV MODULE: Python’s built-in csv module was used to read the data.csv file. This file contained rows of student names and their corresponding marks. The csv.DictReader helped convert each row into a dictionary for easier access and manipulation.
3. STATISTICS MODULE: The mean function from the statistics module was used to compute the average marks of all students. Python’s standard library makes such mathematical operations straightforward and accurate.
4. FPDF LIBRARY (fpdf2): For creating the PDF report, I used the fpdf2 library, a modern version of the classic FPDF for Python. It allowed me to add pages, set fonts, write headers and footers, and insert custom text — all dynamically based on our analysis. I avoided deprecated parameters (like ln=True) and used XPos and YPos for positioning.
5. IDE USED: VISUAL CODE STUDIO (VS CODE): I used VS Code as the Integrated Development Environment (IDE) for this project. It supports Python development through the Python extension, providing features like syntax highlighting, IntelliSense, debugging tools, and terminal access—all in one place.

PROCESS:
1. DATA PREPARATION: The data was stored in a file named data.csv, containing the names and marks of students. The CSV format was chosen due to its simplicity and universal compatibility.
2. REAING THE DATA: Python’s built-in csv module was used to read the data efficiently. Each row was converted into a dictionary for easier access and manipulation.
3. DATA ANALYSIS: Each student's marks were converted to integers. Then we calculated:
Total number of students
Average marks
Highest scorer
Lowest scorer
This analysis was done using simple Python loops and the statistics.mean() function for average calculation.
4. CREATING THE PDF REPORT: Using the fpdf2 library, a class was created to customize the PDF header and footer. A new page was added, and fonts were set to define different sections of the report.
The Student Marks section listed each student with their corresponding marks.
The Summary section presented the results of the analysis: total number of students, average marks, highest marks, and lowest marks. 
5. EXPORTING THE REPORT: The completed report was saved in a pdf format using: pdf.output("student_report.pdf")

APPLICATIONS:
1. EDUCATIONAL INSTITUTIONS
2. BUSINESS REPORTS
3. HR ANALYTICS
4. FINANCIAL AUDITS
