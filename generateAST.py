import os

def main(args):
    if len(args) != 2:
        print("Usage: generate_ast <output directory>", file=sys.stderr)
        sys.exit(64)
    output_dir = args[1]
    defineAst(output_dir, "Expr", [
        "Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : object value",
        "Unary    : Token operator, Expr right"
    ])

def defineAst(outputDir, baseName, types):
    path = os.path.join(outputDir, baseName + ".py")
    with open(path, "w") as writer:
        writer.write("class " + baseName + ":\n")
        writer.write("\tpass\n\n")
        defineVisitor(writer, baseName, types)  # Define the visitor interface
        writer.write("\n")  # Add a newline before defining the base accept() method
        writer.write("  def accept(self, visitor):\n")
        writer.write("    return visitor.visit{}(self)\n\n".format(baseName))  # Base accept() method
        for typeStr in types:
            className, fields = [part.strip() for part in typeStr.split(":")]
            defineType(writer, baseName, className, fields)

def defineVisitor(writer, baseName, types):
    writer.write("  class Visitor:\n")

    for typeStr in types:
        typeName = typeStr.split(":")[0].strip()
        writer.write(f"    def visit{typeName}{baseName}(self, {baseName.lower()}):\n")
        writer.write(f"        pass\n")

    writer.write("\n")

            

def defineType(writer, baseName, className, fieldList):
    writer.write(f"class {className}({baseName}):\n")
    writer.write("\tdef __init__(self, " + ", ".join(field.split()[1] for field in fieldList.split(", ")) + "):\n")
    for field in fieldList.split(", "):
        field_name = field.split()[1]
        writer.write(f"\t\tself.{field_name} = {field_name}\n")
    writer.write("\n")
    writer.write("\tdef accept(self, visitor):\n")
    writer.write(f"\t\treturn visitor.visit{className}{baseName}(self)\n\n")


if __name__ == "__main__":
    import sys
    main(sys.argv)
