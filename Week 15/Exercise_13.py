# Exercise 13 - Vanessa Belous

import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def create_db(cursor_obj):

    # Drop the table if it exists (for clean setup)
    cursor_obj.execute("DROP TABLE IF EXISTS population")

    # SQL query to create table
    table_creation_query = """
        CREATE TABLE population (
            City CHAR(50),
            Year INT,
            Population INT
        );
    """
    # Execute table creation query
    cursor_obj.execute(table_creation_query)

    # Confirm table creation
    print("Table population is Ready")

    # Insert data into population table (2023)
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2023, 993468)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2023, 470677)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2023, 409742)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2023, 327390)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2023, 265083)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2023, 228557)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2023, 246695)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2023, 227022)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2023, 203665)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2023, 187872)")

def pop_growth(cursor_obj):
    # 1 - Jacksonville
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2024, 1013337)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2025, 1003204)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2026, 1013236)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2027, 992971)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2028, 1022750)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2029, 1023910)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2030, 1032977)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2031, 1043307)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2032, 1064173)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2033, 1059314)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2034, 1032248)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2035, 1073538)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2036, 1084273)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2037, 1073430)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2038, 1082104)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2039, 1094898)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2040, 1105847)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2041, 1083730)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2042, 1094810)")
    cursor_obj.execute("INSERT INTO population VALUES ('Jacksonville', 2043, 1116242)")

    # 2 - Miami
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2024, 461263)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2025, 465876)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2026, 479852)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2027, 481931)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2028, 475053)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2029, 484554)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2030, 489400)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2031, 479612)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2032, 498796)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2033, 499201)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2034, 503784)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2035, 503784)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2036, 519008)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2037, 513818)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2038, 511924)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2039, 524094)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2040, 508371)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2041, 523724)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2042, 525831)")
    cursor_obj.execute("INSERT INTO population VALUES ('Miami', 2043, 528963)")

    # 3 - Tampa
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2024, 403597)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2025, 394763)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2026, 397911)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2027, 385459)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2028, 380833)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2029, 371281)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2030, 369425)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2031, 369794)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2032, 359484)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2033, 353745)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2034, 346311)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2035, 342140)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2036, 335633)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2037, 337311)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2038, 331243)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2039, 328268)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2040, 324635)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2041, 325934)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2042, 338105)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tampa', 2043, 340193)")

    # 4 - Orlando

    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2024, 331319)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2025, 336290)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2026, 343340)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2027, 346420)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2028, 346073)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2029, 351610)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2030, 357939)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2031, 366897)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2032, 372036)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2033, 374640)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2034, 377637)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2035, 384810)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2036, 389033)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2037, 394479)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2038, 401185)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2039, 409209)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2040, 414528)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2041, 416601)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2042, 417434)")
    cursor_obj.execute("INSERT INTO population VALUES ('Orlando', 2043, 421608)")

    # 5 - St. Petersburg
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2024, 271787)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2025, 269720)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2026, 278924)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2027, 279761)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2028, 273812)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2029, 272393)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2030, 273991)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2031, 272408)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2032, 283230)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2033, 276464)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2034, 271481)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2035, 276427)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2036, 284720)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2037, 294222)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2038, 296878)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2039, 302233)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2040, 305813)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2041, 307597)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2042, 310210)")
    cursor_obj.execute("INSERT INTO population VALUES ('St. Petersburg', 2043, 305099)")

    # 6 - Hialeah
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2024, 228688)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2025, 230064)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2026, 229191)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2027, 230227)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2028, 232042)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2029, 233184)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2030, 233780)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2031, 234312)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2032, 233757)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2033, 232958)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2034, 234449)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2035, 235979)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2036, 237343)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2037, 236703)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2038, 238284)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2039, 237381)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2040, 236793)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2041, 236929)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2042, 236988)")
    cursor_obj.execute("INSERT INTO population VALUES ('Hialeah', 2043, 237346)")

    # 7 - Port St. Lucie
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2024, 248391)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2025, 246031)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2026, 254411)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2027, 262499)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2028, 259040)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2029, 253300)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2030, 258078)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2031, 264887)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2032, 272360)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2033, 274324)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2034, 277143)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2035, 285557)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2036, 284868)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2037, 288675)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2038, 282139)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2039, 284005)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2040, 287556)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2041, 277532)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2042, 281999)")
    cursor_obj.execute("INSERT INTO population VALUES ('Port St. Lucie', 2043, 289335)")

    # 8 - Cape Coral
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2024, 230733)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2025, 229141)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2026, 231189)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2027, 234449)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2028, 236211)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2029, 232593)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2030, 233260)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2031, 236134)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2032, 235935)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2033, 238111)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2034, 235720)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2035, 236999)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2036, 237303)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2037, 239697)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2038, 235307)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2039, 238740)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2040, 242036)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2041, 241556)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2042, 242284)")
    cursor_obj.execute("INSERT INTO population VALUES ('Cape Coral', 2043, 240659)")

    # 9 - Tallahassee
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2024, 205091)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2025, 206751)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2026, 204611)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2027, 205100)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2028, 203506)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2029, 202347)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2030, 204498)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2031, 206172)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2032, 206448)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2033, 207639)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2034, 209796)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2035, 211811)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2036, 213991)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2037, 215640)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2038, 218881)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2039, 217143)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2040, 216664)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2041, 214561)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2042, 213858)")
    cursor_obj.execute("INSERT INTO population VALUES ('Tallahassee', 2043, 214547)")

    # 10 - Fort Lauderdale
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2024, 191834)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2025, 189872)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2026, 194165)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2027, 195454)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2028, 190479)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2029, 188829)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2030, 193853)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2031, 191312)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2032, 190538)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2033, 198906)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2034, 207399)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2035, 217430)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2036, 218557)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2037, 219766)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2038, 221291)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2039, 222874)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2040, 219277)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2041, 219036)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2042, 229158)")
    cursor_obj.execute("INSERT INTO population VALUES ('Fort Lauderdale', 2043, 237887)")

