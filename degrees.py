

import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Global mappings for data storage
names = {}  # Maps names to sets of person IDs
people = {}  # Maps person IDs to a dictionary with name, birth year, and movies
movies = {}  # Maps movie IDs to a dictionary with title, year, and cast


def load_data(directory):
    """
    Loads data from CSV files into memory.

    Args:
        directory (str): Path to the directory containing the CSV files.

    Structure:
    - `people`: dictionary mapping person IDs to their details (name, birth year, movies).
    - `names`: dictionary mapping names to sets of person IDs.
    - `movies`: dictionary mapping movie IDs to their details (title, year, cast).
    """
    # Load people data
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies data
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars data
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    """
    Main entry point for the program. Handles user input and outputs results.
    """
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Finds the shortest path between two people using BFS.

    Args:
        source (str): The ID of the starting person.
        target (str): The ID of the target person.

    Returns:
        list: A list of (movie_id, person_id) pairs representing the path, or None if no path exists.
    """
    start = Node(source, None, None)
    frontier = QueueFrontier()
    frontier.add(start)
    
    explored = set()
    
    while not frontier.empty():
        node = frontier.remove()
        
        if node.state == target:
            path = []
            while node.parent is not None:
                path.append((node.movie, node.state))
                node = node.parent
            path.reverse()
            return path
        
        explored.add(node.state)
        
        for movie_id, person_id in neighbors_for_person(node.state):
            if not frontier.contains_state(person_id) and person_id not in explored:
                child = Node(person_id, node, movie_id)
                frontier.add(child)
        
    return None


def person_id_for_name(name):
    """
    Returns the IMDB ID for a person's name, resolving ambiguities if necessary.

    Args:
        name (str): The name of the person.

    Returns:
        str: The person's ID, or None if not found.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns a set of (movie_id, person_id) pairs for people who starred with a given person.

    Args:
        person_id (str): The ID of the person.

    Returns:
        set: A set of (movie_id, person_id) pairs.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
