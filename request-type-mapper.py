import sys


# def main(argv):
#     line = sys.stdin.readline()
#     pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
#     try:
#         while line:
#             for word in pattern.findall(line):
#                 print ("LongValueSum:" + word.lower() + "\t" + "1")
#                 # x = 1 / random.randint(0,99)
#             line = sys.stdin.readline()
#     except EOFError as error:
#         return None

# if __name__ == "__main__":
#     main(sys.argv)

def main(argv):
    line = sys.stdin.readline()
    try:
        # for line in sys.stdin:
        while line:
            # split on opening parens, second element will be the request type
            log_elems = line.split('"')
            if len(log_elems) > 1:
                # print(log_elems)
                # break
                # after date time portion, we have the GET, POST, PUT etc. message
                request = log_elems[1].split()  # ['GET', '/index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53', 'HTTP/1.1']
                # ensure we actually have data
                if len(request) > 0:
                    method = request[0]
                    print(f"{method}\t1")
        line = sys.stdin.readline()
                

    except EOFError as error:
        return None


if __name__ == "__main__":
    main(sys.argv)