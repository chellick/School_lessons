def f(heap, stop, step, moves):
    
    if sum(heap) >= 109 and step % 2 == 0:
        print(moves[0])
        return True
    elif sum(heap) >= 109 and step % 2 != 0: return False
    
    elif max(heap) >= stop and step == 3:
        print(moves[0])
        return True
    elif max(heap) < stop and step == 3: return False
    elif max(heap) >= stop: return False
    
    
    
    if step % 2 == 0:
        return f([heap[0]+1, heap[1]], stop, step+1, moves+'A') or\
            f([heap[0]+2, heap[1]], stop, step+1, moves+'B') or\
                f([heap[0]*2, heap[1]], stop, step+1, moves+'C') or\
                    f([heap[0], heap[1]+1], stop, step+1, moves+'A') or\
                        f([heap[0], heap[1]+2], stop, step+1, moves+'B') or\
                            f([heap[0], heap[1]*2], stop, step+1, moves+'C')
    
    else:
        return f([heap[0]+1, heap[1]], stop, step+1, moves+'1') and\
            f([heap[0]+2, heap[1]], stop, step+1, moves+'2') and\
                f([heap[0], heap[1]+2], stop, step+1, moves+'3') and\
                    f([heap[0], heap[1]+1], stop, step+1, moves+'4') and\
                        f([heap[0]*2, heap[1]], stop, step+1, moves+'5') and\
                            f([heap[0], heap[1]*2], stop, step+1, moves+'6')
                            
                            
for s in range(1, 50):
    if f([24, s], 50, 0, ''):
        print(s, '----')
    
    
a = int(input('ВВедите 1, 2, 3, 4, 5: '))

if a == 1:
    print('Yes')
elif a == 2:
    print('YES')
elif a == 3:
    print('YEEEH')