import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument('--input', type=str, required=True, help="Path to input file")
    parser.add_argument('--output', type=str, required=True, help="Path to output file")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
