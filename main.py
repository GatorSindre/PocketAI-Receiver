import subprocess
import pyautogui
import time
import pyperclip
import socket

response = ""

default_preset = "only use uft-8 characters in this conversation and respond with simple sentences that can be read by a screen reader since i can only hear you not read. And also please ignore the extra o's at the start of my messages"

def chatgpt_new_message(input):
    pyautogui.leftClick(-400, 1000)
    time.sleep(0.5)
    pyautogui.write("oooooo ", 0.05)
    time.sleep(0.1)
    pyautogui.write(input)
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.1)

    wait_for_answer()

def wait_for_answer():
    lastMessage = "past"
    currentMessage = "message"
    check_delay = 0

    # ----   Just run it once without setting last message
    pyautogui.click(-400, 1000)
    for i in range(4):
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
            global response
            response = conversation_to_string(currentMessage)
            print(response)

            time.sleep(0.3)
            return 0

def chatgpt_create_convo(preset=0):
    global convo_exists
    if convo_exists == True:
        print("Stopped duplicate convo")
        return
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

    pyautogui.leftClick(-400, 1000)
    
    pyautogui.press("space")
    pyautogui.write("ooooo ", 0.05)
    time.sleep(0.05)
    pyautogui.write(default_preset)
    time.sleep(0.3)
    pyautogui.press("enter")
    
    time.sleep(1)

    wait_for_answer()

def chatgpt_delete_convo():
    global convo_exists
    if not convo_exists:
        global response
        print("Prevented overusage of chatgpt_delete_convo")
        response = "blocked deletion"
        return
    convo_exists = False

    response = "deleted message"

    pyautogui.leftClick(-30, 16)
    time.sleep(0.3)

convo_exists = False

def conversation_to_string(full_text):

    parts = full_text.split("ChatGPT sa:")
    
    if len(parts) < 2:
        return ""

    latest_message = parts[-1].strip()

    return latest_message



HOST = "0.0.0.0"
PORT = 8081


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)  # allow backlog of connections
print(f"Listening on {HOST}:{PORT}...")

while True:  # keep server running forever
    conn, addr = sock.accept()
    print("Connected by", addr)
    try:
        data = conn.recv(4096)
        if not data:
            print("Client disconnected")
            conn.close()
            continue

        text = data.decode("utf-8")
        print("As string:", text)

        text = text.lower()

        if text == "new":
            chatgpt_create_convo()
            response = "Started new conversation"
        elif text == "del":
            chatgpt_delete_convo()
            response = "Deleted conversation"
        elif text == "rep":
            print("repeating...")
        else:
            chatgpt_new_message(text)
            response = response

        conn.sendall(response.encode("utf-8"))

    except Exception as e:
        print("Error handling client:", e)
    finally:
        conn.close()
        print("Connection closed, waiting for new client...")
