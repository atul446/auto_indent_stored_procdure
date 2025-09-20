def format_mysql_procedure(sql_code: str, indent_size: int = 4) -> str:
    """
    Auto-formats MySQL procedure code so that nested IF blocks
    are indented similar to Python indentation style.

    Args:
        sql_code (str): Input SQL procedure code as a string
        indent_size (int): Spaces per indentation level

    Returns:
        str: Formatted SQL procedure string
    """
    formatted_lines = []
    indent_level = 0

    # Keywords to increase/decrease indentation
    increase_keywords = ("IF", "CASE", "WHILE", "LOOP", "BEGIN")
    decrease_increase_keywords = ("ELSEIF", "ELSE")
    decrease_keywords = ("END IF", "END CASE", "END WHILE", "END LOOP", "END")

    for raw_line in sql_code.splitlines():
        line = raw_line.strip()

        # Skip empty lines but preserve them
        if not line:
            formatted_lines.append("")
            continue
        
        if any(line.upper().startswith(kw) for kw in decrease_increase_keywords):
            formatted_lines.append(" " * (max(indent_level - 1, 0) * indent_size) + line)
            continue
            
        # If the line starts with an END keyword, reduce indent first
        if any(line.upper().startswith(kw) for kw in decrease_keywords):
            indent_level = max(indent_level - 1, 0)

        # Apply indentation
        formatted_lines.append(" " * (indent_level * indent_size) + line)

        # If the line starts with an increase keyword (and not END), indent after
        if any(line.upper().startswith(kw) for kw in increase_keywords) and not line.upper().startswith("END"):
            indent_level += 1

    return "\n".join(formatted_lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Format MySQL procedure indentation.")
    parser.add_argument("input_file", help="Path to the input SQL file")
    parser.add_argument("-o", "--output_file", help="Path to save the formatted SQL file (optional)")
    args = parser.parse_args()

    # Read SQL code from file
    with open(args.input_file, "r", encoding="utf-8") as f:
        raw_sql = f.read()

    formatted_sql = format_mysql_procedure(raw_sql)

    if args.output_file:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(formatted_sql)
        print(f"Formatted SQL written to {args.output_file}")
    else:
        print(formatted_sql)
