import subprocess
import pyautogui
import time
import pyperclip
import socket

presets = (
    "hello", 
    "preset2"
    )

def chatgpt_new_message(input):
    pyautogui.write(input, 0.05)
    time.sleep(0.05)
    pyautogui.press("enter")
    time.sleep(0.1)

    wait_for_answer()

def wait_for_answer():
    lastMessage = "past"
    currentMessage = "message"
    check_delay = 0.2

    # ----   Just run it once without setting last message
    pyautogui.click(-400, 1000)
    for i in range(10):
        pyautogui.scroll(-1000)
        time.sleep(0.1)

    time.sleep(0.2)
    pyautogui.rightClick(-400, 1000)
    time.sleep(0.4)
    pyautogui.leftClick(-690, 874)

    currentMessage = pyperclip.paste()

    time.sleep(check_delay)
    # ----

    while (True):
        pyautogui.click(-400, 1000)
        for i in range(10):
            pyautogui.scroll(-1000)
            time.sleep(0.1)

        time.sleep(0.2)
        pyautogui.rightClick(-400, 1000)
        time.sleep(0.4)
        pyautogui.leftClick(-690, 874)

        lastMessage = currentMessage

        currentMessage = pyperclip.paste()

        if (currentMessage != lastMessage):
            time.sleep(check_delay)
        else:
            response = conversation_to_string(currentMessage)
            print(response)

            time.sleep(0.3)
            return response

def chatgpt_create_convo(preset=0):
    global convo_exists
    convo_exists = True

    subprocess.run([
        r"C:\Program Files\Google\Chrome\Application\chrome.exe", 
        "--incognito"
    ])

    time.sleep(1)

    pyautogui.write("chatgpt.com", 0.05)
    time.sleep(0.05)
    pyautogui.press("enter")

    time.sleep(1.5)


    pyautogui.write(presets[preset-1], 0.05)
    time.sleep(0.05)
    pyautogui.press("enter")
    
    time.sleep(1)

    wait_for_answer()

def chatgpt_delete_convo():
    global convo_exists
    if not convo_exists:
        print("Prevented overusage of chatgpt_delete_convo")
        return
    convo_exists = False

    pyautogui.leftClick(-30, 16)
    time.sleep(0.3)

convo_exists = False

def conversation_to_string(full_text):

    parts = full_text.split("ChatGPT sa:")
    
    if len(parts) < 2:
        return ""  # No ChatGPT message found

    latest_message = parts[-1].strip()

    return latest_message


"""   -- Functions
chatgpt_new_message
chatgpt_delete_convo
chatgpt_create_convo

"""








HOST = "0.0.0.0"
PORT = 8081
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"Listening on {HOST}:{PORT}...")

conn, addr = sock.accept()
print("Connected by", addr)

while True:
    data = conn.recv(4096)
    if not data:
        break

    print("Raw bytes:", data)

    text

    try:
        global text
        text = data.decode("utf-8")
        print("As string:", text)
    except UnicodeDecodeError:
        print("Could not decode bytes to string")

    if text:
        send_variable = f"I received: {text}"

        ## TODO Create code here to receive data and send it back


        conn.sendall(send_variable.encode("utf-8"))  # encode to bytes
    
    else:       # TODO Delete this send-back later when everything is confirmed to work, so nobody tries to ddos and just thinks the port is closed
        # Send back raw bytes if it couldn't decode
        conn.sendall(data)


conn.close()
sock.close()