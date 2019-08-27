n = int(input())
for i in range(1, n + 1):
    url = input()
    protocol, url = url.split('://', 1)
    if '/' in url:
        url, path = url.split('/', 1)
    else:
        path = '<default>'
    if ':' in url:
        host, port = url.split(':', 1)
    else:
        host = url
        port = '<default>'
    # print(f"URL #{i}\n{'Protocol'.ljust(9)}= {protocol}\n{'Host'.ljust(9)}= {host}\n{'Port'.ljust(9)}= {port}\n{'Path'.ljust(9)}= {path}")
    print('URL #{}'.format(i))
    print('Protocol = {}'.format(protocol))
    print('Host     = {}'.format(host))
    print('Port     = {}'.format(port))
    print('Path     = {}'.format(path))
    if i==n:
        break
    print()