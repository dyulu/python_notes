#!/usr/bin/python3

# Coroutines are used for cooperative multitasking where a process voluntarily yield control periodically or when idle
#     in order to enable multiple applications to be run simultaneously

# While both generator and coroutine use yield, generator produces data and coroutine consumes data
def cor_search(pattern):
    while True:
        data_to_consume = (yield)     # Data sent to coroutine will be captured and returned by (yield) expression
        if pattern.lower() in data_to_consume.lower():
            print(data_to_consume)

search = cor_search("Hello")
print(search)                         # <generator object cor_search at 0x7f8119cd69a8>
next(search)                          # Start the coroutine by calling next() to advance the execution to yield
search.send("Hello world")            # Send data to coroutine by calling send(); Hello world
search.send("Python 3")               #
search.close()                        # Close the coroutine
# search.send("Hello world")          # Raise exception StopIteration


# Python 3.5 introduced async/await keywords.
# async is used to declare a function as coroutine
# await is used to call such function
# event loop is the central point of execution for async functions
import asyncio

work_on_vaccine = True
vaccinate = True
hide_from_covid = True
vaccine_dev_count_down = 10
vaccination_count_down = 10

async def develop_covid_vaccine():
    global work_on_vaccine
    global vaccine_dev_count_down

    print("COVID vaccines are crucial in fighting COVID.")
    while(work_on_vaccine):
        if(vaccine_dev_count_down):
            print("    Working on vaccines ...")
            vaccine_dev_count_down -= 1
        else:
            print("Vaccines are available.")
            work_on_vaccine = False
            break

        await asyncio.sleep(1)    # Yield control, sleep 1 sec

async def enforce_social_distancing():
    global hide_from_covid

    print("Social distancing and good hygiene are effective in fighting COVID.")
    while(hide_from_covid):
        print("    Please continue wearing masks and maintaining social distances ...")
        await asyncio.sleep(1)
    else:
        print("End social distancing rules, but good hygiene is always good")

async def vaccinate_people():
    global work_on_vaccine
    global vaccinate
    global vaccination_count_down
    global hide_from_covid

    while(work_on_vaccine):
        await asyncio.sleep(1)

    print("Vaccination is critical.")
    while(vaccinate):
        if(vaccination_count_down):
            print("    Vaccinating and boosting ...")
            vaccination_count_down -= 1
        else:
            print("Reached herd immunity. Hope no new variants")
            vaccinate = False
            hide_from_covid = False
            break

        await asyncio.sleep(1)

async def fighting_covid():
    event_loop = asyncio.get_event_loop()
    covid_tasks = []
    covid_tasks.append(event_loop.create_task(develop_covid_vaccine()))
    covid_tasks.append(event_loop.create_task(enforce_social_distancing()))
    covid_tasks.append(event_loop.create_task(vaccinate_people()))
    try:
        for covid_task in covid_tasks:
            await asyncio.wait_for(covid_task, timeout = 30)
    except asyncio.TimeoutError as e:
        print(e)
        pass

def live_with_covid():
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    try:
        event_loop.run_until_complete(fighting_covid())    # Blocking till all acync tasks are done
    finally:
        print("    Live with COVID, not hiding from it.")
        event_loop.close()

live_with_covid()

