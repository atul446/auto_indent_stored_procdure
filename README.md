
````markdown
# MySQL Procedure Formatter

A lightweight Python tool to **auto-format MySQL stored procedure code** for better readability.  
It focuses on fixing **indentation of nested `IF ... END IF;` blocks** (and similar structures like `CASE`, `WHILE`, `BEGIN/END`) to follow a Python-like indentation style, without changing any other part of the SQL code.

---

## ✨ Features
- Automatically adjusts indentation for:
  - `IF ... THEN ... ELSE ... END IF;`
  - `CASE ... END CASE;`
  - `WHILE ... END WHILE;`
  - `BEGIN ... END;`
  - `LOOP ... END LOOP;`
- Preserves all SQL code as-is, only correcting indentation.
- Works on single files or outputs directly to the console.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/mysql-procedure-formatter.git
cd mysql-procedure-formatter
````

(Optional) create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

> No external dependencies are required (pure Python).

---

## 🚀 Usage

### Format and print to console:

```bash
python format_sql.py myproc.sql
```

### Format and save to a new file:

```bash
python format_sql.py myproc.sql -o myproc_formatted.sql
```

### Example

**Input:**

```sql
CREATE PROCEDURE test_proc()
BEGIN
IF condition1 THEN
IF condition2 THEN
SET @x = 1;
ELSE
SET @x = 2;
END IF;
ELSEIF condition3 THEN
SET @x = 3;
END IF;
END;
```

**Output:**

```sql
CREATE PROCEDURE test_proc()
BEGIN
    IF condition1 THEN
        IF condition2 THEN
            SET @x = 1;
        ELSE
            SET @x = 2;
        END IF;
    ELSEIF condition3 THEN
        SET @x = 3;
    END IF;
END;
```

---

## ⚙️ Options

* `input_file` (required): Path to the SQL file you want to format.
* `-o output_file` (optional): Save formatted SQL into a new file instead of printing to console.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

---

Do you want me to also add a **badge section** (Python version, license, etc.) to make the README more GitHub-friendly?
```

