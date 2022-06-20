
with open('C:/test/study/nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        line_spisok = line.split()
        remote_addr = line_spisok[0]
        request_type = line_spisok[5][1:4]
        requested_resource = line_spisok[6]
        finite = (remote_addr, request_type, requested_resource)
        print(finite)
