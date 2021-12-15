"""
ASSIGNMENT 5
Steven Michalove
Nov 13 2021

Mailroom
========

Overall Program Goal:
---------------------

You work in the mail room at a local charity. Part of your job is to write
incredibly boring, repetitive emails thanking your donors for their generous
gifts. You are tired of doing this over and over again, so you've decided to
let Python help you out of a jam and do your work for you.


The Program:
------------

Write a small command-line script called ``mailroom.py``. This script should be executable. The script should
 accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each. You can store that data structure in
   the global namespace.

* The script should prompt the user (you) to choose from a menu of 3 actions:
  "Send a Thank You", "Create a Report" or "quit".

Send a Thank You
----------------

* If the user (you) selects "Send a Thank You" option, prompt for a Full Name.

  * If the user types ``list`` show them a list of the donor names and re-prompt.
  * If the user types a name not in the list, add that name to the data structure and use it.
  * If the user types a name in the list, use it.
* Once a name has been selected, prompt for a donation amount.

  * Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
  * Add that amount to the donation history of the selected user.

* Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

It is fine for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.

Create a Report
-----------------

* If the user (you) selected "Create a Report," print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
  You do not need to print out all of each donor's donations, just the summary info.
  - Using string formatting, format the output rows as nicely as possible.  The end result should be tabular
   (values in each column should align with those above and below).
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return
  to the original prompt.

* From the original prompt, the user should be able to quit the script cleanly.


Your report should look something like this::

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14


Guidelines
----------

First, factor your script into separate functions. Each of the above
tasks can be accomplished by a series of steps.  Write discreet functions
that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive
programs are a classic use case for the ``while`` loop.

Of course, ``input()`` will be useful here.

Put the functions you write into the script at the top.

# For help getting started, read the following tutorial

Controlling Main Program Flow
-----------------------------

One of the key components of the mailroom program is managing program flow and interacting with the user. Ideally main flow code should be cleanly separate from your feature code.

The best way to manage the program flow of an interactive prompt is to use a ``while True`` loop, which means you will keep asking the user for input until the user selects a feature or exits.

There are several ways to write your main interactive loop. Let's consider these two options:


Option 1:
.........

.. code-block:: python

    def do_something():
        # do things

    def main():
        while True:
            do_something()

    main()

Option 2:
.........

.. code-block:: python

    def do_something()
        # do things
        main()

    def main():
        do_something()

    main()


Can you see the advantages of one example over the other?

In the first one, ``do_something`` is not aware of how the main function works and as you add more features they don't need to know about how the main function works either.
The call stack will also keep getting deeper and deeper, which can make error stack traces hard to debug.

Another advantage is simpler code logic, and simpler code logic means fewer bugs!

Let's look at a simple program to utilize the ``while True`` loop and how we can handle user response:

.. code-block:: python

    import sys  # imports go at the top of the file


    fruits = ['Apples', 'Oranges', 'Pears']

    prompt = "\n".join(("Welcome to the fruit stand!",
              "Please choose from below options:",
              "1 - View fruits",
              "2 - Add a fruit",
              "3 - Remove a fruit",
              "4 - Exit",
              ">>> "))


    def view_fruits():
        print("\n".join(fruits))


    def add_fruit():
        new_fruit = input("Name of the fruit to add?").title()
        fruits.append(new_fruit)


    def remove_fruit():
        purge_fruit = input("Name of the fruit to remove?").title()
        if purge_fruit not in fruits:
            print("This fruit does not exist!")
        else:
            fruits.remove(purge_fruit)

    def exit_program():
        print("Bye!")
        sys.exit()  # exit the interactive script


    def main():
        while True:
            response = input(prompt)  # continuously collect user selection
            # now redirect to feature functions based on the user selection
            if response == "1":
                view_fruits()
            elif response == "2":
                add_fruit()
            elif response == "3":
                remove_fruit()
            elif response == "4":
                exit_program()
            else:
                print("Not a valid option!")


    if __name__ == "__main__":
        # don't forget this block to guard against your code running automatically if this module is imported
        main()



Choosing A Data Structure
-------------------------


So far in this course, we have learned about strings, tuples, and lists. We will apply these data structures to hold
our mailroom donor information.

What goes into this decision to use a specific data structure? Here are a couple of things to consider.

* Efficiency: We often need to look up data; are you able to efficiently look up the data you need?
* Ease of use: Is the code straightforward and simple for basic operations?
* Features: Does the code do everything you need to do for your requirements?

Let's consider each data structure.

A simple string would probably be able to do what we need feature-wise but the code to implement these features would be quite complex and not very efficient.

A tuple would be an issue when adding donors since it is an immutable data structure.

A list would satisfy all of the needed features with a fairly simple code to implement.
It makes the most sense to use a list for the main data structure. Actually, we can use a combination of both tuples and a list.

Here is a potential data structure to consider:

.. code-block:: python

    donor_db = [("William Gates, III", [100.0, 120.10]),
                ("Jeff Bezos", [877.33]),
                ("Paul Allen", [663.23, 343.87, 411.32]),
                ("Mark Zuckerberg", [1660.23, 4320.87, 10432.0]),
                ]

Here we have the first item in a tuple as a donor name, which we will use to determine if we need to add to
existing donor or add a new one and the second item is a list of donation values.

Why choose tuples for the inner donor record? Well, another part of using the right data structure is to reduce bugs;
you are setting clear expectations that a single donor entry only contains two items.


Sorting
-------

Python makes sorting fairly easy and has utilities for sorting simple lists as well as more complex structures like lists of tuples as above.

Let's start with a structure that represents student records: student name and age.

::

    >>> students = [('Bob', 39), ('Joe', 26), ('Jimmy', 40)]

We will use the ``sorted`` function to do the sorting and either sort by name or age. There are actually several ways to accomplish that, we will look at some of them.

The first option is to use optional ``key`` param, which accepts a function object - it can be any custom function we define as long as input and output are correctly implemented.

    >>> def sort_key(student):
            return student[1]
    >>> sorted(students, key=sort_key)
    [('Joe', 26), ('Bob', 39), ('Jimmy', 40)]

``sort_key`` function takes in a single parameter that represents the item in the list, in our case the student record, you then need to return which field should be used for sort comparison. We are using field at index 1, that's the age.


Another option is to use a ``itemgetter`` function from ``operator`` module, it accepts a parameter for list item index value, similar to our ``sort_key`` function:

    >>> from operator import itemgetter
    >>> sorted(students, key=itemgetter(1))
    [('Joe', 26), ('Bob', 39), ('Jimmy', 40)]
    >>> sorted(students, key=itemgetter(0))
    [('Bob', 39), ('Jimmy', 40), ('Joe', 26)]

Using second option makes the most sense in simple cases like above since we're not doing anything complicated and simply need to sort on the index. If our student record also included the last name:

    >>> students = [('Bob Mac', 39), ('Joe Acer', 26), ('Jimmy Lenovo', 40)]

Then the custom function becomes really handy to sort on the last name:

    >>> def sort_key(student):
            return student[0].split(" ")[1]
    >>> sorted(students, key=sort_key)
    [('Joe Acer', 26), ('Jimmy Lenovo', 40), ('Bob Mac', 39)]

"""