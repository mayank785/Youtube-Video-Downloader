def main():
    print("========== CSV Maker ==========")
    maker()

def maker():
    for i in range(0, 100000000):
        csv_upd()

def csv_upd():
    with open("vid_url.csv", "a") as f:
        for j in range(1, 100000000000):
            item = input("Enter the url : ")
            if item == "e".lower():
                f.close()
            f.write(f"{j}, {item}\n")

main()