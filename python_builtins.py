# =============================================================================
# Python Built-in Functions — Medium Difficulty Examples
# Covers: Data & Iteration | Type Conversion | I/O & Inspection | Advanced
# =============================================================================


# =============================================================================
# SECTION 1: DATA & ITERATION
# =============================================================================

# --- len() ---
# Returns the number of items in an object.
# Here we use it to validate that two lists are the same length before pairing.
students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]
if len(students) == len(grades):
    print("Lists are equal length, safe to pair.")
else:
    print("Mismatch! Cannot pair students and grades.")
# Output: Lists are equal length, safe to pair.


# --- range() ---
# Generates a sequence of numbers.
# Here we use range with step to build a multiplication table for 5.
table = 5
print(f"Multiplication table of {table}:")
for i in range(1, 11):               # from 1 to 10
    print(f"{table} x {i} = {table * i}")
# Output: 5 x 1 = 5, 5 x 2 = 10 ... 5 x 10 = 50


# --- enumerate() ---
# Adds an index counter to an iterable.
# Here we find which students scored below 80 and report their position.
scores = [91, 73, 88, 65, 95]
print("Students who need improvement:")
for rank, score in enumerate(scores, start=1):  # start rank from 1, not 0
    if score < 80:
        print(f"  Student #{rank} scored {score} — needs improvement")
# Output: Student #2 scored 73, Student #4 scored 65


# --- zip() ---
# Pairs elements from two or more iterables together.
# Here we combine names, scores, and grades into a single report.
names  = ["Alice", "Bob", "Charlie", "Diana"]
scores = [91, 73, 88, 65]
grades = ["A", "C", "B", "D"]
print("\nStudent Report:")
for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score}/100 → Grade {grade}")
# Output: Alice: 91/100 → Grade A, etc.


# --- map() ---
# Applies a function to every item in an iterable.
# Here we normalize a list of temperatures from Celsius to Fahrenheit.
celsius_temps = [0, 20, 37, 100]
def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 2)   # formula: (C × 9/5) + 32
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print("\nTemperature conversion:")
for c, f in zip(celsius_temps, fahrenheit_temps):
    print(f"  {c}°C = {f}°F")
# Output: 0°C = 32°F, 20°C = 68°F, 37°C = 98.6°F, 100°C = 212°F


# --- filter() ---
# Filters an iterable, keeping only items where the function returns True.
# Here we extract only premium users from a user list.
users = [
    {"name": "Alice", "plan": "premium"},
    {"name": "Bob",   "plan": "free"},
    {"name": "Charlie", "plan": "premium"},
    {"name": "Diana", "plan": "free"},
]
premium_users = list(filter(lambda u: u["plan"] == "premium", users))
print("\nPremium users:")
for user in premium_users:
    print(f"  {user['name']}")
# Output: Alice, Charlie


# --- sorted() ---
# Returns a new sorted list without modifying the original.
# Here we sort students by score descending, then alphabetically for ties.
students_data = [
    {"name": "Charlie", "score": 88},
    {"name": "Alice",   "score": 95},
    {"name": "Bob",     "score": 88},
    {"name": "Diana",   "score": 72},
]
# Sort by score descending (-score), then name ascending for ties
ranked = sorted(students_data, key=lambda s: (-s["score"], s["name"]))
print("\nLeaderboard:")
for i, s in enumerate(ranked, start=1):
    print(f"  {i}. {s['name']} — {s['score']}")
# Output: 1. Alice 95, 2. Bob 88, 3. Charlie 88, 4. Diana 72


# --- reversed() ---
# Returns an iterator that goes through a sequence in reverse.
# Here we print a countdown timer.
print("\nCountdown:")
for t in reversed(range(1, 6)):   # range(1,6) = [1,2,3,4,5], reversed = [5,4,3,2,1]
    print(f"  {t}...")
print("  Launch!")
# Output: 5... 4... 3... 2... 1... Launch!


# --- sum() ---
# Adds up all items in an iterable.
# Here we calculate the total and average score of a class.
class_scores = [91, 73, 88, 65, 95, 82, 76]
total = sum(class_scores)
average = total / len(class_scores)   # combine with len()
print(f"\nClass total: {total}")
print(f"Class average: {average:.2f}")   # :.2f = 2 decimal places
# Output: Class total: 570, Class average: 81.43


