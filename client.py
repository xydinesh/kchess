import requests

def  main():
    payload = {'white': 'eric', 'black': 'thilina', 'wtime': '00:99', 'btime':'00:79', 'result': '10', 'comments': 'Checkmate with bishop and queen.'}
    r = requests.post('http://localhost:53655/game/result', data=payload)
    print r.text

if __name__ == "__main__":
    main()
