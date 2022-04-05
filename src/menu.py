from week0 import swap
from week0 import restaurantmenu
from week1 import listsandloops
from week2 import factorial
from week2 import imperativeFactors
from week2 import oopFactors
from week2 import palindrome

main_menu = [

]
#week 0 submenu
week0_list = [
    ["Swap", swap.test_swappers],
    ["Restaurant Menu", restaurantmenu.menu],
]
#week 1 submenu
week1_list = [
    ["Fibonacci", listsandloops.test_recur_fibonacci],
    ["For Loop", listsandloops.for_loop]
]

#week 2 submenu
week2_list = [
    ["Factorial Class", factorial.factorialTester],
    ["Factors Function Imperative", imperativeFactors.factorTest],
    ["Factors Function OOP", oopFactors.factorsTest],
    ["Palindrome Extra Credit", palindrome.palindromeTester]
]

# Second menu for iteration
iteration_list = [
    ["For Loop to print all of InfoDb", listsandloops.for_loop],
    ["While Loop to print all of InfoDb", listsandloops.while_loop],
    ["Recursive Loop to print all of InfoDb", listsandloops.test_recur_loop]
]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0",week0Menu])
    menu_list.append(["Week 1",week1Menu])
    menu_list.append(["Week 2",week2Menu])
    buildMenu(title, menu_list)

def iterationMenu():
    title = "Iteration Menu" + banner
    buildMenu(title, iteration_list)

def week0Menu():
    title = "Week 0 Menu" + banner
    buildMenu(title, week0_list)

def week1Menu():
    title = "Week 1 Menu" + banner
    week1_list.append(["Iteration to print Info", iterationMenu],)
    buildMenu(title, week1_list)

def week2Menu():
    title = "Week 2 Menu" + banner
    buildMenu(title, week2_list)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])


    choice = input("Type your choice> ")


    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")

    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")


    buildMenu(banner, options)


if __name__ == "__main__":
    menu()