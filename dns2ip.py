import socket
import os

file_path = os.path.split(os.path.realpath(__file__))[0]


def get_ip(host):
    """
    Get ip of host.
    """
    try:
        return socket.gethostbyname(host)
    except Exception as e:
        print("Unable to get IP of Hostname, %s" % str(e))


def main():
    result = '%s/result.txt' % file_path
    with open(result, 'w') as r:
        r.write("# Start\n")

        with open("%s/domain.txt" % file_path, "r") as domains:
            for host in domains:
                ip = get_ip(host.strip())
                r.write(ip.strip('\n') + " " + host)
        r.write("\n# End\n")


if __name__ == "__main__":
    main()