# --- min() and max() ---
# Returns the smallest or largest item.
# Here we find the lowest and highest scoring students by using the key argument.
students_scores = {"Alice": 91, "Bob": 73, "Charlie": 88, "Diana": 65}
top_student    = max(students_scores, key=students_scores.get)   # key=.get looks at values
bottom_student = min(students_scores, key=students_scores.get)
print(f"\nTop student: {top_student} ({students_scores[top_student]})")
print(f"Needs support: {bottom_student} ({students_scores[bottom_student]})")
# Output: Top student: Alice (91), Needs support: Diana (65)


# =============================================================================
# SECTION 2: TYPE CONVERSION
# =============================================================================

# --- int() ---
# Converts a value to an integer.
# Here we parse user input and do binary-to-decimal conversion.
user_input = "255"
decimal = int(user_input)         # "255" → 255
binary_str = "11111111"
from_binary = int(binary_str, 2)  # base 2 → reads as binary → 255
print(f"\n'{user_input}' as int: {decimal}")
print(f"'{binary_str}' in binary = {from_binary} in decimal")
# Output: '255' as int: 255 | '11111111' in binary = 255 in decimal


# --- float() ---
# Converts a value to a floating-point number.
# Here we calculate a percentage with float precision.
correct = "45"
total   = "60"
percentage = (float(correct) / float(total)) * 100   # string → float for division
print(f"\nScore: {correct}/{total} = {percentage:.1f}%")
# Output: Score: 45/60 = 75.0%


# --- str() ---
# Converts a value to its string representation.
# Here we build a summary sentence by combining different types.
item  = "laptop"
price = 799
qty   = 3
summary = "Item: " + item + " | Price: $" + str(price) + " | Qty: " + str(qty)
print("\n" + summary)
# Output: Item: laptop | Price: $799 | Qty: 3


# --- list() ---
# Converts an iterable to a list.
# Here we convert a string to a list of characters, modify it, then rejoin.
word = "hello"
chars = list(word)       # "hello" → ['h', 'e', 'l', 'l', 'o']
chars[0] = chars[0].upper()   # capitalize first letter
result = "".join(chars)       # rejoin to string
print(f"\n'{word}' → modified → '{result}'")
# Output: 'hello' → modified → 'Hello'


# --- dict() ---
# Creates a dictionary from key-value pairs.
# Here we build a word frequency counter using zip and dict.
keys   = ["python", "java", "c++"]
values = [120, 85, 60]
language_popularity = dict(zip(keys, values))  # zip pairs them, dict converts
print("\nLanguage Popularity:")
for lang, score in language_popularity.items():
    print(f"  {lang}: {score}")
# Output: python: 120, java: 85, c++: 60


# --- set() ---
# Creates a set — unique elements only, unordered.
# Here we find common interests between two users using set intersection.
alice_interests = ["python", "music", "gaming", "reading"]
bob_interests   = ["java", "music", "gaming", "cooking"]
common = set(alice_interests) & set(bob_interests)   # & = intersection
print(f"\nAlice and Bob both like: {common}")
only_alice = set(alice_interests) - set(bob_interests)   # - = difference
print(f"Only Alice likes: {only_alice}")
# Output: both like: {'gaming', 'music'} | Only Alice: {'python', 'reading'}


# --- tuple() ---
# Converts to an immutable sequence.
# Here we store fixed coordinate pairs that should never be modified.
raw_coords = [[10, 20], [30, 40], [50, 60]]
# Convert each list to a tuple to make coordinates immutable/hashable
fixed_coords = [tuple(coord) for coord in raw_coords]
print(f"\nFixed coordinates: {fixed_coords}")
# Tuples can be used as dict keys because they're hashable (lists cannot)
location_names = {(10, 20): "Home", (30, 40): "Office", (50, 60): "Gym"}
for coord, name in location_names.items():
    print(f"  {coord} → {name}")
