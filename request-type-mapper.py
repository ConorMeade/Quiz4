import sys

def main(argv):

    try:
        for line in sys.stdin:
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

    except EOFError as error:
        return None


if __name__ == "__main__":
    main(sys.argv)