def show_pop(cursor_obj):
    # Let user choose which city they want displayed
    print("Welcome to the City Population Plotter!")
    print("Available Cities:")
    print("\t1 - Jacksonville")
    print("\t2 - Miami")
    print("\t3 - Tampa")
    print("\t4 - Orlando")
    print("\t5 - St. Petersburg")
    print("\t6 - Hialeah")
    print("\t7 - Port St. Lucie")
    print("\t8 - Cape Coral")
    print("\t9 - Tallahassee")
    print("\t10 - Fort Lauderdale")
    choice = int(input("Enter the id of the city you wish to display (eg: 10): "))

    # Plot Jacksonville (1)
    if choice == 1:
        jacksonville = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Jacksonville'")
        year = []
        population = []
        for i in jacksonville:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Jacksonville", fontweight='bold')
        plt.show()

    # Plot Miami (2)
    elif choice == 2:
        miami = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Miami'")
        year = []
        population = []
        for i in miami:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Miami", fontweight='bold')
        plt.show()

    # Plot Tampa (3)
    elif choice == 3:
        tampa = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Tampa'")
        year = []
        population = []
        for i in tampa:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Tampa", fontweight='bold')
        plt.show()

    # Plot Orlando (4)
    elif choice == 4:
        orlando = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Orlando'")
        year = []
        population = []
        for i in orlando:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Orlando", fontweight='bold')
        plt.show()

    # Plot St. Petersburg (5)
    elif choice == 5:
        stPetersburg = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'St. Petersburg'")
        year = []
        population = []
        for i in stPetersburg:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("St. Petersburg", fontweight='bold')
        plt.show()

    # Plot Hialeah (6)
    elif choice == 6:
        hialeah = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Hialeah'")
        year = []
        population = []
        for i in hialeah:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Hialeah", fontweight='bold')
        plt.show()

    # Plot Port St. Lucie (7)
    elif choice == 7:
        stLucie = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Port St. Lucie'")
        year = []
        population = []
        for i in stLucie:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Port St. Lucie", fontweight='bold')
        plt.show()

    # Plot Cape Coral (8)
    elif choice == 8:
        capeCoral = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Cape Coral'")
        year = []
        population = []
        for i in capeCoral:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Cape Coral", fontweight='bold')
        plt.show()

    # Plot Tallahassee (9)
    elif choice == 9:
        tallahassee = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Tallahassee'")
        year = []
        population = []
        for i in tallahassee:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Tallahassee", fontweight='bold')
        plt.show()

    # Plot Fort Lauderdale (10)
    elif choice == 10:
        fortLauderdale = cursor_obj.execute("SELECT year, population FROM population WHERE city = 'Fort Lauderdale'")
        year = []
        population = []
        for i in fortLauderdale:
            year.append(i[0])
            population.append(i[1])
        plt.plot(year, population)
        plt.xlabel("Year", fontweight='bold')
        plt.xticks(np.arange(2023, 2044, 2),
                   ('2023', '2025', '2027', '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043'))
        plt.xticks(rotation=45)
        plt.ylabel("Population", fontweight='bold')
        plt.title("Fort Lauderdale", fontweight='bold')
        plt.show()

    else:
        print("Oops! You entered an invalid choice...")
        print("Please restart.")

def main():
    # Create SQLite database
    connection_obj = sqlite3.connect('population_VB.db')

    # Create cursor object (to interact with db)
    cursor_obj = connection_obj.cursor()

    # Call function to create db
    create_db(cursor_obj)

    # Call function to simulate population growth/decline over next 20 years
    pop_growth(cursor_obj)

    # Call function to show a city's population over time
    show_pop(cursor_obj)

    # Commit changes and close connection to db
    connection_obj.close()

main()