# Output: (10,20) → Home, (30,40) → Office, (50,60) → Gym


# --- bool() ---
# Converts a value to True or False.
# Here we validate form fields — empty strings and 0 are falsy.
def validate_form(name, age, email):
    fields = {"name": name, "age": age, "email": email}
    errors = []
    for field, value in fields.items():
        if not bool(value):   # empty string, 0, None are all falsy
            errors.append(f"  '{field}' is required")
    return errors

errors = validate_form("Alice", 0, "")   # age=0 and email="" are falsy
print("\nForm validation errors:")
for err in errors:
    print(err)
# Output: 'age' is required | 'email' is required


# =============================================================================
# SECTION 3: I/O & INSPECTION
# =============================================================================

# --- print() ---
# Outputs to the console with flexible formatting options.
# Here we build a formatted table using sep and f-strings.
headers = ["Name", "Score", "Grade"]
rows = [("Alice", 91, "A"), ("Bob", 73, "C"), ("Charlie", 88, "B")]
print("\n" + "-"*30)
print(*headers, sep="\t\t")    # sep="\t\t" puts tabs between each header
print("-"*30)
for row in rows:
    print(*row, sep="\t\t")    # unpack tuple and separate with tabs
print("-"*30)
# Output: Name   Score   Grade (tab-separated table)


# --- type() ---
# Returns the data type of an object — mainly used for debugging.
# Here we inspect what types come out of a mixed data source (like a CSV).
raw_data = ["42", 3.14, True, None, [1, 2], {"key": "val"}]
print("\nType inspection:")
for item in raw_data:
    print(f"  {str(item):<15} → {type(item).__name__}")
# Output shows type name cleanly: int, float, bool, NoneType, list, dict


# --- isinstance() ---
# Checks if an object belongs to a specific class. Better than type() for safety.
# Here we write a function that handles both int and float inputs gracefully.
def safe_double(value):
    if isinstance(value, (int, float)):   # check against multiple types at once
        return value * 2
    elif isinstance(value, str):
        return value * 2   # repeats string twice: "hi" → "hihi"
    else:
        return None   # unsupported type

print("\nSafe double:")
for val in [5, 3.14, "hi", [1, 2]]:
    print(f"  safe_double({val!r}) = {safe_double(val)}")
# Output: 10, 6.28, 'hihi', None


# --- dir() ---
# Lists all attributes and methods of an object.
# Here we use it to discover all string methods that contain "find".
string_methods = [m for m in dir("") if "find" in m.lower()]
print(f"\nString methods with 'find': {string_methods}")
# Output: ['find', 'rfind']   ← rfind searches from the right side


# --- id() ---
# Returns the memory address (identity) of an object.
# Here we demonstrate the difference between copy and reference.
original = [1, 2, 3]
reference = original        # points to same object in memory
copy      = original[:]     # creates a new object via slicing

print(f"\noriginal id : {id(original)}")
print(f"reference id: {id(reference)}  ← same as original!")
print(f"copy id     : {id(copy)}  ← different object")

reference.append(99)   # modifying reference ALSO changes original
print(f"\nAfter appending to reference:")
print(f"  original  = {original}")   # [1, 2, 3, 99] — changed!
print(f"  copy      = {copy}")       # [1, 2, 3]    — unchanged
# This is why understanding id() matters for avoiding bugs.


# =============================================================================
# SECTION 4: ADVANCED
# =============================================================================

# --- any() ---
# Returns True if at least ONE element is truthy. Short-circuits on first True.
# Here we check if any product in a cart is out of stock.
cart_items = [
    {"name": "Phone",   "in_stock": True},
    {"name": "Charger", "in_stock": False},   # out of stock!
    {"name": "Case",    "in_stock": True},
]
has_out_of_stock = any(not item["in_stock"] for item in cart_items)
if has_out_of_stock:
    print("\nWarning: Some items in your cart are out of stock!")
# Output: Warning: Some items in your cart are out of stock!


