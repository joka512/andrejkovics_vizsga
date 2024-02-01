


paths={
    "munkatarsak":r"munkatarsak.txt",
    "gepjarmuvek":r"gepjarmuvek.txt",
    "eladasok":r"eladasok.txt"
}
def load_any(path) -> list:
    x=[]
    with open(path,mode="r") as f:
        for data in f:
            x.append(data.strip())
    return x

def save_any(path,lines):
    """save
        lines: list of strings
    """
    with open(path,mode="w") as f:
        f.writelines(lines)
