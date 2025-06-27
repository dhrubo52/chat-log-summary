import os

def read_chat_log_files(file_name):
    try:
        with open(f'./chat_logs/{file_name}', 'r') as f:
            file = f.read()

        return file
    except Exception as e:
        print(str(e))
        return None


def chat_log_file_names():
    return [file for file in os.listdir('./chat_logs/') if os.path.isfile(os.path.join(f'./chat_logs/{file}'))]


chat_log_file_list = chat_log_file_names()

for file_name in chat_log_file_list:
    file_txt = read_chat_log_files(file_name)

    print(file_txt)