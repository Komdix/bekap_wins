while move != pos:
            for element in directions:
                move = element
                if move in plan(element) and move not in been_to and been_to[-1] != move:
                    last_way = directions.index(element)
                    pos = move


        for _ in range(3):
            if last_way != 3:
                last_way += 1
            if last_way == 3:
                last_way = 0
            while move != pos and move not in been_to and move != been_to[-1]:
                print(move, pos)
                been_to.append(move)
                move = directions[last_way]
                if move in plan and last_way not in plan(directions[last_way]):
                    move == pos
            print(been_to,'been')
            if last_pos != pos:
                continue
            else: 
                break