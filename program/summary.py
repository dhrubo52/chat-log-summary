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


ERROR_FLAG = False
chat_log_file_list = chat_log_file_names()

for file_name in chat_log_file_list:
    file_text = read_chat_log_files(file_name)

    file_text_list = file_text.split('\n')

    '''
    Combining each message that may have 
    been consisted of multiple lines
    '''
    combined_msg_list = []

    for index, item in enumerate(file_text_list):
        combined_msg_list_length = len(combined_msg_list)
        
        if item.startswith('User: '):
            if index>0 and combined_msg_list[combined_msg_list_length-1].startswith('User: '):
                '''
                We assume that the messages alternate between User and AI.
                So even if we find two message lines one after another that start with 'User: '
                we consider them to be part of one message line. Example user message:

                User: Show me the answer where the previous message was:
                User: What is your name?

                in this case "User: what is your name?" is not a new message but
                part of the previous message."
                '''
                combined_msg_list[combined_msg_list_length-1] = combined_msg_list[combined_msg_list_length-1]+' '+item
            else:
                combined_msg_list.append(item)
        elif item.startswith('AI: '):
            if index>0 and combined_msg_list[combined_msg_list_length-1].startswith('AI: '):
                '''
                We assume and check the same case with the AI message as we did with the
                User message.
                '''
                combined_msg_list[combined_msg_list_length-1] = combined_msg_list[combined_msg_list_length-1]+' '+item
            else:
                combined_msg_list.append(item)
        else:
            if index==0:
                ERROR_FLAG = True
                print(f'Invalid chat log format in {file_name}.')
                break
            combined_msg_list[combined_msg_list_length-1] = combined_msg_list[combined_msg_list_length-1]+' '+item

    if ERROR_FLAG:
        break

    


