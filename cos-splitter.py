def read_sql_file(file_to_split) -> list[str]:
    with open(file_to_split, "r+") as f:
        return f.readlines()


def strip_from_new_line(text: str):
    return text.replace("\n", "")


def split_line(line: str) -> list[str]:
    split: list[str] = []
    new_line_content = ""
    for current_line_content in line.split(" "):
        if len(new_line_content + current_line_content) > 72:
            split.append(strip_from_new_line(new_line_content))
            new_line_content = f"{current_line_content} "
        else:
            new_line_content = f"{new_line_content}{current_line_content} "
    split.append(strip_from_new_line(new_line_content))
    return split


if __name__ == "__main__":
    file_name: str = input("Filename: ")
    output_file_name: str = ".".join(file_name.split(".")[:-1]) + ".split." + file_name.split(".")[-1]
    print(output_file_name)
    file_content: list[str] = read_sql_file(file_name)
    split_lines: list[str] = []
    for line_content in file_content:
        if len(line_content) > 72:
            split_lines.extend(split_line(line_content))
        else:
            split_lines.append(strip_from_new_line(line_content))
    with open(output_file_name,"w+") as f:
        f.writelines(' \n'.join(split_lines))
 
