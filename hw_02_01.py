import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Генератор унікальних номерів заявок
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Request_{request_id}"
    request_queue.put(request)
    print(f"Generated: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing: {request}")
    else:
        print("Queue is empty. No requests to process.")

def main():
    while True:
        # Генерація нової заявки
        generate_request()
        # Обробка заявки
        process_request()
        # Затримка для імітації часу обробки
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited.")
import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Генератор унікальних номерів заявок
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Request_{request_id}"
    request_queue.put(request)
    print(f"Generated: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing: {request}")
    else:
        print("Queue is empty. No requests to process.")

def main():
    while True:
        # Генерація нової заявки
        generate_request()
        # Обробка заявки
        process_request()
        # Затримка для імітації часу обробки
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited.")