# --- all() ---
# Returns True only if ALL elements are truthy. Short-circuits on first False.
# Here we validate that a password meets all required conditions.
password = "SecurePass1!"
checks = [
    len(password) >= 8,                         # at least 8 characters
    any(c.isupper() for c in password),         # has uppercase
    any(c.isdigit() for c in password),         # has a digit
    any(c in "!@#$%" for c in password),        # has special character
]
if all(checks):   # all() ensures every single check passed
    print("\nPassword is strong!")
else:
    print("\nPassword is too weak.")
# Output: Password is strong!


# --- open() ---
# Opens a file for reading or writing. Always use with 'with' statement.
# Here we write student data to a file and read it back.
filename = "students.txt"
student_records = [("Alice", 91), ("Bob", 73), ("Charlie", 88)]

# WRITE: save each student on a new line
with open(filename, "w") as f:
    f.write("Name,Score\n")              # header row
    for name, score in student_records:
        f.write(f"{name},{score}\n")     # write each record

# READ: read back and parse the data
print("\nReading from file:")
with open(filename, "r") as f:
    lines = f.readlines()               # read all lines into a list
    header = lines[0].strip()           # first line is the header
    print(f"  Header: {header}")
    for line in lines[1:]:              # skip header, iterate data rows
        name, score = line.strip().split(",")
        print(f"  {name} scored {score}")
# Output: Alice scored 91, Bob scored 73, Charlie scored 88


# --- getattr() ---
# Dynamically gets an attribute from an object by name (as a string).
# Here we build a flexible report generator that reads field names from a list.
class Product:
    def __init__(self, name, price, category, stock):
        self.name     = name
        self.price    = price
        self.category = category
        self.stock    = stock

laptop = Product("MacBook", 1299, "Electronics", 15)

# Instead of hardcoding laptop.name, laptop.price, etc.,
# we dynamically pick which fields to display.
report_fields = ["name", "price", "stock"]   # could come from config or DB
print("\nProduct Report:")
for field in report_fields:
    value = getattr(laptop, field, "N/A")    # "N/A" is the default if field not found
    print(f"  {field.capitalize()}: {value}")
# Output: Name: MacBook | Price: 1299 | Stock: 15


# --- setattr() ---
# Dynamically sets an attribute on an object by name.
# Here we apply a bulk update from a dictionary to an object.
class UserProfile:
    def __init__(self, username):
        self.username = username
        self.bio      = ""
        self.location = ""
        self.website  = ""

user = UserProfile("sinan_ck")

# Simulate receiving updated fields from a form submission
form_data = {
    "bio":      "Python developer & DSA enthusiast",
    "location": "Kerala, India",
    "website":  "github.com/Sinan-ck",
}

for field, value in form_data.items():
    setattr(user, field, value)   # dynamically set each field by name

print("\nUpdated Profile:")
print(f"  @{user.username}")
print(f"  Bio: {user.bio}")
print(f"  Location: {user.location}")
print(f"  Website: {user.website}")
# Output: updated profile with all form_data applied


# --- callable() ---
# Returns True if the object can be called like a function.
# Here we build a flexible pipeline that safely calls only callable steps.
def double(x):   return x * 2
def add_ten(x):  return x + 10
def square(x):   return x ** 2

pipeline = [double, add_ten, 5, square, None]   # mix of callables and non-callables

value = 3
print(f"\nPipeline starting with {value}:")
for step in pipeline:
    if callable(step):              # only call it if it's actually callable
        value = step(value)
        print(f"  Applied {step.__name__}() → {value}")
    else:
        print(f"  Skipped {step!r} (not callable)")
# Output: double → 6, add_ten → 16, skipped 5, square → 256


# --- vars() ---
# Returns an object's attributes as a dictionary (__dict__).
# Here we use it to serialize an object to a plain dict for JSON export.
import json

class Order:
    def __init__(self, order_id, item, qty, price):
        self.order_id = order_id
        self.item     = item
        self.qty      = qty
        self.price    = price
        self.total    = qty * price   # computed field

order = Order("ORD-001", "Laptop", 2, 799)

order_dict = vars(order)   # converts object attributes → dict
json_output = json.dumps(order_dict, indent=2)   # dict → JSON string
print(f"\nOrder as JSON:\n{json_output}")
# Output: JSON with order_id, item, qty, price, total fields
