x = int(input())

if x >= 10:
    print("Horse")
elif 1 < x < 10:
    print('Duck')
else:
    print('Baguette')

print("Horse" if x >= 10 else "Duck" if 1 < x < 10 else "Baguette")

# 这样写起来非常的简洁，可以将之前的代码都改正成这种格式

