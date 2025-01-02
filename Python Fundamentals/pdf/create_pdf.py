from fpdf import FPDF

# Create a PDF document
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'StringBuilder Explained', ln=True, align='C')
        self.ln(5)
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()

# Initialize PDF
pdf = PDF()
pdf.add_page()

# Add content to the PDF
pdf.chapter_title("📚 StringBuilder Explained")
pdf.chapter_body("""In programming, particularly in languages like C# and Java, StringBuilder is a class used for manipulating mutable sequences of characters efficiently. Unlike String, which is immutable (cannot be changed once created), StringBuilder allows dynamic modifications like appending, inserting, or removing characters without creating new string objects in memory every time.""")

pdf.chapter_title("🛠️ Key Features of StringBuilder")
pdf.chapter_body("""1. Mutable: You can modify the content without creating a new object.\n2. Efficient: Reduces memory overhead when performing repeated string modifications.\n3. Dynamic Size: Automatically resizes the buffer when needed.\n4. Performance: Much faster than String for operations like concatenation in loops.""")

pdf.chapter_title("📝 String vs. StringBuilder")
pdf.chapter_body("""String:\n- Immutable\n- Creates new object on modification\n- Slow for frequent modifications\n- Use Case: Static/constant strings\n\nStringBuilder:\n- Mutable\n- Modifies the existing object\n- Fast for frequent modifications\n- Use Case: Frequent dynamic updates""")

pdf.chapter_title("✅ C# StringBuilder Methods")
pdf.chapter_body("""- Append(string value): Adds text to the end of the current StringBuilder.\n- Insert(int index, string value): Inserts text at the specified index.\n- Remove(int startIndex, int length): Removes a range of characters.\n- Replace(string oldValue, string newValue): Replaces all occurrences of a string.\n- Clear(): Removes all characters.\n- ToString(): Converts StringBuilder to a string.""")

pdf.chapter_title("💡 When to Use StringBuilder?")
pdf.chapter_body("""- When performing repeated string concatenations in loops.\n- When modifying string content frequently.\n- When working with dynamic strings whose
